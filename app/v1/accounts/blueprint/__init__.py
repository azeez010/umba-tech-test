from flask import Blueprint, jsonify, request
from http import HTTPStatus

from app.v1.accounts.models import Account
from app.v1.accounts.serializers import AccountSchema

from app.v1.transactions.models import Transactions
from app.v1.transactions.serializers import TransactionSchema

from umba_lib.models import ModelUtilities
from umba_lib.decorators import ErrorDecorator
from umba_lib.helpers.pagination import Pagination
from umba_lib.helpers.auth import AuthUtils


account_bp = Blueprint('account', __name__, url_prefix='/account')


@account_bp.route("/",  methods=["POST"])
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def create(*arg, **kwargs):
    return AccountSchema.Retrieve().dump(ModelUtilities.create(Account, user_id=kwargs["current_user"].id)), HTTPStatus.OK


@account_bp.route("/")
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def list_all(*arg, **kwargs):
    return Pagination.get_paginated_data(ModelUtilities.list(Account, page=request.args.get("page", type=int), per_page=request.args.get("per_page", type=int)), AccountSchema.Retrieve), HTTPStatus.OK


@account_bp.route("/<int:pk>")
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def retrieve(pk, *arg, **kwargs):
    return AccountSchema.Retrieve().dump(ModelUtilities.get(Account, id=pk)), HTTPStatus.OK


@account_bp.route("/<int:pk>",  methods=["DELETE"])
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def destroy(pk, *arg, **kwargs):
    ModelUtilities.delete_one(Account, pk)
    return {}, HTTPStatus.NO_CONTENT


@account_bp.route("/<int:pk>",  methods=["PUT"])
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def update(pk, *args, **kwargs):
    errors = AccountSchema.Update().validate(request.form)
    if errors:
        return jsonify(errors), HTTPStatus.BAD_REQUEST
    return AccountSchema.Retrieve().dump(ModelUtilities.update_one(Account, request.form, pk)), HTTPStatus.OK


@account_bp.route("<int:pk>/transactions",  methods=["get"])
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def transactions(pk, *args, **kwargs):
    return TransactionSchema.Retrieve().dump(ModelUtilities.list(Transactions, account_id=pk), many=True), HTTPStatus.OK
