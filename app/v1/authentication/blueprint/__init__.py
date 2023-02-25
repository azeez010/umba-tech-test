import jwt

from flask import request, jsonify, make_response
from apiflask import APIBlueprint

from werkzeug.security import check_password_hash
from datetime import datetime, timedelta

from app.v1.users.models import User
from settings.config import app

from app.v1.authentication.serializers import LoginSchema
from umba_lib.models import ModelUtilities


authentication_bp = APIBlueprint('auth', __name__, url_prefix='/auth')


@authentication_bp.route('/login', methods=['POST'])
@authentication_bp.input(LoginSchema, location="form")
def login(auth, *args, **kwargs):
    user = ModelUtilities.get(User, email=auth.get('email'))

    if not user:
        # returns 401 if user does not exist
        return make_response(
            {"message": "Could not verify"},
            401,
            {'WWW-Authenticate': 'Basic realm ="User does not exist !!"'}
        )

    if check_password_hash(user.password, auth.get('password')):
        # generates the JWT Token
        token = jwt.encode({
            'email': user.email,
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config.get('SECRET_KEY'))

        return make_response(jsonify({'token': token}), 201)
    # returns 403 if password is wrong
    return make_response(
        {"message": "Could not verify"},
        403,
        {'WWW-Authenticate': 'Basic real "Wrong Password !!"'}
    )