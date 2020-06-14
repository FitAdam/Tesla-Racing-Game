# Class for the main action of the game.
import pygame
from pygame.locals import *

pygame.init()

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tesla Racing Game")
icon = pygame.image.load('graphics/tesla_icon.png')
pygame.display.set_icon(icon)
# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False