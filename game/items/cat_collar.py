"""
third consumable item

add's a cat above the shop bar, which walks around it
"""
from game.item import Item


class CatCollar(Item):

    def __init__(self, price, name, image):
        Item.__init__(self, price, name, image)