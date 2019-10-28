from typing import List, Iterator
from transfer_objects.transaction import Transaction
from copy import copy


class TransactionList:
    """A list of transactions.

    :Author: Aris Fernandez
    """
    def __init__(self):
        self.__transactions: List[Transaction] = list()

    def __len__(self) -> int:
        return self.__transactions.__len__()

    def __iter__(self) -> Iterator[Transaction]:
        self.__num = 0

        def generate():
            while True:
                try:
                    yield self.__transactions[self.__num]
                    self.__num += 1
                except IndexError:
                    del self.__num
                    return

        return generate()

    def add_transaction(self, transaction: Transaction):
        self.__transactions.append(copy(transaction))

    def get_transaction(self, index: int) -> Transaction:
        return self.__transactions[index]
