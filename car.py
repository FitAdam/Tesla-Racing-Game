import pygame
from pygame.locals import *

class Car:
    def __init__(self, x, y, health):
        self.health = health
        self.carImg = pygame.image.load('graphics/cybertruck.png')
        self.shield_image = pygame.image.load('graphics/shield_activated.png')
        self.health_font = pygame.font.SysFont("comicsans", 50)
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.carImg)

    def draw_car(self, screen):
        screen.blit(self.carImg, (self.x, self.y))

    def draw_car_shield(self, screen):
        screen.blit(self.shield_image, (self.x - 20, self.y - 70))

    def get_width(self):
        return self.carImg.get_width()

    def get_height(self):
        return self.carImg.get_height()

    def display_health(self, screen):
        lives_label = self.health_font.render(f"Lives: {self.health}", 1, (255, 255, 255))
        screen.blit(lives_label, (10, 10))