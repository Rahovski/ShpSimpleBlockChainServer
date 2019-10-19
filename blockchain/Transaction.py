import hashlib
from datetime import datetime


class ClientTransaction:
    __owner = ""
    __receiver = ""
    __amount = 0.0
    __time = ""
    __transaction_hash = ""

    def __init__(self, key_owner, key_receiver, tran_amount):
        self.__owner = key_owner
        self.__receiver = key_receiver
        self.__amount = tran_amount
        self.__time = str(datetime.now())
        self.__transaction_hash = self.calc_tran_hash()

    def calc_tran_hash(self):
        result = self.__owner + self.__receiver + str(self.__amount)
        result = result.encode()
        return hashlib.sha256(result).hexdigest()

    def get_dict(self):
        return dict(From=self.__owner, To=self.__receiver, Amount=self.__amount,
                    Time=self.__time, Hash=self.__transaction_hash)

    @staticmethod
    def to_json(transaction):
        return transaction.get_dict()


