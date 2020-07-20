import pygame
from pygame.locals import *


class Vehicle:
    yellow_truck = pygame.image.load('graphics/yellow_truck.png')
    red_truck = pygame.image.load('graphics/red_truck.png')
    fire_truck = pygame.image.load('graphics/fire_truck.png')
    garbagge_collector = pygame.image.load('graphics/garbagge_collector.png')
    types_of_vehicles = [yellow_truck, fire_truck, red_truck, garbagge_collector]

    def __init__(self, x, y, number_type):
        self.obstacle_image = self.types_of_vehicles[number_type] 
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.obstacle_image)

    def draw_vehicle(self, screen):
        screen.blit(self.obstacle_image, (self.x, self.y))

    def move_obstacle(self, vel):
        self.x -= vel

    def get_width(self):
        return self.obstacle_image.get_width()

    def get_height(self):
        return self.obstacle_image.get_height()
