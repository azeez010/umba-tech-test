from apiflask import APIBlueprint

from http import HTTPStatus

from app.v1.transactions.models import Transactions
from app.v1.transactions.serializers import TransactionSchema

from app.v1.accounts.models import Account
from app.v1.accounts.serializers import AccountSchema
from umba_lib.helpers.auth import http_token_auth

from umba_lib.models import ModelUtilities
from umba_lib.decorators import ErrorDecorator
from umba_lib.external_apis import IP
from umba_lib.helpers.transactions import TransactionUtils
from umba_lib.enums import TransactionType

transaction_bp = APIBlueprint('transactions', __name__, url_prefix='/transactions')


@transaction_bp.route("<int:pk>/credit",  methods=["POST"])
@transaction_bp.auth_required(http_token_auth)
@transaction_bp.input(AccountSchema.Transact, location='form')
@ErrorDecorator.capture_errors_and_respond
def credit(pk: int, parsed_data: dict, *args, **kwargs):
    """
    Get the account to credit, credit and get the transaction status
    """
    account = ModelUtilities.get(Account, id=pk)
    transaction_status = TransactionUtils.get_transaction_status(account.credit(**parsed_data))
    return TransactionSchema.Retrieve()\
           .dump(ModelUtilities.create(Transactions, ip=IP.my_ip(), account_id=pk, transaction_type=TransactionType.CREDIT.value, **transaction_status, **parsed_data)), HTTPStatus.OK


@transaction_bp.route("<int:pk>/debit",  methods=["POST"])
@transaction_bp.auth_required(http_token_auth)
@transaction_bp.input(AccountSchema.Transact, location='form')
@ErrorDecorator.capture_errors_and_respond
def debit(pk: int, parsed_data: dict, *args, **kwargs):
    """
        Get the account to debit, debit and get the transaction status
    """
    account = ModelUtilities.get(Account, id=pk)
    transaction_status = TransactionUtils.get_transaction_status(account.debit(**parsed_data))
    return TransactionSchema.Retrieve() \
               .dump(ModelUtilities.create(Transactions, ip=IP.my_ip(), account_id=pk, transaction_type=TransactionType.DEBIT.value,
                              **transaction_status, **parsed_data)), HTTPStatus.OK


