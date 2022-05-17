class Client:
    def __init__(self, name, surname, ident, state=False): #False= Espera, True=Atendido ##Todo lo igual lo dejo a lo ultimo
        self.name = name
        self.surname = surname
        self.ident = ident
        self.state = state
    
    def __str__(self):
        return f"{self.name}, {self.surname}, {self.ident}, {self.state}"

        