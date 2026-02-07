"""
first consumable item -> least expensive item

add's a buff to the heart gen with +1
"""
from game.item import Item


class ChocolateBox(Item):

    def __init__(self, price, name, image):
        Item.__init__(self, price, name, image)