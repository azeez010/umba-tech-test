import jwt

from functools import wraps
from flask import request, jsonify
from settings.config import app

from app.v1.users.models import User
from umba_lib.models import ModelUtilities


class AuthUtils:
    @staticmethod
    def token_required(f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None

            if request.headers.get("Authorization"):
                token = request.headers.get("Authorization").split(" ")[-1].strip()

            # return 401 if token is not passed
            if not token:
                return jsonify({'message': 'Token is missing !!'}), 403

            try:
                # decoding the payload to fetch the stored details
                data = jwt.decode(token, app.config.get('SECRET_KEY'), algorithms=["HS256"])
                current_user = ModelUtilities.get(User, email=data['email'])
            except:
                return jsonify({
                    'message': 'Token is invalid !!'
                }), 403
            # returns the current logged in users context to the routes
            kwargs["current_user"] = current_user
            return f(*args, **kwargs)

        return decorated
