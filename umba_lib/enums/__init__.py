from enum import Enum


class BaseEnum(Enum):
    @classmethod
    def choices(cls):
        return [(i.value, i.name) for i in cls]

    @classmethod
    def values(cls):
        return list(i.value for i in cls)

    @classmethod
    def count(cls):
        return len(cls)

    @classmethod
    def mapping(cls):
        return dict((i.name, i.value) for i in cls)


class TransactionType(BaseEnum):
    CREDIT = "CREDIT"
    DEBIT = "DEBIT"


class AccountType(BaseEnum):
    SAVING = "SAVING"
    PRO = "PRO"
    DOM = "DOM"
    CURRENT = "CURRENT"


class TransactionStatus(BaseEnum):
    PENDING = "PENDING"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
