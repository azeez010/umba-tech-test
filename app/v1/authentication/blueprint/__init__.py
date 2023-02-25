import jwt

from flask import Blueprint, request, jsonify, make_response

from werkzeug.security import check_password_hash
from datetime import datetime, timedelta

from app.v1.users.models import User
from settings.config import app

from umba_lib.models import ModelUtilities

authentication_bp = Blueprint('auth', __name__, url_prefix='/auth')


@authentication_bp.route('/login', methods=['POST'])
def login():
    # creates dictionary of form data
    auth = request.form

    if not auth or not auth.get('email') or not auth.get('password'):
        # returns 401 if any email or / and password is missing
        return make_response(
            {"message": "Could not verify"},
            401,
            {'WWW-Authenticate': 'Basic realm ="Login required !!"'}
        )

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