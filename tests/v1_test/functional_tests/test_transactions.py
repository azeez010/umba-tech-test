import json, pytest
from decimal import Decimal

from umba_lib.enums import TransactionStatus


class TestTransactions:
    @staticmethod
    def get_account_data(client, login, id_):
        response = client.get("/api/v1/account/%s" % id_, headers={
            "Authorization": "Bearer %s" % login
        })
        return json.loads(response.data.decode('utf-8'))

    @staticmethod
    def credit_account(client, login, id_, amount):
        return client.post("/api/v1/transactions/%s/credit" % id_, data={"amount": amount}, headers={
            "Authorization": "Bearer %s" % login
        })

    @staticmethod
    def debit_account(client, login, id_, amount):
        return client.post("/api/v1/transactions/%s/debit" % id_, data={"amount": amount}, headers={
            "Authorization": "Bearer %s" % login
        })

    @pytest.mark.parametrize("amount", [30, 40, 200])
    @pytest.mark.parametrize("top_up_amount", [200, 322, 31])
    def test_credit(self, app, mocker, account, client, amount, top_up_amount):
        """
        the my_ip is mocked cos it an external call
        the first assert returns 400 cos negative integer is not allowed as amount in request body
        the second assert credit the account and check if it was successful, it also check if the new balance is incremented by the amount deposited
        The last assert credits the wallet with another deposit, it also check if the new balance is incremented by the amount deposited
        """
        mocker.patch("umba_lib.external_apis.IP.my_ip", return_value="127.0.0.1")
        account_data, login = account

        response = self.credit_account(client, login, account_data.get("id"), -abs(amount))
        assert response.status_code == 400

        response = self.credit_account(client, login, account_data.get("id"), amount)
        account_data = self.get_account_data(client, login, account_data.get("id"))
        assert response.status_code == 200
        assert Decimal(account_data.get("account_balance")) == Decimal(amount)

        self.credit_account(client, login, account_data.get("id"), top_up_amount)
        account_data = self.get_account_data(client, login, account_data.get("id"))
        assert Decimal(account_data.get("account_balance")) == Decimal(amount + top_up_amount)

    @pytest.mark.parametrize("initial_amount", [300, 400, 2000])
    @pytest.mark.parametrize("amount", [30, 40, 200])
    def test_debit(self, app, mocker, account, client, initial_amount, amount):
        """
        the my_ip is mocked cos it an external call
        the first assert returns 400 cos negative integer is not allowed as amount in request body
        the second assert credit the account with an initial amount and then debit some amount from it
        it checks if the new account balance reflects the former, it also check if the debit was successful (200 OK)
        The last assert trys to debit the account with money it doesn't have, it is expect for this transaction to fail
        """

        mocker.patch("umba_lib.external_apis.IP.my_ip", return_value="127.0.0.1")
        account_data, login = account

        response = self.debit_account(client, login, account_data.get("id"), -abs(amount))
        assert response.status_code == 400

        self.credit_account(client, login, account_data.get("id"), initial_amount)
        response = self.debit_account(client, login, account_data.get("id"), amount)
        account_data = self.get_account_data(client, login, account_data.get("id"))
        assert response.status_code == 200
        assert Decimal(account_data.get("account_balance")) == Decimal(initial_amount - amount)

        response = self.debit_account(client, login, account_data.get("id"), 1000000)
        transaction_details = json.loads(response.data.decode('utf-8'))
        assert transaction_details.get("transaction_status") == TransactionStatus.FAILED.value
