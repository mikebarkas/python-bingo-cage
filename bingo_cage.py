import random


class BingoCage:
    """A callable class that will return a pick from the cage."""
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('The bingo cage is empty')

    def __call__(self):
        return self.pick()
