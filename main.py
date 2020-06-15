# Class for the main action of the game.
import pygame
from pygame.locals import *
import random

class View:
    def __init__(self, clock, screen, width, height):
        self.FPS = 120
        self.x = 0
        self.clock = clock
        self.screen = screen
        self.width = width
        self.height = height
        pygame.display.set_caption("Tesla Racing Game")
        self.icon = pygame.image.load('graphics/tesla_icon.png')
        pygame.display.set_icon(self.icon)
        self.bkgd = pygame.image.load("graphics/road.png").convert()

    def move_picture(self):
        rel_x = self.x % self.screen.get_rect().width
        self.screen.blit(self.bkgd, (rel_x - self.screen.get_rect().width, 0))
        if rel_x < self.width:
            self.screen.blit(self.bkgd, (rel_x, 0))
        self.x -= 1
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


class Vehicle:
    yellow_truck = pygame.image.load('graphics/yellow_truck.png')
    dhl_truck = pygame.image.load('graphics/dhl.png')
    prius = pygame.image.load('graphics/prius.png')
    types_of_vehicles = [yellow_truck, dhl_truck, prius]

    def __init__(self, x, y, type):
        self.obstacle_image = self.types_of_vehicles[type]
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.obstacle_image)

    def draw_obstacle(self, screen):
        screen.blit(self.obstacle_image, (self.x, self.y))

    def move_obstacle(self, vel):
        self.x -= vel

    def destroy_obstacle(self):
        pass


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

def main(window):
    level = 0
    car_vel = 5  # car speed
    enemies = []
    wave_length = 5
    enemy_vel = 1
    CLOCK = pygame.time.Clock()
    view = View(CLOCK, window, 1024, 750)
    player = Car(30, 325)
    yellow_truck = Vehicle(1300, 120, 0)
   #dhl = Vehicle(1300, 325, 1)
    prius = Vehicle(1300, 600, 2)

    for enemy in enemies:
        yellow_truck.draw_obstacle(window)

    # Game loop
    running = True
    while running:
        view.move_picture()
        player.draw_car(window)
        yellow_truck.draw_obstacle(window)
        yellow_truck.move_obstacle(3)
        #dhl.draw_obstacle(window)
        #dhl.move_obstacle(4)
        prius.draw_obstacle(window)
        prius.move_obstacle(2)

        pygame.display.update()
        if len(enemies) == 0:
            level += 1
            wave_length += 5
            for i in range(wave_length):
                enemy = Vehicle(random.randrange(50, 1024 -100), random.randrange(-1500, -100), random.choice(range(0,1)))
                enemies.append(enemy)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y - car_vel > 0:  # car goes up
            player.y -= car_vel
        if keys[pygame.K_DOWN] and player.y + car_vel + player.get_height() < 870:  # car goes down
            player.y += car_vel

        if collide(enemy, player):
            enemy.x += 150
      #      enemies.remove(yellow_truck)
      #  elif enemy.y + enemy.get_height() > HEIGHT:
       #     lives -= 1
       #     enemies.remove(enemy)