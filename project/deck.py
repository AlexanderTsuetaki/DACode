# deck.py
# simulates a deck of cards
# Julian Cochran
# 01/21/2016

import random # random is a library of the Python language
from Card import Card

suits = ["Clubs","Diamonds","Hearts","Spades"]
values = [2,3,4,5,6,7,8,9,10,11,12,13,14]
deck = []

for suit in suits:
    for val in values:
        deck.append(Card(suit, val))

print("*** sorted deck here ***")
print(deck)

random.shuffle(deck)
print("*** shuffled deck here ***")
print(deck)
