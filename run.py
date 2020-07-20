from game.main import main_menu


if __name__ == "__main__":
    x = 300
    y = 50
    WIDTH, HEIGHT = 1200, 600
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    import pygame
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    main_menu(window)
   