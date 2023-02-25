from flask import request
from apiflask import APIBlueprint
from http import HTTPStatus


from app.v1.accounts.models import Account
from app.v1.accounts.serializers import AccountSchema

from app.v1.transactions.models import Transactions
from app.v1.transactions.serializers import TransactionSchema

from umba_lib.models import ModelUtilities
from umba_lib.decorators import ErrorDecorator
from umba_lib.helpers.pagination import Pagination
from umba_lib.helpers.auth import http_token_auth


account_bp = APIBlueprint('account', __name__, url_prefix='/account')


@account_bp.route("/",  methods=["POST"])
@account_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def create(*arg, **kwargs):
    return AccountSchema.Retrieve().dump(ModelUtilities.create(Account, user_id=http_token_auth.current_user.id)), HTTPStatus.OK


@account_bp.route("/")
@account_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def list_all(*arg, **kwargs):
    return Pagination.get_paginated_data(ModelUtilities.list(Account, page=request.args.get("page", type=int), per_page=request.args.get("per_page", type=int)), AccountSchema.Retrieve), HTTPStatus.OK


@account_bp.route("/<int:pk>")
@account_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def retrieve(pk, *arg, **kwargs):
    return AccountSchema.Retrieve().dump(ModelUtilities.get(Account, id=pk)), HTTPStatus.OK


@account_bp.route("/<int:pk>",  methods=["DELETE"])
@account_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def destroy(pk, *arg, **kwargs):
    ModelUtilities.delete_one(Account, pk)
    return {}, HTTPStatus.NO_CONTENT


@account_bp.route("/<int:pk>",  methods=["PUT"])
@account_bp.auth_required(http_token_auth)
@account_bp.input(AccountSchema.Update, location="form")
@ErrorDecorator.capture_errors_and_respond
def update(pk, parsed_data, *args, **kwargs):
    return AccountSchema.Retrieve().dump(ModelUtilities.update_one(Account, parsed_data, pk)), HTTPStatus.OK


@account_bp.route("<int:pk>/transactions",  methods=["get"])
@account_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def transactions(pk, *args, **kwargs):
    return TransactionSchema.Retrieve().dump(ModelUtilities.list(Transactions, account_id=pk), many=True), HTTPStatus.OK
