import book

class Reader:
    def __init__(self, name, n_borrowed_books, d_fouls):
        self.name = name
        self.borrowed_books = n_borrowed_books
        self.fouls = d_fouls
    def __str__(self):
        return f"{self.name}, {self.borrowed_books}, {self.ticket}"
    
