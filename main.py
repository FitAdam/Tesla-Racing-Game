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
    red_truck = pygame.image.load('graphics/red_truck.png')
    fire_truck = pygame.image.load('graphics/fire_truck.png')
    types_of_vehicles = [yellow_truck, fire_truck, red_truck]

    def __init__(self, x, y, number_type):
        self.obstacle_image = self.types_of_vehicles[number_type]
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.obstacle_image)

    def draw_obstacle(self, screen):
        screen.blit(self.obstacle_image, (self.x, self.y))

    def move_obstacle(self, vel):
        self.x -= vel

    def destroy_obstacle(self):
        pass

    def get_width(self):
        return self.obstacle_image.get_width()

    def get_height(self):
        return self.obstacle_image.get_height()


def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None


def main(window):
    WIDTH, HEIGHT = 1024, 750
    running = True
    level = 0
    car_vel = 5  # car speed
    FPS = 60

    vehicles = []
    test_vehicles = []
    wave_length = 0
    enemy_vel = 3

    current_clock = pygame.time.Clock()

    view = View(current_clock, window, 1024, 750)
    player = Car(30, 325)

    def redraw_window():
        view.move_picture()
        for enemy in vehicles:
            enemy.draw_obstacle(window)

        player.draw_car(window)
        pygame.display.update()

    # Game loop
    while running:
        # current_clock.tick(FPS)
        redraw_window()

        if len(vehicles) == 0:
            level += 1
            wave_length += 1
            for i in range(wave_length):
                # vehicle = Vehicle(1500, 300, 0)

                # tour = [0, 290, 580, 865]
                tour = [580, 400, 290, 170, 0]
                que = [1300, 1700, 2100, 2500]
                vehicle = Vehicle(random.choice(que), random.choice(tour), random.randrange(0, 3))
                vehicles.append(vehicle)

                print(f'Enemy generated! number: {i}')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y - car_vel > 0:  # car goes up
            player.y -= car_vel
        if keys[pygame.K_DOWN] and player.y + car_vel + player.get_height() < 870:  # car goes down
            player.y += car_vel

        for vehicle in vehicles[:]:
            vehicle.move_obstacle(enemy_vel)
            # print(f'vehicle y {vehicle.y}')
            # print(f'vehicle x {vehicle.x}')
            if collide(vehicle, player):
                # player.health -= 10
                vehicles.remove(vehicle)
                # print('Enemy removed by collision')
            elif vehicle.x + vehicle.get_width() < 0:
                # lives -= 1
                vehicles.remove(vehicle)
                # print(f'Enemy removed by vehicle.x {vehicle.x} and get_width(){vehicle.get_width() }')
        # elif vehicle.x
