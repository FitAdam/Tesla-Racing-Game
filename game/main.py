import pygame
from pygame.locals import *
import random
from game.database import DB
from game.view import View
from game.car import Car
from game.vehicle import Vehicle
from game.bonuses import Shield_bonus, Live_bonus
from game.mechanics import Mechanics
from game.crash import Crash
from pygame import mixer



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
    batteries = []
    shields = []
    defenses = []

    current_clock = pygame.time.Clock()

    view = View(current_clock, window, WIDTH, HEIGHT, FPS)
    view.play_music()
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

        for bonus in batteries:
            bonus.draw_bonus(window)

        for shield in shields:
            shield.draw_bonus(window)

        for defense in defenses:
            player.draw_car_shield(window)

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
        # if the number of vehicles is 0 then do:
        if len(vehicles) == 0:
            level += 1

            if level < 10:
                enemy_vel += 1
            elif level > 10 and level < 20:
                enemy_vel = 10
            else:
                enemy_vel = 12

            if level > 10:
                bkg_vel = 7
            elif level > 5:
                bkg_vel = 4
            else:
                bkg_vel = 3

            Mechanics.enemy_generator(vehicles)

        # System of bonuses:
            random_num = random.randint(0, 4)

            if random_num == 0:
                Mechanics.live_generator(batteries)
            if random_num == 1:
                Mechanics.shield_generator(shields)

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
            pygame.display.update()
            
            for defense in defenses[:]:

                if Mechanics.collide(defense, vehicle):
                    vehicle.x += 100
                    new_crash = Crash(vehicle.x + 30, vehicle.y)
                    effects.append(new_crash)
                    vehicles.remove(vehicle)
                    defenses.remove(defense)

            if Mechanics.collide(vehicle, player):
                player.health -= 1

                # pygame.display.flip()
                new_crash = Crash(vehicle.x + 30, vehicle.y)
                new_crash.play_crash_sound()
                effects.append(new_crash)
                # pygame.display.flip()

                vehicles.remove(vehicle)

            elif vehicle.x + vehicle.get_width() < 0:
                vehicles.remove(vehicle)

        for effect in effects[:]:

            effect.move_crash(enemy_vel)

            if effect.x + effect.get_width() < 0:
                effects.remove(effect)

        for bonus in batteries[:]:

            bonus.move_bonus(enemy_vel)

            if Mechanics.collide(bonus, player):
                # This adds life points for player
                Mechanics.collecting()
                bonus.add_live(player)

                # pygame.display.flip()

                batteries.remove(bonus)

            elif bonus.x + bonus.get_width() < 0:
                batteries.remove(bonus)

        for shield in shields[:]:

            shield.move_bonus(enemy_vel)

            if Mechanics.collide(shield, player):

                # pygame.display.flip()
                Mechanics.collecting()
                defense = shield

                defenses.append(defense)

                shields.remove(shield)

            elif shield.x + shield.get_width() < 0:
                shields.remove(shield)

def main_menu(screen):
    mixer.music.load('sounds/menu_music.mp3')
    mixer.music.play(-1)
    run = True
    while  run:
        #pygame.mixer.music.stop()
        
        pygame.display.set_caption("Tesla Racing Game")
        icon = pygame.image.load('graphics/tesla_icon.png')
        pygame.display.set_icon(icon)
        bkgd = pygame.image.load("graphics/game_menu.png")
        title_font = pygame.font.SysFont("Bauhaus 93", 40)
        screen.blit(bkgd, (0,0))
        title_label = title_font.render("Press any key to start...",1,(255,255,255))
        screen.blit(title_label,(350, 500) )
        pygame.display.update()
        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                main(screen)
    pygame.quit()


def game_over(screen, score):
    """
    db = DB()
    db.connect()
    db.add_record(score)
    tablescore = db.get_records()
    db.close_connection()
    """
    mixer.music.load('sounds/menu_music.mp3')
    mixer.music.play(-1)
    run = True
    while  run:
        #pygame.mixer.music.stop()
        
        pygame.display.set_caption("Tesla Racing Game")
        icon = pygame.image.load('graphics/tesla_icon.png')
        pygame.display.set_icon(icon)
        bkgd = pygame.image.load("graphics/game_over.png")
        gameover_font = pygame.font.SysFont("Bauhaus 93", 80)
        screen.blit(bkgd, (0,0))
        #title_label = gameover_font.render("Game over!",1,(255,255,255))
        new_score_label = gameover_font.render(f"Your score is {score}!",1,(255,255,255))
        # TO DO FIX THE TABLE SCORE
        #table_score_label = gameover_font.render(f"Tablescore {tablescore}",1,(255,255,255))
        #screen.blit(title_label,(600, 200) )
        screen.blit(new_score_label,(600, 300))
        #screen.blit(table_score_label,(600, 600))
        pygame.display.update()

        for event in pygame.event.get():
            if  event.type == pygame.QUIT:
                run = False
            if event.type ==pygame.KEYDOWN:
                main_menu(screen)

    pygame.quit()
