# Class for the main action of the game.
import pygame
from pygame.locals import *

class Car:
    def __init__(self):
        pass
    def go_down(self):
        pass
    def go_up(self):
        pass

class Obstacle:
    def __init__(self):
        pass
    def type(self):
        pass
    def disapear(self):
        pass

class Road:
    def __init__(self):
        pass
    def change(self):
        pass

## to do scrolling background image


def main():
    width = 800
    height = 600
    
    pygame.init()
    CLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Tesla Racing Game")
    icon = pygame.image.load('graphics/tesla_icon.png')
    pygame.display.set_icon(icon)
    FPS = 120
    bkgd = pygame.image.load("graphics/road.png").convert()
    x = 0

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(bkgd,(x,0))

        pygame.display.update()
        CLOCK.tick(FPS)

main()