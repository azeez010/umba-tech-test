from umba_lib.enums import AccountType

from settings.database import ma
from app.v1.accounts.models import Account
from marshmallow import fields
from marshmallow.validate import Range


class AccountSchema:
    class Create(ma.SQLAlchemyAutoSchema):
        user_id = fields.Int(required=True)

        class Meta:
            exclude = ("transactions",)
            model = Account

    class Retrieve(ma.SQLAlchemyAutoSchema):
        account_name = fields.Str()
        number_of_transactions = fields.Int()
        account_type = fields.Enum(AccountType)

        class Meta:
            exclude = ("transactions",)
            model = Account

    class Update(ma.SQLAlchemyAutoSchema):
        account_type = fields.Enum(AccountType)

        class Meta:
            exclude = ("transactions",)
            model = Account

    class Transact(ma.SQLAlchemySchema):
        amount = fields.Int(required=True, validate=[Range(min=0, error="Value must be greater than -1")])

        class Meta:
            model = Account
