from flask import Blueprint
from app.v1.users.blueprint import user_bp
from app.v1.accounts.blueprint import account_bp
from app.v1.transactions.blueprint import transaction_bp
from app.v1.authentication.blueprint import authentication_bp


api_v1 = Blueprint("v1", __name__, url_prefix="/api/v1")
api_v1.register_blueprint(user_bp)
api_v1.register_blueprint(account_bp)
api_v1.register_blueprint(transaction_bp)
api_v1.register_blueprint(authentication_bp)
