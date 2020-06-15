from main import main


if __name__ == "__main__":
    x = 300
    y = 50
    import os
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x,y)
    import pygame
    window = pygame.display.set_mode((1024, 750))
    main(window)