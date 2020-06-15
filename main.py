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

class Car:
    def __init__(self, x, y):
        self.carImg = pygame.image.load('graphics/cybertruck.png')
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.carImg)
    def draw_car(self, screen):
        screen.blit(self.carImg, (self.x, self.y))

    def get_width(self):
        return self.carImg.get_width()

    def get_height(self):
        return self.carImg.get_width()
        

class Obstacle:
    def __init__(self):
        pass
    def type(self):
        pass
    def disapear(self):
        pass

def main(window):
    car_vel = 5 #car speed
    CLOCK = pygame.time.Clock()
    new_road = Road(CLOCK, window, 1024, 750)
    new_road.load()
    new_car = Car(30, 325)
    
    # Game loop
    running = True
    while running:
        new_road.move_picture()
        new_car.draw_car(window)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and new_car.y - car_vel > 0: #car goes up
            new_car.y -= car_vel
        if keys[pygame.K_DOWN] and new_car.y + car_vel + new_car.get_height() < 870: #car goes down
            new_car.y += car_vel
       

