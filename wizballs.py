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
from groups import Group, CourtTilesGroup, PlayersGroup, SingleSelectableSpriteGroup
all_sprites = pygame.sprite.LayeredUpdates()
court_fields_group = Group()
court_tiles_group = CourtTilesGroup()
players_group = PlayersGroup()
special_effects_group = Group()
players_sssg = SingleSelectableSpriteGroup()
court_sssg = SingleSelectableSpriteGroup()

# Assign Sprites to classes
from court import CourtTile, CourtField
from players import ActivePlayers
from special_effects import Explode
CourtField.groups = all_sprites, court_fields_group
CourtTile.groups = all_sprites, court_tiles_group, court_sssg
ActivePlayers.groups = all_sprites, players_group, players_sssg
Explode.groups = all_sprites, special_effects_group

# Set layer priority
CourtField._layer = BG_L
CourtTile._layer = CT_L
ActivePlayers._layer = AP_L
Explode._layer = SFX_L

# Initialise each group of sprites
from court import init_all_court_fields, init_all_court_tiles
init_all_court_fields()
init_all_court_tiles(court_fields_group.find_by_name('play_court')[0])

from players import init_all_players
init_all_players(court_tiles_group)

i = True

# Main run loop
while i:
    process_events(pygame.event.get(), all_sprites, players_sssg, court_sssg)

    play_surface.fill(CL_BG) 
    
    all_sprites.update()
    all_sprites.draw(play_surface)

    pygame.display.flip()

    time.sleep(0.1)
