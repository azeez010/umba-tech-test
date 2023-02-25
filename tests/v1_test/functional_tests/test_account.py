class TestAccount:
    def test_get_account(self, app, login, client):
        response = client.get("/api/v1/account/")
        assert response.status_code == 401

        response = client.get("/api/v1/account/", headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_create_account(self, app, login, client):
        response = client.post("/api/v1/account/")
        assert response.status_code == 401

        response = client.post("/api/v1/account/", headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_account_transaction(self, app, account, client):
        account_data, login = account

        response = client.get("/api/v1/account/%s/transactions" % account_data.get("id"), headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_retrieve_account(self, app, account, client):
        account_data, login = account

        response = client.get("/api/v1/account/%s" % account_data.get("id"), headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_update_account(self, app, account, client):
        account_data, login = account

        response = client.put("/api/v1/account/%s" % account_data.get("id"), data={"account_type": "PRO"}, headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 200

    def test_delete_account(self, app, account, client):
        account_data, login = account

        response = client.delete("/api/v1/account/%s" % account_data.get("id"), headers={
            "Authorization": "Bearer %s" % login
        })

        assert response.status_code == 204