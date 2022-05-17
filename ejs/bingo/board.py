import itertools
import resource

class Board:
    newID = itertools.count()
    def __init__(self,size,numbers):
        self.ident = next(self.newID)
        self.size = size
        self.numbers = numbers

    def __str__(self):
        return f"{self.ident},{self.size},{self.numbers}"

