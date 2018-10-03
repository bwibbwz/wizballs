#!/usr/bin/env python3

import pygame, sys
import logging as l
from conf import *

def draw_border(image, color=CL_BLACK, dimensions=(0, 0, GRID_SIZE - 1, GRID_SIZE - 1), thickness=2):
    pygame.draw.rect(image, color, dimensions, thickness)

def copy_color(color):
    return pygame.Color(color.r, color.g, color.b, color.a)
