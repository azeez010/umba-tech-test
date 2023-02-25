from flask import Blueprint, jsonify, request
from http import HTTPStatus

from app.v1.transactions.models import Transactions
from app.v1.transactions.serializers import TransactionSchema

from app.v1.accounts.models import Account
from app.v1.accounts.serializers import AccountSchema
from umba_lib.helpers.auth import AuthUtils

from umba_lib.models import ModelUtilities
from umba_lib.decorators import ErrorDecorator
from umba_lib.external_apis import IP
from umba_lib.helpers.transactions import TransactionUtils
from umba_lib.enums import TransactionType

transaction_bp = Blueprint('transactions', __name__, url_prefix='/transactions')


@transaction_bp.route("<int:pk>/credit",  methods=["POST"])
@AuthUtils.token_required
@ErrorDecorator.capture_errors_and_respond
def credit(pk, *args, **kwargs):
    errors = AccountSchema.Transact().validate(request.form)
    if errors:
        return jsonify(errors), HTTPStatus.BAD_REQUEST

    account = ModelUtilities.get(Account, id=pk)

    transaction_status = TransactionUtils.get_transaction_status(account.credit(**request.form))

    return TransactionSchema.Retrieve()\
           .dump(ModelUtilities.create(Transactions, ip=IP.my_ip(), account_id=pk, transaction_type=TransactionType.CREDIT.value, **transaction_status, **request.form)), HTTPStatus.OK


@transaction_bp.route("<int:pk>/debit",  methods=["POST"])
@AuthUtils.token_required
@ErrorDecorator.capture_errors_and_respond
def debit(pk, *args, **kwargs):
    errors = AccountSchema.Transact().validate(request.form)
    if errors:
        return jsonify(errors), HTTPStatus.BAD_REQUEST

    account = ModelUtilities.get(Account, id=pk)

    transaction_status = TransactionUtils.get_transaction_status(account.debit(**request.form))

    return TransactionSchema.Retrieve() \
               .dump(ModelUtilities.create(Transactions, ip=IP.my_ip(), account_id=pk, transaction_type=TransactionType.DEBIT.value,
                              **transaction_status, **request.form)), HTTPStatus.OK


