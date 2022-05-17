#Importo las clases que voy a usar
from itertools import combinations_with_replacement
from constants import Constants
from clients import Clients
from book import Book


#Creo la Clase Biblioteca
class Library:
    #Creo listas para libros y clientes de la biblioteca
    books_lst = []
    clients_lst = []
    borrower_books = []


    #Funcion para agregar un libro a la biblioteca.
    def add_book(self):
        name = input(Constants.NAME_BOOK)
        author = input(Constants.AUTHOR)
        isb = int(input("Enter book Code: "))

        book = Book(name, author, isb)
        self.books_lst.append(book)
        print("Book added!")
        return book

    #Funcion para Agregar un cliente
    def add_client(self):
        name = input(Constants.NAME_CLIENT)
        age = input(Constants.AGE_CLIENT)
        country = input(Constants.COUNTRY_CLIENT)

        client = Clients(name,age,country)
        self.clients_lst.append(client)
        print("Client Added!")


    #Funcion para Verificar un cliente de la biblioteca
    def verify_client(self):
        name = input(Constants.NAME_BOOK)
        for i in range(len(self.clients_lst)):
            if self.clients_lst[i].name == name:
                print(Constants.REGISTER)
                return self.clients_lst[i]
        else:
            print(Constants.NOT_REGISTER)
            return None 

    #Funcion para verificar si un libro no se encuentra prestado.
    def verify_book_borrowed(self):
        name_book = input(Constants.NAME_BOOK)
        for i in range(len(self.books_lst)):
            if self.books_lst[i].name == name_book and self.books_lst[i].borrowed == False:
                print(Constants.NOT_BORROWED)
                return self.books_lst[i]
        else:
            print(Constants.BORROWED)
            return None 

    def show_clients(self):
        for i in range(len(self.clients_lst)):
            print(self.clients_lst[i])

    #Funcion para Prestar un Libro
    # def assign(self):
    #     self.verify_client()
    #     self.verify_book_borrowed()
    #     for i ra####
