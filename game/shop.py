"""
the shop shows every item which can be bought.

checks if item can be pruchased.

after buy will upgrade heart or else.

mark item as bought.
"""

class Shop:

    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.items = []
        self.spacing = 20 #space between items

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        for item in self.items:
            item.draw(screen)

    def init_items(self, items: list):
        self.items = items

        # starting position
        x = self.rect.left + 80
        y = self.rect.centery

        for item in items:
            item.set_position(x, y)
            x += item.rect.width + self.spacing

    def check_item_buyable(self, item, bank):
        pass

    def buy_item(self, item, bank):
        pass