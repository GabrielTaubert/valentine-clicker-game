import pygame

class FloatingText:

    def __init__(self, text, position, font):
        self.text = text
        self.pos = list(position)
        self.font = font
        self.surface = self.font.render(self.text, True, (148,27,45)).convert_alpha()

        self.lifetime = 1
        self.timer = 0
        self.speed = 40

    def update(self, dt):
        self.timer += dt
        self.pos[1] -= self.speed * dt   # number going up

    def draw(self, screen):
        screen.blit(self.surface, self.pos)

    def is_dead(self):
        if self.timer >= self.lifetime:
            return True
        else:
            return False