#!/usr/bin/env python3

# Import main libraries
import pygame, sys, logging, time

# Import main subfunctions
from events_handler import process_events
from gameboard import draw_gameboard

# Import static parameters
from conf import *

# Set up logging
logging.basicConfig(filename = 'wizballs.log', filemode = 'w', level = logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
l = logging.getLogger()

# Initialise Pygame
init_error_check = pygame.init()
if init_error_check[1] > 0:
    l.critical('Pygame initialisation error.')
    sys.exit(-1)
else:
    l.debug('Pygame succesfully initialised.')

# Set up the game window
pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption('WizBalls!')

# Main run loop
while True:
    process_events(pygame.event.get())
    draw_gameboard()
    
    pygame.display.flip()





