from umba_lib.models import BaseModelMixin, db
from umba_lib.enums import TransactionType, TransactionStatus


class Transactions(db.Model, BaseModelMixin):
    __tablename__ = 'transaction'
    id = db.Column(db.Integer, primary_key=True)
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    transaction_status = db.Column(db.Enum(TransactionStatus), default=TransactionStatus.PENDING.value)
    transaction_type = db.Column(db.Enum(TransactionType))
    ip = db.Column(db.String, nullable=False)
    amount = db.Column(db.Numeric(precision=10, scale=2), default="0.00", nullable=False)
