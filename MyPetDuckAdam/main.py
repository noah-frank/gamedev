import pygame
import math
import os

pygame.init()

clock = pygame.time.Clock()
FPS = 60

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

#create game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Endless Scroll")

#load image
bg = pygame.image.load(os.path.join("Assets", "Background.png")).convert()
bg = pygame.transform.scale(bg, (1200, 600))
bg_width = bg.get_width()
bg_rect = bg.get_rect()

adam = pygame.image.load(os.path.join("Assets", "Adam1.png"))
adam = pygame.transform.scale(adam, (75, 75))

#define game variables
scroll = 0
tiles = math.ceil(SCREEN_WIDTH  / bg_width) + 1


def main():
    scroll = 0
    tiles = 1 + 1
    run = True
    while run: 
        clock.tick(FPS)

        #draw scrolling background
        for i in range(0, tiles):
            screen.blit(bg, (i * bg_width + scroll, 0))
            bg_rect.x = i * bg_width + scroll
            # pygame.draw.rect(screen, (255, 0, 0), bg_rect, 1)

        #scroll background
        scroll -= 3

        #reset scroll
        if abs(scroll) > bg_width:
            scroll = 0

        #event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        screen.blit(adam, (100, SCREEN_HEIGHT//2 - 75//2))
        pygame.display.update()

if __name__ == "__main__":
    main()