import random
from bingo import Bingo
from board import Board
from queue import Queue


class Program:
    queue_extract = Queue()
    queue_nonextract = []
    board_list = []

    def generate_bombo(self,big_ball):
        #Creamos una lista de numeros
        for i in range(0,big_ball):  
            self.queue_nonextract.append(i)
        print("Bombo:", self.queue_nonextract)


    def extract_number(self):
        #Extremos un numero de 
        n = random.choice(self.queue_nonextract)
        self.queue_nonextract.remove(n)
        self.queue_extract.push(n)
        print("Numero Extrido: ", n)
        return n


    def generate_board(self,big_ball):
        size = int(input("Enter board size: "))
        numbers = random.sample(range(int(big_ball)),size)

        board = Board(size,numbers)
        self.board_list.append(board)
        self.show_boards()
        return board
    

    def show_boards(self):
        for i in range(len(self.board_list)):
            print(self.board_list[i])


    def verify_bingo(self):
        for i in range(len(self.board_list)):
            if self.board_list[i].numbers[i] == self.extract_number():

                    return "BINGO BOARD!!"
            else:
                return None


    def generate_bingo(self):

        big_ball = int(input("Enter the biggest ball: "))

        #Generamos los 5 cartones
        car1 = self.generate_board(big_ball)
        car2 = self.generate_board(big_ball)
        car3 = self.generate_board(big_ball)
        car4 = self.generate_board(big_ball)
        car5 = self.generate_board(big_ball)

        self.generate_bombo(big_ball)
        bombo = self.queue_nonextract
        ext_balls = self.queue_extract
        last_ball = self.extract_number()
        size_board = car1.size

        bingo = Bingo(big_ball, bombo, ext_balls, last_ball, size_board)

        for i in range(big_ball):
            if self.verify_bingo() == None:
                self.extract_number()
            elif self.verify_bingo == "BINGO BOARD!!":
                self.show_bingoBoard()


    def show_extract_balls(self):
        print(len(self.queue_extract))
    
    def show_bingoBoard(self):
        for i in range(len(self.served)):
            return self.served[i]
        if self.verify_bingo() == "BINGO BOARD!!":
            print("Bingo's board winner is: ", board.id)
        else:
            return None
    


    
    

    


        


            


        
    

