# color.py
# Returns various tuple representations of colors
# 03-23-2016
__author__ = "Julian Cochran"

import random

class Color:
    BLACK = (0,0,0)
    RED = (255,0,0)
    GREEN = (0,255,0)
    DARKGREEN = (0,153,0)
    BLUE = (0,0,255)
    YELLOW = (255,255,0)
    ORANGE = (255,128,0)
    PURPLE = (127,0,255)
    PINK = (255,0,255)
    WHITE = (255,255,255)

    @staticmethod
    def random_color():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)