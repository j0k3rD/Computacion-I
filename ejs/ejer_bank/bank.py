from asyncore import write
from queue import Queue
from client import Client
from constants import Constants

class Bank:
    queue1 = Queue()
    queue2 = Queue()
    client_wait_lst = []
    clients_served = []

    #Funcion para crear un Cliente
    def add_client(self):
        name = input(Constants.ASK_CLIENT_NAME)
        ident = input("Enter the client ID: ")

        client = Client(name,ident)
        self.client_wait_lst.append(client)
        print("Client was Added!")
        self.register_data()
        print(self.show_client_lst())
        return client
        
    #Funcion para verificar cliente
    def call_client(self):
        name = input(Constants.ASK_CLIENT_NAME)
        for i in range(len(self.client_lst)):
            if self.client_lst[i].name == name:
                self.client_wait_lst[i].state = True
                self.clients_served.append(self.client_wait_lst[i])
                return self.client_wait_lst[i]
        return None


    #Funcion agregar a una cola
    def add_client_to_queue(self):
        name = input(Constants.ASK_CLIENT_NAME)
        qNum = input("Enter queue number (1 or 2): ")
        if qNum == 1:
            for i in range(len(self.client_lst)):
                if self.client_wait_lst[i].name == name:
                    self.queue1.push(self.client_wait_lst[i])
    

    #Funcion verificar Cliente en Cola
    def verify_client_queue(self):
        name = input(Constants.ASK_CLIENT_NAME)
        qNum = input("Enter queue number (1 or 2): ")
        if qNum == 1:
            for i in range(len(self.queue1.list)):
                if self.queue1.list[i].name == name:
                    return self.queue1.list[i]
            return None
        elif qNum == 2:
            for i in range(len(self.queue1.list)):
                if self.queue2.list[i].name == name:
                    return self.queue2.list[i]
            return None
    

    #Funcion ver Lista de Clientes
    def show_client_lst(self):
        print("\nClients:\n")
        for i in range(len(self.client_wait_lst)):
            return self.client_wait_lst[i]


    #Funcion ver Cola 1
    def show_queue1(self):
        print("\nQueue1:\n")
        for i in range(len(self.queue1.list)):
            return self.queue1.list[i]


    #Funcion ver Cola 2
    def show_queue2(self):
        print("\nQueue2:\n")
        for i in range(len(self.queue2.list)):
            return self.queue2.list[i]

    #Funcion ver Clientes Atendido
    def show_served(self):
        print("\nServed Clients:\n")
        for i in range(len(self.clients_served)):
            return self.clients_served[i]


    #Funcion para ver Registros
    def show_register(self):
        print(len(self.client_wait_lst))
        print(self.show_client_lst())
        print("\n")
        print(self.show_queue1())
        print("\n")
        print(self.show_queue2())
        print("\n")        
        print(self.show_served())
        print("\n")     

    #Funcion Registrar cambios en archivo
    def register_data(self):
        with open("reg.txt", "w", encoding="UTF-8") as R1:
            R1.write("Clientes:\n")
            if len(self.client_wait_lst) == 0:
                R1.write("\n")
            else:
                R1.write("\n")    
                for client in range (len(self.client_wait_lst)):
                    R1.write(str(self.client_wait_lst[client])+("\n")) ##sumar str
                R1.write("\n")

            R1.write("Queue 1:\n")
            if len(self.queue1.list) == 0:
                R1.write("\n")
            else:
                R1.write("\n")
                for client in range (len(self.queue1.list)):                
                    R1.write(str(self.queue1.list[client])+("\n"))
                R1.write("\n")

            R1.write("Queue 2:\n")
            if len(self.queue2.list) == 0:
                R1.write("\n")
            else:
                R1.write("\n")
                for client in range (len(self.queue2.list)):                
                    R1.write(str(self.queue2.list[client])+("\n"))
                R1.write("\n")
            
            R1.write("Clients Served:\n")
            if len(self.clients_served) == 0:
                R1.write("\n")
            else:
                R1.write("\n")
                for client in range (len(self.clients_served)):                
                    R1.write(str(self.clients_served[client])+("\n"))
                R1.write("\n")

