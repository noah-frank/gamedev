import pygame
import math
import os
import random

pygame.init()

clock = pygame.time.Clock()
FPS = 60
GRAY = (128, 128, 128)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

ADAM_WIDTH = 75
ADAM_HEIGHT = 75
ADAM_VEL = 4

ROCK_DIMS = [30, 40, 50]

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

#load image
bg = pygame.image.load(os.path.join("Assets", "Background.png")).convert()
bg = pygame.transform.scale(bg, (600, 600))
bg = pygame.transform.rotate(bg, 90)
bg_width = bg.get_width()
bg_height = bg.get_height()
bg_rect = bg.get_rect()

adam_img = pygame.image.load(os.path.join("Assets", "Adam1.png"))
adam_img = pygame.transform.scale(adam_img, (75, 75))
adam_img = pygame.transform.rotate(adam_img, 90)

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_HEIGHT  / bg_height) + 1

def draw_window(screen, scroll, adam, rocks):
    #draw scrolling background
    for i in range(-1, tiles - 1):
        screen.blit(bg, (0, i * bg_height - scroll))
        bg_rect.y = i * bg_height - scroll
        # pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

    for rock in rocks:
        pygame.draw.rect(screen, GRAY, rock)

    screen.blit(adam_img, (adam.x, adam.y))
    pygame.display.update()

def handle_adam_movement(adam, keys_pressed):
    if keys_pressed[pygame.K_w] and adam.y - ADAM_VEL > 0:
        adam.y -= ADAM_VEL
    if keys_pressed[pygame.K_s] and adam.y + ADAM_VEL + adam.height < SCREEN_HEIGHT:
        adam.y += ADAM_VEL
    if keys_pressed[pygame.K_a] and adam.x - ADAM_VEL > 0:
        adam.x -= ADAM_VEL
    if keys_pressed[pygame.K_d] and adam.x + ADAM_VEL + adam.width < SCREEN_WIDTH:
        adam.x += ADAM_VEL

def main():
    adam = pygame.Rect(SCREEN_WIDTH//2 - 75//2, SCREEN_HEIGHT - 150, ADAM_WIDTH, ADAM_HEIGHT)

    rock1 = random.choice(ROCK_DIMS)
    rock2 = random.choice(ROCK_DIMS)
    rock3 = random.choice(ROCK_DIMS)

    rocks = []
        # pygame.Rect(SCREEN_WIDTH//2 - 75//2, 150, rock1, rock1),
        # pygame.Rect(SCREEN_WIDTH//2 - 150, 150, rock2, rock2),
        # pygame.Rect(SCREEN_WIDTH//2 + 150, 150, rock3, rock3)]
    
    scroll = 0
    # tiles = 1 + 1
    run = True
    while run: 
        clock.tick(FPS)

        #scroll background
        scroll -= 3
        #reset scroll
        if abs(scroll) > bg_height:
            scroll = 0

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys_pressed = pygame.key.get_pressed()
        draw_window(screen, scroll, adam, rocks)
        handle_adam_movement(adam, keys_pressed)

        # screen.blit(adam_img, (adam.x, adam.y))
        # pygame.display.update()

if __name__ == "__main__":
    main()