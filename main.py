# Class for the main action of the game.
import pygame
from pygame.locals import *
import random


class View:
    def __init__(self, clock, screen, width, height, FPS):
        self.FPS = FPS
        self.x = 0
        self.clock = clock
        self.screen = screen
        self.width = width
        self.height = height
        pygame.display.set_caption("Tesla Racing Game")
        self.icon = pygame.image.load('graphics/tesla_icon.png')
        pygame.display.set_icon(self.icon)
        self.bkgd = pygame.image.load("graphics/road.png").convert()

    def move_picture(self, tempo):
        rel_x = self.x % self.screen.get_rect().width
        self.screen.blit(self.bkgd, (rel_x - self.screen.get_rect().width, 0))
        if rel_x < self.width:
            self.screen.blit(self.bkgd, (rel_x, 0))
        self.x -= tempo
        self.clock.tick(self.FPS)


class Car:
    def __init__(self, x, y, health):
        self.health = health
        self.carImg = pygame.image.load('graphics/cybertruck.png')
        self.health_font = pygame.font.SysFont("comicsans", 50)
        self.x = x
        self.y = y
        self.mask = pygame.mask.from_surface(self.carImg)

    def draw_car(self, screen):
        screen.blit(self.carImg, (self.x, self.y))

    def get_width(self):
        return self.carImg.get_width()

    def get_height(self):
        return self.carImg.get_height()

    def display_health(self, screen):
        lives_label = self.health_font.render(f"Lives: {self.health}", 1, (255, 255, 255))
        screen.blit(lives_label, (10, 10))


class Vehicle:
    yellow_truck = pygame.image.load('graphics/yellow_truck.png')
    red_truck = pygame.image.load('graphics/red_truck.png')
    fire_truck = pygame.image.load('graphics/fire_truck.png')
    garbagge_collector = pygame.image.load('graphics/garbagge_collector.png')
    types_of_vehicles = [yellow_truck, fire_truck, red_truck, garbagge_collector]

    def __init__(self, x, y, number_type):
        self.obstacle_image = self.types_of_vehicles[number_type].convert_alpha()
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


class Mechanics:
    @staticmethod
    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    @staticmethod
    def display_score(score, screen, width):
        main_font = pygame.font.SysFont("comicsans", 50)
        score_label = main_font.render(f"Score: {score}", 1, (255, 255, 255))
        screen.blit(score_label, (width - score_label.get_width() - 10, 10))

    @staticmethod
    def enemy_generator(vehicles):
        # the line vertically
        # 1
        # 2
        # 3
        tour = [25, 225, 425]
        # the line horizontally
        # 1 2 3 
        collumn = [1300, 1600, 1900]
        # random placed vehicle
        random_vehicle = Vehicle(random.choice(collumn), random.choice(tour), random.randrange(0, 4))
        # vehicles for the grid
        vehicle_a_0 = Vehicle( collumn[0], tour[0], random.randrange(0,4))
        vehicle_a_1 = Vehicle( collumn[1], tour[0], random.randrange(0,4))
        vehicle_a_2 = Vehicle( collumn[2], tour[0], random.randrange(0,4))
        
        vehicle_b_0 = Vehicle( collumn[0], tour[1], random.randrange(0,4))
        vehicle_b_1 = Vehicle( collumn[1], tour[1], random.randrange(0,4))
        vehicle_b_2 = Vehicle( collumn[2], tour[1], random.randrange(0,4))

        vehicle_c_0 = Vehicle( collumn[0], tour[2], random.randrange(0,4))
        vehicle_c_1 = Vehicle( collumn[1], tour[2], random.randrange(0,4))
        vehicle_c_2 = Vehicle( collumn[2], tour[2], random.randrange(0,4))
        
        first_grid = [vehicle_b_0, vehicle_a_2, vehicle_c_2]
        second_grid = [vehicle_a_0, vehicle_c_0, vehicle_b_2]
        third_grid = [vehicle_a_0, vehicle_b_0, vehicle_c_2]
        fourth_grid = [vehicle_a_2, vehicle_b_2, vehicle_c_0]


        # generate random number to choose the wave of enemies
        random_num = random.randint(0, 4) #it does indeed include first and last number!
        # wave of enemies 
        if random_num == 0:
            vehicles += first_grid
            return vehicles
        elif random_num == 1:
            vehicles += second_grid
            return vehicles
        elif random_num == 2:
            vehicles += third_grid
            return vehicles
        elif random_num == 3:
            vehicles += fourth_grid
            return vehicles
        else:
            return vehicles.append(random_vehicle)

        print(f'Wave generated!')

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

def main(window):
    WIDTH, HEIGHT = 1200, 600
    FPS = 120
    running = True
    level = 0
    score = level
    car_vel = 5  # car speed
    bkg_vel = 3
    vehicles = []
    enemy_vel = 3
    effects = []

    current_clock = pygame.time.Clock()

    view = View(current_clock, window, WIDTH, HEIGHT, FPS)
    player = Car(30, 325, 3)

    lost = False
    lost_count = 0

    def redraw_window():
        pygame.font.init()
        view.move_picture(bkg_vel)

        for enemy in vehicles:
            enemy.draw_vehicle(window)

        for effect in effects:
            effect.draw_crash(window)

        player.draw_car(window)
        Mechanics.display_score(level, window, WIDTH)
        player.display_health(window)
        
        if lost:
            game_over(window, level)
        pygame.display.update()

    # Game loop
    while running:
        current_clock.tick(FPS)
        redraw_window()
        if player.health <= 0:
            lost = True
            lost_count += 1

        if lost:
            if lost_count > FPS:
                running = False
                main_menu(window)
            else:
                continue

        if len(vehicles) == 0:
            level += 1

            if level > 10:
                enemy_vel = 10
            else:
                enemy_vel += 1
            if level > 10:
                bkg_vel = 7
            elif level > 5:
                bkg_vel = 4
            else:
                bkg_vel = 3

            Mechanics.enemy_generator(vehicles)
            """
            tour = [25, 225, 425]
            # tour = [580, 400, 290, 170, 0]
            que = [1300, 1800, 2100]
            vehicle = Vehicle(random.choice(que), random.choice(tour), random.randrange(0, 3))
            vehicles.append(vehicle)
            print(f'Enemy generated! level: {level}')
            """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y - car_vel > 0:  # car goes up
            player.y -= car_vel
        if keys[pygame.K_DOWN] and player.y + car_vel + player.get_height() < HEIGHT:  # car goes down
            player.y += car_vel
        if keys[pygame.K_ESCAPE]:
            running = False
            main_menu(window)

        for vehicle in vehicles[:]:
            vehicle.move_obstacle(enemy_vel)
            # print(f'vehicle y {vehicle.y}')
            # print(f'vehicle x {vehicle.x}')
            if Mechanics.collide(vehicle, player):
                player.health -= 1

                pygame.display.flip()
                new_crash = Crash(vehicle.x + 30, vehicle.y)
                effects.append(new_crash)
                pygame.display.flip()
                
                vehicles.remove(vehicle)
                print('Enemy removed by collision')
            elif vehicle.x + vehicle.get_width() < 0:
                vehicles.remove(vehicle)
                # print(f'Enemy removed by vehicle.x {vehicle.x} and get_width(){vehicle.get_width() }')
        # elif vehicle.x
        for effect in effects[:]:

            effect.move_crash(enemy_vel)

            if effect.x + effect.get_width() < 0:
                effects.remove(effect)

def main_menu(screen):
    run = True
    while  run:
        bkgd = pygame.image.load("graphics/game_menu.png")
        title_font = pygame.font.SysFont("comicsans", 80)
        screen.blit(bkgd, (0,0))
        title_label = title_font.render("Press any key to start!",1,(255,255,255))
        screen.blit(title_label,(300, 100) )
        pygame.display.update()
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                main(screen)
    pygame.quit()
        
def game_over(screen, score):
    run = True
    while  run:
        bkgd = pygame.image.load("graphics/game_over.png")
        gameover_font = pygame.font.SysFont("comicsans", 80)
        screen.blit(bkgd, (0,0))
        title_label = gameover_font.render("Game over!",1,(255,255,255))
        new_score_label = gameover_font.render(f"Score {score}",1,(255,255,255))
        screen.blit(title_label,(600, 200) )
        screen.blit(new_score_label,(600, 300))
        pygame.display.update()
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                main_menu(screen)
    pygame.quit()
