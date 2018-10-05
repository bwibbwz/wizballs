#!/usr/bin/env python3

import pygame, sys, math
import logging as l
from conf import *

def load_image(name, rect):
    image = pygame.image.load(name).convert()
    image = pygame.transform.scale(image, (rect.size))
    return image

def quit_game(quit_code=0):
    l.info('Exit game.')
    pygame.quit()
    sys.exit(quit_code)

def calculate_conf_parameters(tol=0.05):
    from conf import X_SIZE, X_TILES, COURT_RATIO, GRID_PADDING

    GRID_SIZE_FLOAT = X_SIZE / (X_TILES * (1 + GRID_PADDING) + GRID_PADDING)
    GRID_SIZE = round(GRID_SIZE_FLOAT)
    
    # Make sure GRID_SIZE_FLOAT is close (controlled by tol) to an ineger value divisible by 2, by varying X_SIZE
    while abs(GRID_SIZE_FLOAT - GRID_SIZE) > tol or GRID_SIZE % 2 != 0:
        X_SIZE += 1
        GRID_SIZE_FLOAT = X_SIZE / (X_TILES * (1 + GRID_PADDING) + GRID_PADDING)
        GRID_SIZE = round(GRID_SIZE_FLOAT)
        #print(X_SIZE, GRID_SIZE, GRID_SIZE_FLOAT, GRID_SIZE_FLOAT - GRID_SIZE)

    #print("-- -- -- -- -- -- -- --")
    print('X_SIZE = %i' % X_SIZE)
    print('GRID_SIZE = %i' % GRID_SIZE)

    from conf import Y_TILES, COURT_RATIO
    Y_COURT_SIZE = round(GRID_SIZE * (Y_TILES * (1 + GRID_PADDING) + GRID_PADDING))
    Y_SCORE_SIZE = round(Y_COURT_SIZE * (1 - COURT_RATIO))
    Y_SIZE = Y_COURT_SIZE + Y_SCORE_SIZE

    print('Y_COURT_SIZE = %i' % Y_COURT_SIZE)
    print('Y_SCORE_SIZE = %i' % Y_SCORE_SIZE)
    print('Y_SIZE = %i' % Y_SIZE)
