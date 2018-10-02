#!/usr/bin/env python3

X_SIZE = 1000
Y_SIZE = 720
GRID_SIZE = 20
COURT_RATIO = 0.7

X_TILES = 20
Y_TILES = 10

# COLOURS
CL_BG = [255, 255, 255]
CL_COURT = [205, 133, 0]
CL_TILES = [155, 83, 50]
CL_SCORE = [80, 80, 80]
CL_RED = [255, 0, 0]

# SKIN-TONES / TAG
CL_STONE = {}
CL_STONE[0] = [(234, 192, 134), 'C'] # cauc-brown
CL_STONE[1] = [(255, 224, 189), 'C'] # cauc-pink
CL_STONE[2] = [(255, 173, 96), 'C']  # cauc-orange
CL_STONE[3] = [(156, 114, 72), 'A']  # afram-lbrown
CL_STONE[4] = [(135, 97, 39), 'A']   # afram-mbrown
CL_STONE[5] = [(111, 79, 29), 'A']   # afram-dbrown

# WIZ-TONES
CL_WTONE = {}
CL_WTONE[0] = (255, 0, 255)  # wiz-magenta
CL_WTONE[1] = (138, 43, 226) # wiz-violet
CL_WTONE[2] = (75, 0, 130)   # wiz-indigo

# Physics
FORCE_OF_GRAVITY = 9.81 # 9.81 pixels / s^2

# TEAMS
T_SIZE = 2
W_SIZE = 1

# ACTIONS
ACTIONS = {}
ACTIONS['M'] = ('RIGHT','LEFT','UP','DOWN')
