"""
fourth consumable item

add's +2 to the heart gen
"""
from game.item import Item


class DiamondRing(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 100
        self.name = "Diamond Ring"