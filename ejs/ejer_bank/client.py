class Client:
    def __init__(self, name, ident, state=False): #False: Esperando, True: Atendido
        self.name = name
        self.ident = ident
        self.state = state

    def __str__(self):
        return f"{self.name}, {self.ident}, {self.state}"