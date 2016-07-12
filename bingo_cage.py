import random


class BingoCage:

    def __init__(self, items):
        self._items = list(items)


    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('The bingo cage is empty')

