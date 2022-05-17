#Creo la clase Clientes
class Clients:
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    #Creo la clase Clientes
    def __str__(self):
        return f"{self.name}, {self.age}, {self.country}"

        
