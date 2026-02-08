import pygame
from game.heart import Heart
from game.heartBank import HeartBank
from game.items.cat_collar import CatCollar
from game.items.chocolate import Chocolate
from game.items.diamond_ring import DiamondRing
from game.items.house_key import HouseKey
from game.items.letter import Letter
from game.shop import Shop

#initialization
pygame.init()

WIDTH, HEIGHT = 1820, 1080
#WIDTH, HEIGHT = 2560, 1440
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Valentinstag ❤️")

#####background#####
tile = pygame.image.load("assets/images/heart-background-2.png")
tile_w, tile_h = tile.get_size()

background = pygame.Surface(screen.get_size())
bg_w, bg_h = background.get_size()

for y in range(0, bg_h, tile_h):
    for x in range(0, bg_w, tile_w):
        background.blit(tile, (x, y))
#####################

clock = pygame.time.Clock()
running = True

#objects
heart_image = pygame.image.load("assets/images/heart-sprite.png").convert_alpha()

heart_image = pygame.transform.scale(heart_image,
                                     (heart_image.get_width() * 2,
                                      heart_image.get_height() * 2))

bank_image = pygame.image.load("assets/images/heart-bank.png").convert_alpha()

shop_image = pygame.image.load("assets/images/shop-banner.png").convert_alpha()

cat_image = pygame.image.load("assets/images/cat-collar.png").convert_alpha()

chocolate_image = pygame.image.load("assets/images/chocolate.png").convert_alpha()

ring_image = pygame.image.load("assets/images/diamond-ring.png").convert_alpha()

key_image = pygame.image.load("assets/images/house-key.png").convert_alpha()

letter_image = pygame.image.load("assets/images/letter.png").convert_alpha()

heart = Heart(image=heart_image, position=(WIDTH // 2, HEIGHT // 2.5))

bank = HeartBank(image=bank_image, position=(300, 100))

shop = Shop(image=shop_image, position=(WIDTH // 2, HEIGHT // 1.3))

cat_collar = CatCollar(image=cat_image)

chocolate = Chocolate(image=chocolate_image)

diamond_ring = DiamondRing(image=ring_image)

house_key = HouseKey(image=key_image)

letter = Letter(image=letter_image)

items = [ cat_collar, chocolate, house_key, diamond_ring, letter]

shop.init_items(items)

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
    bank.draw(screen, heart)
    shop.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
