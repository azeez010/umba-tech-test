from umba_lib.models import BaseModelMixin, db
from app.v1.accounts.models import Account

from werkzeug.security import generate_password_hash


class User(db.Model, BaseModelMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=True)
    email = db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    accounts = db.relationship(Account, backref='user', lazy=True)

    def create(self, **kwargs):
        kwargs["password"] = generate_password_hash(kwargs.get("password"))
        return self.create_(User, **kwargs)

    def list(self, **kwargs):
        return self.list_(User, **kwargs)

    def get(self, **kwargs):
        return self.get_(User, **kwargs)





