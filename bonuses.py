import pygame
from pygame.locals import *



class Live_bonus:
    def __init__(self, x, y, live_premium):
        self.bonus_image = pygame.image.load('graphics/battery.png').convert_alpha()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.bonus_image)
        self.live_premium = 1

    def draw_bonus(self, screen):
        screen.blit(self.bonus_image, (self.x, self.y))

    def move_bonus(self, vel):
        self.x -= vel

    def get_width(self):
        return self.bonus_image.get_width()

    def get_height(self):
        return self.bonus_image.get_height()
    # adds live points for player
    def add_live(self, obj1):
        obj1.health += self.live_premium 

class Shield_bonus:
    def __init__(self, x, y):
        self.bonus_image = pygame.image.load('graphics/shield.png').convert_alpha()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.bonus_image)

    def draw_bonus(self, screen):
        screen.blit(self.bonus_image, (self.x, self.y))

    def move_bonus(self, vel):
        self.x -= vel

    def get_width(self):
        return self.bonus_image.get_width()

    def get_height(self):
        return self.bonus_image.get_height()
 