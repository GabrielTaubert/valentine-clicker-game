"""
last consumable item

opens the last message, player wins and get invitation to a date
"""
from game.item import Item


class Letter(Item):

    def __init__(self, price, name, image):
        Item.__init__(self, price, name, image)