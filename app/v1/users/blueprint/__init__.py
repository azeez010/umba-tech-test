from flask import request
from apiflask import APIBlueprint
from http import HTTPStatus

from app.v1.users.models import User
from app.v1.users.serializers import UserSchema

from umba_lib.models import ModelUtilities
from umba_lib.decorators import ErrorDecorator
from umba_lib.helpers.auth import http_token_auth

user_bp = APIBlueprint('user', __name__, url_prefix='/user')


@user_bp.route("/",  methods=["POST"])
@user_bp.input(UserSchema.Create, location='form')
@ErrorDecorator.capture_errors_and_respond
def create(parsed_data, *args, **kwargs):
    return UserSchema.Retrieve().dump(User().create(**parsed_data)), HTTPStatus.OK


@user_bp.route("/",  methods=["GET"])
@user_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def list_all(*args, **kwargs):
    return UserSchema.Retrieve().dump(ModelUtilities.list(User), many=True), HTTPStatus.OK


@user_bp.route("/<int:pk>")
@user_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def retrieve(pk, *args, **kwargs):
    return UserSchema.Retrieve().dump(ModelUtilities.get(User, id=pk)), HTTPStatus.OK


@user_bp.route("/<int:pk>",  methods=["DELETE"])
@user_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def destroy(pk, *args, **kwargs):
    ModelUtilities.delete_one(User, pk)
    return {}, HTTPStatus.NO_CONTENT


@user_bp.route("/<int:pk>",  methods=["PUT"])
@user_bp.input(UserSchema.Update, location='form')
@user_bp.auth_required(http_token_auth)
@ErrorDecorator.capture_errors_and_respond
def update(pk, *args, **kwargs):
    return UserSchema.Retrieve().dump(ModelUtilities.update_one(User, request.form, pk)), HTTPStatus.OK
