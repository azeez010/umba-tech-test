from flask import Blueprint, jsonify, request
from http import HTTPStatus

from app.v1.users.models import User
from app.v1.users.serializers import UserSchema
from umba_lib.helpers.auth import AuthUtils
from umba_lib.models import ModelUtilities
from umba_lib.decorators import ErrorDecorator

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route("/",  methods=["POST"])
def create():
    errors = UserSchema.Create().validate(request.form)
    if errors:
        return jsonify(errors), HTTPStatus.BAD_REQUEST

    return UserSchema.Retrieve().dump(User().create(**request.form)), HTTPStatus.OK


@user_bp.route("/")
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def list_all(*args, **kwargs):
    return UserSchema.Retrieve().dump(ModelUtilities.list(User), many=True), HTTPStatus.OK


@user_bp.route("/<int:pk>")
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def retrieve(pk, *args, **kwargs):
    return UserSchema.Retrieve().dump(ModelUtilities.get(User, id=pk)), HTTPStatus.OK


@user_bp.route("/<int:pk>",  methods=["DELETE"])
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def destroy(pk, *args, **kwargs):
    ModelUtilities.delete_one(User, pk)
    return {}, HTTPStatus.NO_CONTENT


@user_bp.route("/<int:pk>",  methods=["PUT"])
@ErrorDecorator.capture_errors_and_respond
@AuthUtils.token_required
def update(pk, *args, **kwargs):
    errors = UserSchema.Update().validate(request.form)
    if errors:
        return jsonify(errors), HTTPStatus.BAD_REQUEST
    return UserSchema.Retrieve().dump(ModelUtilities.update_one(User, request.form, pk)), HTTPStatus.OK
