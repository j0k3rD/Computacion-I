class Bingo:
    def __init__(self,big_ball,bombo,ext_balls,last_ball,size_board):
        self.big_ball = big_ball
        self.bombo = bombo
        self.ext_balls = ext_balls
        self.last_ball = last_ball
        self.size_board = size_board

    
    def __str__(self):
        return f"{self.big_ball},{self.bombo},{self.ext_balls},{self.last_ball},{self.size_board}"
    
