import pygame
from pygame.locals import *
from pygame import mixer
import random

class Crash:
    def __init__(self, x, y):
        self.crash_image = pygame.image.load('graphics/boom_yellow.png').convert_alpha()
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.crash_image)
        
    def draw_crash(self, screen):
        screen.blit(self.crash_image, (self.x, self.y))

    def move_crash(self, vel):
        self.x -= vel

    def get_width(self):
        return self.crash_image.get_width()

    def play_crash_sound(self):

        first_crash = mixer.Sound('sounds/Explosion1.wav')
        second_crash = mixer.Sound('sounds/Explosion2.wav')
        
        random_num = random.randint(1, 2)

        if random_num == 1:
            first_crash.play()
        else:
            second_crash.play()