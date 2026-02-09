"""
last consumable item

opens the last message, player wins and get invitation to a date
"""
import pygame

from game.item import Item


class Letter(Item):

    def __init__(self, image, msg_position):
        Item.__init__(self, image)
        self.price = 1000
        self.name = "Letter"
        self.msg_image = pygame.image.load("assets/images/message-box.png")
        self.msg_image = pygame.transform.scale(self.msg_image,
                                             (self.msg_image.get_width() * 1.5,
                                              self.msg_image.get_height() * 1.5))
        self.msg_rect = self.msg_image.get_rect(center=msg_position)
        self.is_opened = False

    def apply_effect(self, base_dict):
        self.is_opened = True

    def draw_message(self, screen):
        if self.is_opened:
            screen.blit(self.msg_image, self.msg_rect)

            font = pygame.font.Font("assets/font/Minecraft.ttf", 60)
            small_font = pygame.font.Font("assets/font/Minecraft.ttf", 28)

            color = (148, 27, 45)

            title = font.render("You did it!", True, color)
            subtitle = font.render("You are my Valentine date! <3", True, color)
            date = small_font.render("14 February 2026", True, color)

            center_x = self.msg_rect.centerx
            center_y = self.msg_rect.centery

            title_rect = title.get_rect(center=(center_x, center_y - 60))
            subtitle_rect = subtitle.get_rect(center=(center_x, center_y))
            date_rect = date.get_rect(center=(center_x, center_y + 70))

            screen.blit(title, title_rect)
            screen.blit(subtitle, subtitle_rect)
            screen.blit(date, date_rect)

