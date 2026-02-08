"""
the heart ist the main component of the game.

it should be clickable, by clicking generate hearts.

amount of generated hearts should be upgradeable.

maybe an animation would be nice.
"""

import pygame
import random

from game.floating_text import FloatingText


class Heart:

    def __init__(self, image, position):
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect(center=position)
        self.hearts_per_click = 1
        self.automatic_hearts_per_second = 0

        self.is_pressed = False
        self.press_timer = 0
        self.press_duration = 0.1

        self.floating_numbers = []

        self.font = pygame.font.Font("assets/font/Minecraft.ttf", 50)
        self.number_font = pygame.font.Font("assets/font/Minecraft.ttf", 30)

    def upgrade_hearts_per_click(self, amount):
        self.hearts_per_click += amount

    def upgrade_automatic_hearts_per_second(self, amount):
        self.automatic_hearts_per_second += amount

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        for ft in self.floating_numbers:
            ft.draw(screen)

    def create_floating_number(self):

        offset_x = random.randint(-300, 300)
        offset_y = random.randint(-300, 300)

        position = (
            self.rect.centerx + offset_x,
            self.rect.centery + offset_y
        )

        floating_number = FloatingText(f"+{self.hearts_per_click}", position, self.number_font )

        self.floating_numbers.append(floating_number)

    def shrink(self):
        self.is_pressed = True
        #self.press_timer = 0

        scale = 0.85  # 85% Größe
        w = int(self.original_image.get_width() * scale)
        h = int(self.original_image.get_height() * scale)

        self.image = pygame.transform.scale(self.original_image, (w, h))
        center = self.rect.center
        self.rect = self.image.get_rect(center=center)

    def update(self, dt):
        if self.is_pressed:
            self.press_timer += dt

            if self.press_timer >= self.press_duration:
                self.image = self.original_image
                center = self.rect.center
                self.rect = self.image.get_rect(center=center)
                self.is_pressed = False

        for ft in self.floating_numbers:
            ft.update(dt)
            if ft.is_dead():
                self.floating_numbers.remove(ft)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # linke Maustaste
                if self.rect.collidepoint(event.pos):
                    self.shrink()
                    self.create_floating_number()
                    return self.hearts_per_click
        return 0