#!/usr/bin/env python3

import pygame, sys, logging

# Set up logging
logging.basicConfig(filename = 'wizballs.log', filemode = 'w', level = logging.DEBUG, format='%(asctime)s %(levelname)s: %(message)s')
l = logging.getLogger()

# Import static parameters
from wizballs_conf import X_SIZE, Y_SIZE, GRID_SIZE

