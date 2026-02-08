"""
items are consumables in the game.

this is just the basis/parent class.

vars like price, name, image are standard

every item can just be pruchased once.

after the buy of a item, a costum message should appear.
"""

class Item:

    def __init__(self, image):
        self.price = 0
        self.name = ""
        self.image = image
        self.rect = self.image.get_rect()
        self.is_bought = False

    def set_position(self, position):
        self.rect.center = position

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def buy(self):
        self.is_bought = True

    def message(self):
        pass