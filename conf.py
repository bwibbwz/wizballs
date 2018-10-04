#!/usr/bin/env python3

import pygame

# AMOUNT OF COURT TILES
X_TILES = 15
Y_TILES = 7

# VARIOUS PLAY AREA FACTORS
GRID_PADDING = 0.1
COURT_RATIO = 0.7

# CALUCULATED VALUES (python3 -c "import basic_functions; basic_functions.calculate_conf_parameters()")
X_SIZE = 1095
GRID_SIZE = 66
Y_COURT_SIZE = 515
Y_SCORE_SIZE = 155
Y_SIZE = 670

# SET OPACITIES
BG_COURT_OPACITY = 150
COURT_TILE_OPACITY = 50
BASKET_TILE_OPACITY = 150

# COLOURS
CL_BG    = pygame.Color(255, 255, 255)
CL_COURT = pygame.Color(218, 173, 124) # For image 'img/wood-floor-tileable.jpg'
CL_TILES = pygame.Color(155, 83, 50)
CL_SCORE = pygame.Color(80, 80, 80)
CL_RED   = pygame.Color(255, 0, 0)
CL_BLUE  = pygame.Color(0, 0, 255)
CL_ALPHA = pygame.Color(0, 0, 0, 0)
CL_BLACK = pygame.Color(0, 0, 0)

# SKIN-TONES / TAG
CL_STONE = {}
CL_STONE[0] = [pygame.Color(234, 192, 134), 'C'] # cauc-brown
CL_STONE[1] = [pygame.Color(255, 224, 189), 'C'] # cauc-pink
CL_STONE[2] = [pygame.Color(255, 173, 96), 'C']  # cauc-orange
CL_STONE[3] = [pygame.Color(156, 114, 72), 'A']  # afram-lbrown
CL_STONE[4] = [pygame.Color(135, 97, 39), 'A']   # afram-mbrown
CL_STONE[5] = [pygame.Color(111, 79, 29), 'A']   # afram-dbrown

# WIZ-TONES
CL_WTONE = {}
CL_WTONE[0] = pygame.Color(255, 0, 255)  # wiz-magenta
CL_WTONE[1] = pygame.Color(138, 43, 226) # wiz-violet
CL_WTONE[2] = pygame.Color(75, 0, 130)   # wiz-indigo

# Physics
FORCE_OF_GRAVITY = 9.81 # 9.81 pixels / s^2

# TEAMS
T_SIZE = 2
W_SIZE = 1

# ACTIONS
ACTIONS = {}
ACTIONS['M'] = ('RIGHT','LEFT','UP','DOWN')

# LAYERS
BG_L  = 1 # Background
CT_L  = 2 # Court tiles
CMD_L = 3 # Command tiles
AP_L  = 4 # Active players
SFX_L = 5 # Special effects
