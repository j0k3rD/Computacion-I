from book import Book

class Library:
    books = []
    authors = []
    readers = []
    borroweds = []


    def addBook(self,book):
        self.books.append(book)
        print("Book Added!")
    

    def addAuthor(self, author):
        self.authors.append(author)
        print("Author Added!")


    def addReader(self,reader):
        self.readers.append(reader)
        print("Reader Added!")


    def viewBook(self):
        for book in self.books:
            print(book)
    

    def viewAuthor(self):
        for author in self.authors:
            print(author)


    def verify_reader(self, name):
        for i in len(self.readers):
            if self.readers[i].name == name:
                return self.readers[i]
        return None


    def verify_book(self, title):
        for i in len(self.books):
            if self.books[i].title == title:
                return self.books[i]
        return None


    def change_ident(self, book):
        if book.ident == True:
            print("Book borrowed!")
        else:
            book.ident = True
            print("Book available!")

    def addBorrowed(self):

        name = input("Enter reader's name: ")
        title = input("Enter reader's name: ")
        reader = self.verify_reader(name)
        book = self.verify_book(title)

        if reader == None or book == None:
            print("Reader or Book Not Exist!")

        elif reader.n_borrowed_books <= 4:
            self.change_ident(book)
            reader.n_borrowed_books += 1
            print("Borrowed Added!")
        
        elif reader.n_borrowed_books > 4:
            print("Maximum limit of borrowed books!!, return one to request another.")

    def return_book(self):
        days = input("Days to return: ")
        name = input("Enter reader's name: ")
        reader = self.verify_reader(name)
        if reader != None and days > 30:
            x = days -30
            fouls = x * 2
            reader.d_fouls = fouls
            

            
#print("{} has been borrowed to {}".format(self.title, Reader.name))        
#  print("ERROR. Reader is not defined or Book is borrowed.")