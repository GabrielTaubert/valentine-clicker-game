import pygame
from game.heart import Heart
from game.heartBank import HeartBank

#initialization
pygame.init()

WIDTH, HEIGHT = 1820, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valentinstag ❤️")

clock = pygame.time.Clock()
running = True

#objects
heart_image = pygame.image.load("assets/images/heart-sprite.png").convert_alpha()

heart = Heart(
    image=heart_image,
    position=(WIDTH // 2, HEIGHT // 2)
)

bank = HeartBank()

#game
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        gained_hearts = heart.handle_event(event)
        if gained_hearts > 0:
            bank.addHearts(gained_hearts)

    screen.fill((255, 230, 240))
    heart.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
