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

# Create the Sprite groups
from groups import Group, CourtTilesGroup, PlayersGroup
all_sprites = pygame.sprite.LayeredUpdates()
court_fields_group = Group()
court_tiles_group = CourtTilesGroup()
players_group = PlayersGroup()

# Assign Sprites to classes
from court import CourtTile, CourtField
from players import ActivePlayers
CourtField.groups = all_sprites, court_fields_group
CourtTile.groups = all_sprites, court_tiles_group
ActivePlayers.groups = all_sprites, players_group

# Set layer priority
CourtField._layer = 1
CourtTile._layer = 2
ActivePlayers._layer = 3

# Initialise each group of sprites
from court import init_all_court_fields, init_all_court_tiles
init_all_court_fields()
init_all_court_tiles(court_fields_group.find_by_name('play_court')[0])

from players import init_all_players
init_all_players(court_tiles_group)

i = True

# Main run loop
while i:
    process_events(pygame.event.get(), players_group)

    play_surface.fill(CL_BG) 
    
    players_group.update_render()
    players_group.update('RIGHT')

    #all_sprites.update()
    all_sprites.draw(play_surface)

    pygame.display.flip()
    time.sleep(0.1)
