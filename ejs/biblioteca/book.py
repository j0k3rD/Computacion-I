class Book:

    def __init__(self,title,type,editorial,year,author,b_days=0,ident=False):        

        self.ident = ident
        self.title = title
        self.type = type
        self.editorial = editorial
        self.year = year
        self.author = author
        self.b_days = b_days
    

    def __str__(self):
        return f"{self.title}, {self.type}, {self.editorial}, {self.year}, {self.author}"
