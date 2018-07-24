#ship.py
#data representation of a ship object for battleship game
#2/25/2016
__author__="Alexander Tsuetaki"

from location import Location

class Ship:
    type = None
    size = 0
    orientation = None
    coordinates= None
    alive =None

    def __init__(self, ty, le, ori, coords):
        self.type = ty
        self.length = le
        self.orientation = ori
        self.coordinates = []
        self.coordinates = coords