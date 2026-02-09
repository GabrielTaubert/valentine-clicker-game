"""
the shop shows every item which can be bought.

checks if item can be pruchased.

after buy will upgrade heart or else.

mark item as bought.
"""

import pygame

class Shop:

    def __init__(self, image, position):
        self.image = image
        self.rect = self.image.get_rect(center=position)
        self.items = []
        self.spacing = 20 #space between items
        self.font = pygame.font.Font("assets/font/Minecraft.ttf", 50)

    def draw(self, screen, bank):
        screen.blit(self.image, self.rect)

        text = self.font.render("Shop", True, (148, 27, 45))

        text_x = self.rect.left + 30
        text_y = self.rect.centery - 20

        screen.blit(text, (text_x, text_y))

        for item in self.items:
            is_buyable = self.check_item_buyable(item, bank)
            item.draw(screen, is_buyable)

    def init_items(self, items: list):
        self.items = items

        # starting position
        x = self.rect.left + 230
        y = self.rect.centery

        for item in items:
            item.set_position((x, y))
            x += item.rect.width + self.spacing

    def handle_click(self, mouse_pos, bank, base_dict):
        for item in self.items:

            if item.rect.collidepoint(mouse_pos):

                if item.is_bought:
                    return

                if self.check_item_buyable(item, bank):
                    self.buy_item(item, bank, base_dict)

    def check_item_buyable(self, item, bank):
        if bank.hearts >= item.price:
            return True
        else:
            return False

    def buy_item(self, item, bank, base_dict):
        bank.hearts -= item.price
        item.buy(base_dict)