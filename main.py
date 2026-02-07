import pygame
from game.heart import Heart
from game.heartBank import HeartBank

#initialization
pygame.init()

WIDTH, HEIGHT = 1820, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valentinstag ❤️")

tile = pygame.image.load("assets/images/heart-background-2.png")
tile_w, tile_h = tile.get_size()

background = pygame.Surface(screen.get_size())
bg_w, bg_h = background.get_size()

for y in range(0, bg_h, tile_h):
    for x in range(0, bg_w, tile_w):
        background.blit(tile, (x, y))

clock = pygame.time.Clock()
running = True

#objects
heart_image = pygame.image.load("assets/images/heart-sprite.png").convert_alpha()

heart_image = pygame.transform.scale(heart_image,
                                     (heart_image.get_width() * 2,
                                      heart_image.get_height() * 2))

heart = Heart(
    image=heart_image,
    position=(WIDTH // 2, HEIGHT // 2.5)
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

    screen.blit(background, (0, 0))

    heart.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
