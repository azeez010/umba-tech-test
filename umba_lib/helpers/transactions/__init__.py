from umba_lib.enums import TransactionStatus


class TransactionUtils:
    @staticmethod
    def get_transaction_status(transaction_result):
        if transaction_result:
            return dict(transaction_status=TransactionStatus.COMPLETED.value)
        else:
            return dict(transaction_status=TransactionStatus.FAILED.value)
