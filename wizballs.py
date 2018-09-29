#!/usr/bin/env python3

import pygame, sys, logging, time

# Set up logging
logging.basicConfig(filename = 'wizballs.log', filemode = 'w', level = logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
l = logging.getLogger()

# Import static parameters
from conf import *

# Initialise Pygame
init_error_check = pygame.init()
if init_error_check[1] > 0:
    logging.critical('Pygame initialisation error.')
    sys.exit(-1)
else:
    logging.debug('Pygame succesfully initialised.')

# Set up the game window
playSurface = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption('WizBalls!')

from events_handler import process_events

# Main run loop
while True:
    process_events(pygame.event.get(), l)



