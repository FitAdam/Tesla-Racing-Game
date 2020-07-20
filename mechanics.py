import pygame
from pygame.locals import *
from vehicle import Vehicle
from bonuses import Shield_bonus, Live_bonus
import random

class Mechanics:
    @staticmethod
    def collide(obj1, obj2):
        offset_x = obj2.x - obj1.x
        offset_y = obj2.y - obj1.y
        return obj1.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

    @staticmethod
    def display_score(score, screen, width):
        main_font = pygame.font.SysFont("Bauhaus 93", 50)
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
        fiveth_grid = [vehicle_a_1, vehicle_c_1]
        sixth_grid = [vehicle_b_1, vehicle_c_1]
        seven_grid = [vehicle_a_0, vehicle_c_0, vehicle_a_2, vehicle_c_1]
        eighth_grid = [vehicle_a_0, vehicle_c_0, vehicle_a_2, vehicle_c_2]
        nineth_grid =[vehicle_a_1, vehicle_c_2]
        tenth_grid =[vehicle_a_1, vehicle_b_1]


        # generate random number to choose the wave of enemies
        random_num = random.randint(0, 10) #it does indeed include first and last number!
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
        elif random_num == 4:
            vehicles += fiveth_grid
            return vehicles
        elif random_num == 5:
            vehicles += sixth_grid
            return vehicles
        elif random_num == 6:
            vehicles += seven_grid
            return vehicles
        elif random_num == 7:
            vehicles += eighth_grid
            return vehicles
        elif random_num == 8:
            vehicles += nineth_grid
            return vehicles
        elif random_num == 9:
            vehicles += tenth_grid
            return vehicles
        else:
            return vehicles.append(random_vehicle)

    @staticmethod
    def live_generator(perks):
        # the line vertically
        # 1
        # 2
        # 3
        tour = [25, 225, 425]
        # the line horizontally
        # 1 2 3 
        collumn = [1250, 1550, 1850]
        # random placed perk
        random_perk = Live_bonus(random.choice(collumn), random.choice(tour), random.randint(1, 3))
        # slots for the grid
        slot_a_0 = Live_bonus( collumn[0], tour[0], random.randint(1, 2))
        slot_a_1 = Live_bonus( collumn[0], tour[1], random.randint(1, 2))
        slot_a_2 = Live_bonus( collumn[0], tour[2], random.randint(1, 2))
        
        
        random_num = random.randint(0, 4) #it does indeed include first and last number!
        
        if random_num == 0:
            perks.append(slot_a_0)
            return perks
        elif random_num == 1:
            perks.append(slot_a_1)
            return perks
        elif random_num == 2:
            perks.append(slot_a_2)
            return perks
        elif random_num == 3:
            perks.append(slot_a_0)
            perks.append(slot_a_1)
            perks.append(slot_a_2)
        else:
            return perks.append(random_perk)
    @staticmethod
    def shield_generator(perks):
        # the line vertically
        # 1
        # 2
        # 3
        tour = [25, 225, 425]
        # the line horizontally
        # 1 2 3 
        collumn = [1250, 1550, 1850]
        # random placed perk
        random_perk = Shield_bonus(random.choice(collumn), random.choice(tour))
        # slots for the grid
        slot_a_0 = Shield_bonus( collumn[0], tour[0])
        slot_a_1 = Shield_bonus( collumn[0], tour[1])
        slot_a_2 = Shield_bonus( collumn[0], tour[2])
        
        
        random_num = random.randint(0, 4) #it does indeed include first and last number!
        
        if random_num == 0:
            perks.append(slot_a_0)
            return perks
        elif random_num == 1:
            perks.append(slot_a_1)
            return perks
        elif random_num == 2:
            perks.append(slot_a_2)
            return perks
        elif random_num == 3:
            perks.append(slot_a_0)
            perks.append(slot_a_1)
            perks.append(slot_a_2)
        else:
            return perks.append(random_perk)

