#Creo la clase Libro
class Book:
    def __init__(self, name, author, isb, borrowed = False): #Si es False es que no está prestado, True para libros que si se prestaron.
        self.name = name
        self.author = author
        self.isb = isb
        self.borrowed = borrowed

#Creo el metodo str que es el que me convierte a texto mis variables
    def __str__(self) -> str:
        return f"{self.name}, {self.author}, {self.isb}, {self.borrowed}"
