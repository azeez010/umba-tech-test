from settings.database import ma
from app.v1.transactions.models import Transactions
from marshmallow import fields
from umba_lib.enums import TransactionType, TransactionStatus


class TransactionSchema:
    class Retrieve(ma.SQLAlchemyAutoSchema):
        transaction_status = fields.Enum(TransactionStatus)
        transaction_type = fields.Enum(TransactionType)

        class Meta:
            model = Transactions
