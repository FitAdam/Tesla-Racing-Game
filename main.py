# Class for the main action of the game.
import pygame
from pygame.locals import *


class Road:
    def __init__(self, clock, screen, width, height ):
        self.FPS = 120
        self.x = 0
        self.clock = clock
        self.screen = screen
        self.width = width
        self.height = height

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
        self.clock.tick(self.FPS)

class Car():
    def __init__(self):
        self.height = 100
        self.width = 100
        self.carImg = pygame.image.load('graphics/cybertruck.png')
    def move_car(self, screen, x, y):
        screen.blit(self.carImg, (x,y))
    # TODO car postioning (3 levels)
    def car_position(self):
        pass
class Obstacle:
    def __init__(self):
        pass
    def type(self):
        pass
    def disapear(self):
        pass
    
def main(window):
    pygame.init()
    CLOCK = pygame.time.Clock()
    new_road = Road(CLOCK, window, 1024, 750)
    new_road.load()
    new_car = Car()
    x =  30
    y = 30
    y_change = 0
    car_speed = 0

    # Game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_change = +5
                if event.key == pygame.K_UP:
                    y_change = -5
        y += y_change
        new_road.move_picture()
        new_car.move_car(window,x, y)
        
        
        pygame.display.update()
       


