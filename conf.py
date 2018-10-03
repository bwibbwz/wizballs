#!/usr/bin/env python3

import pygame
import math

# SIZE OF PLAY AREA
X_SIZE = 1079
COURT_RATIO = 0.7

# AMOUNT OF TILES
X_TILES = 15
Y_TILES = 7

# PADDING
GRID_PADDING = 0.1

# CALCULATE THE GRID_SIZE
GRID_SIZE = round(X_SIZE / (X_TILES * (1 + GRID_PADDING) + (GRID_PADDING)))

# ITERATE TO FIND CORRECT X_SIZE
#GS = X_SIZE / (X_TILES * (1 + GRID_PADDING) + (GRID_PADDING))
#GRID_SIZE = round(GS)
#while abs(GRID_SIZE - GS) > 0.05:
#    X_SIZE += 1
#    GS = X_SIZE / (X_TILES * (1 + GRID_PADDING) + (GRID_PADDING))
#    GRID_SIZE = round(GS)
#print('Optimal X_SIZE: ', X_SIZE)

# SET Y_SIZEs
Y_COURT_SIZE = round(GRID_SIZE * (Y_TILES * (1 + GRID_PADDING) + GRID_PADDING))
Y_SCORE_SIZE = round(Y_COURT_SIZE * (1 - COURT_RATIO))
Y_SIZE = Y_COURT_SIZE + Y_SCORE_SIZE

# SET OPACITIES
BG_COURT_OPACITY = 200
COURT_TILE_OPACITY = 50
BASKET_TILE_OPACITY = 150

# COLOURS
CL_BG    = pygame.Color(255, 255, 255)
CL_COURT = pygame.Color(218, 173, 124) # For image 'img/wood-floor-tileable.jpg'
CL_TILES = pygame.Color(155, 83, 50)
CL_SCORE = pygame.Color(80, 80, 80)
CL_RED   = pygame.Color(255, 0, 0)
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
