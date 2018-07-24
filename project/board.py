#board.py
#represents hte 10 x 10 row x col grid in battleship game
# 2/23/2016
__author__ = "alexander Tsuetaki"

from location import Location
class Board:
    ocean=[]
    def __init__(self):
        self.ocean = []
        for i in range(0,10):
            self.ocean.append([])
            for j in range(0,10):
                self.ocean[i].append(Location(i, j))
    def __str__(self):
        rowCount = 0
        to_string = ' '
        to_string += '   0   1   2   3   4   5   6   7   8   9 \n'
        print self.ocean
        for i in self.ocean:
            to_string += '  --- --- --- --- --- --- --- --- --- --- ---\n'
            to_string += (str(rowCount)+' | ')
            for j in i:
                to_string += (str(j) +' | ')
            to_string += ' \n'
            rowCount += 1
        to_string += '  --- --- --- --- --- --- --- --- --- --- --- \n'
        return to_string
