"""
third consumable item

add's a cat above the shop bar, which walks around it
"""
from game.item import Item


class CatCollar(Item):

    def __init__(self, image):
        Item.__init__(self, image)
        self.price = 400
        self.name = "Cat Collar"

    def apply_effect(self, base_dict):
        cat = base_dict.get("cat")
        if cat:
            cat.activate()