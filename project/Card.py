
# This is a single-line comment
# Julian Cochran
# 1-19-2016
# Card.py
# Learning about object-oriented design, encapsulation and how to work with PyCharm

class Card:
    suit = None
    value = 0
    name = None

    # this is the definition of the init method
    # the stuff in (parentheses) is called parameters
    # we use this "special" method indirectly to create
    # objects of the Card class
    def __init__(self, su, va):
        self.suit = su
        if va == 11:
            self.value = 10
            self.name = "Jack of " + su
        elif va == 12:
            self.value = 10
            self.name = "Queen of " + su
        elif va == 13:
            self.value = 10
            self.name = "King of " + su
        elif va == 14:
            self.value = 11
            self.name = "Ace of " + su
        else:
            self.value = va
            self.name = str(va) + " of " + su

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

    def __eq__(self, other):
        return self.value == other.value
    def __lt__(self, other):
        return self.value < other.value
    def __gt__(self, other):
        return self.value > other.value








