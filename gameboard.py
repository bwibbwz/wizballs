#!/usr/bin/env python3

import pygame

# Import static parameters
from conf import *

def draw_gameboard():
    gameSurface = pygame.display.get_surface()
    gameSurface.fill(BG_COLOR)
