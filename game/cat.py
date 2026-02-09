import pygame
import random

class Cat:

    def __init__(self, walk_frames, idle_frames, shop_rect):
        self.walk_frames = walk_frames
        self.idle_frames = idle_frames
        self.shop_rect = shop_rect

        self.x = shop_rect.centerx
        self.y = shop_rect.top - 75   # place above shop
        self.speed = 120

        self.state = "idle"  # idle | left | right
        self.direction = 1   # 1 right, -1 left

        # animation
        self.frame_index = 0
        self.anim_timer = 0
        self.anim_speed = 0.12

        # decision timer
        self.decision_timer = 0
        self.decision_time = random.uniform(2,4)

        self.active = False

    def activate(self):
        self.active = True

    def decide_next_action(self):
        choice = random.choice(["idle", "left", "right"])
        self.state = choice

        if choice == "left":
            self.direction = -1
        elif choice == "right":
            self.direction = 1

        self.decision_time = random.uniform(2,4)
        self.decision_timer = 0

    def update(self, dt):
        if not self.active:
            return

        # decide new action
        self.decision_timer += dt
        if self.decision_timer >= self.decision_time:
            self.decide_next_action()

        # movement
        if self.state == "left":
            self.x -= self.speed * dt
        elif self.state == "right":
            self.x += self.speed * dt

        # shop boundaries
        if self.x < self.shop_rect.left:
            self.x = self.shop_rect.left
            self.direction = 1
            self.state = "right"

        if self.x > self.shop_rect.right - 80:
            self.x = self.shop_rect.right - 80
            self.direction = -1
            self.state = "left"

        # animation
        self.anim_timer += dt
        if self.anim_timer >= self.anim_speed:
            self.anim_timer = 0
            self.frame_index += 1

    def draw(self, screen):
        if not self.active:
            return

        # choose frame
        if self.state == "idle":
            frames = self.idle_frames
        else:
            frames = self.walk_frames

        frame = frames[self.frame_index % len(frames)]

        # flip if directed left
        if self.direction == -1:
            frame = pygame.transform.flip(frame, True, False)

        screen.blit(frame, (int(self.x), int(self.y)))