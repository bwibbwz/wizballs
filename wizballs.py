#!/usr/bin/env python3

# Import main libraries
import pygame, sys, logging, time

# Import main subfunctions
from events_handler import process_events

# Import static parameters
from conf import *

# Set up logging
logging.basicConfig(filename = 'wizballs.log', filemode = 'w', level = logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
l = logging.getLogger()

# Initialise Pygame
pygame.init()
pygame.mixer.init()

# Set up the game window
play_surface = pygame.display.set_mode((X_SIZE, Y_SIZE))
pygame.display.set_caption('WizBalls!')

# Initialise the individual sprite groups
from court import init_all_court_fields, init_all_court_tiles
court_fields_group = init_all_court_fields()
court_tiles_group = init_all_court_tiles(court_fields_group.find_by_name('play_court')[0])

from players import init_all_players
player_group = init_all_players()

# Main run loop
while True:
    process_events(pygame.event.get())

    play_surface.fill(CL_BG) 
    
    court_fields_group.draw(play_surface)
    player_group.draw(play_surface)
    court_tiles_group.draw(play_surface)

    pygame.display.flip()





