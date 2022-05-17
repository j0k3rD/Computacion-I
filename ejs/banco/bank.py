from queue import Queue
from client import Client


class Bank:
    clients = []
    queue1 = Queue()
    queue2 = Queue()
    served = []

    def add_to_register(self):
        with open("reg.txt", "w", encoding="UTF-8") as R1:
            R1.write("Clientes:\n")
            if len(self.clients) == 0:
                R1.write("\n")
            else:
                R1.write("\n")    
                for client in range (len(self.clients)):
                    R1.write(str(self.clients[client])+("\n")) ##sumar str
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
            if len(self.served) == 0:
                R1.write("\n")
            else:
                R1.write("\n")
                for client in range (len(self.served)):                
                    R1.write(str(self.served[client])+("\n"))
                R1.write("\n")

    def add_client(self):
        name = input("Enter Client Name: ")
        sur = input("Enter CLient Surname: ")
        id = input("Enter Client ID: ")
        client = Client(name, sur, id, state=False) #Lo puedo hardcodear al ultimo o dejar 
        if len(self.clients) == 0:
            self.clients.append(client)
            print(self.show_client())
            print("Client added!")
        else:
            for i in range(len(self.clients)):
                if self.clients[i].name == client.name:
                    print(f'{client.name} already exist!')
                else:
                    self.clients.append(client)
                    self.show_client()
                    print("Client added!")


    def show_client(self):
        print("\nClients:\n")
        for i in range(len(self.clients)):
            return self.clients[i]
        
        
    def show_queue1(self):
        print("Clients in Queue1:\n")
        for i in range(len(self.queue1.list)):
            return self.queue1.list[i]
    

    def show_queue2(self):
        print("Clients in Queue2:\n")
        for i in range(len(self.queue2.list)):
            print(self.queue2.list[i])


    def show_served(self):
        print("Clients Served:\n")
        for i in range(len(self.served)):
            return self.served[i]


    def verify_client(self, name):
        for i in range (len(self.clients)):
            if self.clients[i].name == name:
                return self.clients[i]
        return None


    def add_client_to_queue(self):
        name = input("Insert client name: ")
        client = self.verify_client(name)
        if client != None:
            q = str(input("Enter the Queue to add (1 or 2): "))
            if q == "1":
                self.queue1.push(client)
                self.show_queue1()

            elif q == "2":
                self.queue2.push(client)
                self.show_queue2()
            else:
                print('Invalid Option')
        else:
            print("Client dont exist!")


    def call_verify_client_in_queue(self):
        name = input("Insert client name: ")
        client = self.verify_client(name)
        
        if client != None:
            q = int(input("Enter the client's queue: "))
            if q == 1:
                for i in range(len(self.queue1.list)):
                    if self.queue1.list[i].name == client.name:
                        self.queue1.pop()
                        client.state = True
                        self.served.append(client)
                        print(f"{client.name} been served") 
            elif q == 2:
                for i in range(len(self.queue2.list)):
                    if self.queue2.list[i].name == client.name:
                        self.queue2.pop()
                        client.state = True
                        self.served.append(client)
                        print(f"{client.name} been served")


    def show_queue_stats(self):
        fd = open("reg.txt", )
        print("\nNumber of Clients:\n")
        print(len(self.clients))
        print("\n")
        print(self.show_queue1())
        print("\n")
        print(self.show_queue2())
        print("\n")
        print(self.show_served())



