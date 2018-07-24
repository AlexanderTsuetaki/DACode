#location.py
#row,col location in battleship game
#2/23/2016
__author__="Alexander Tsuetaki"

class Location:
    row = -1
    col = -1
    ship_type= ' '
    revealed = False
    hit= False
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.ship_type = ' '
    def __str__(self):
        if self.revealed:
            return'*'
        elif self.hit:
            return'X'
        else:
            return self.ship_type
