"""
second consumable item -> second least expensive item

automatic heart gen without clicking +1
"""
from game.item import Item


class HouseKey(Item):

    def __init__(self, price, name, image):
        Item.__init__(self, price, name, image)