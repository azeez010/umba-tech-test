from umba_lib.enums import AccountType
from umba_lib.models import BaseModelMixin, db
from app.v1.transactions.models import Transactions
from decimal import Decimal


class Account(db.Model, BaseModelMixin):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    account_balance = db.Column(db.Numeric(precision=10, scale=2), default="0.00", nullable=False)
    transactions = db.relationship(Transactions, backref='account', lazy=True)
    account_type = db.Column(db.Enum(AccountType), default=AccountType.SAVING.value)

    @property
    def account_name(self) -> str:
        return "%s %s" % (self.user.first_name, self.user.last_name)

    @property
    def number_of_transactions(self) -> int:
        return len(self.transactions)

    def credit(self, amount) -> bool:
        self.account_balance += Decimal(amount)
        db.session.commit()
        return True

    def debit(self, amount) -> bool:
        if 0 < self.account_balance >= Decimal(amount):
            self.account_balance -= Decimal(amount)
            db.session.commit()
            return True
        return False

