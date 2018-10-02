#!/usr/bin/env python3

# Import main libraries
import pygame, sys, time
import logging as l

# Import main subfunctions
from events_handler import process_events

# Import static parameters
from conf import *

# Set up logging
l.basicConfig(filename = 'wizballs.log', filemode = 'w', level = l.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')

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
command_tiles_group = Group()
players_group = PlayersGroup()

# Assign Sprites to classes
from court import CourtTile, CourtField, CommandTile
from players import ActivePlayers
CourtField.groups = all_sprites, court_fields_group
CourtTile.groups = all_sprites, court_tiles_group
CommandTile.groups = all_sprites, command_tiles_group
ActivePlayers.groups = all_sprites, players_group

# Set layer priority
CourtField._layer = 1
CourtTile._layer = 2
CommandTile._layer = 3
ActivePlayers._layer = 4

# Initialise each group of sprites
from court import init_all_court_fields, init_all_court_tiles, init_all_command_tiles
init_all_court_fields()
init_all_court_tiles(court_fields_group.find_by_name('play_court')[0])
init_all_command_tiles(court_fields_group.find_by_name('score_board')[0])

from players import init_all_players
init_all_players(court_tiles_group)

i = True

# Main run loop
while i:
    process_events(pygame.event.get(), players_group)

    play_surface.fill(CL_BG) 
    
    players_group.update_render()
    #players_group.update()

    #all_sprites.update()
    all_sprites.draw(play_surface)

    pygame.display.flip()

    #time.sleep(2.0)
