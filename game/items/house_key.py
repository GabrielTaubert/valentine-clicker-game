"""
second consumable item -> second least expensive item

automatic heart gen without clicking +1
"""
from game.item import Item


class HouseKey(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 100
        self.name = "House Key"