"""
fourth consumable item

add's +2 to the heart gen
"""
from game.item import Item


class DiamondRing(Item):

    def __init__(self, price, name, image):
        Item.__init__(self, price, name, image)