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
    def __init__(self, clock):
        self.FPS = 120
        self.x = 0
        self.width = 800
        self.height = 586
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = clock

    def load(self):
        pygame.display.set_caption("Tesla Racing Game")
        self.icon = pygame.image.load('graphics/tesla_icon.png')
        pygame.display.set_icon(self.icon)
        self.bkgd = pygame.image.load("graphics/road.png").convert()

    def move_picture(self):
        rel_x = self.x % self.screen.get_rect().width
        self.screen.blit(self.bkgd,(rel_x - self.screen.get_rect().width,0))
        if rel_x < self.width:
            self.screen.blit(self.bkgd,(rel_x,0))
        self.x-=1
        pygame.display.update()
        self.clock.tick(self.FPS)

## to do scrolling background image


def main():
    pygame.init()
    CLOCK = pygame.time.Clock()
    new_road = Road(CLOCK)
    new_road.load()
    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        new_road.move_picture()
        

main()