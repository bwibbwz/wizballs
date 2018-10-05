#!/usr/bin/env python3

import pygame, sys
import logging as l
from conf import *

def draw_border(image, color=CL_BLACK, dimensions=(0, 0, GRID_SIZE - 1, GRID_SIZE - 1), thickness=2):
    pygame.draw.rect(image, color, dimensions, thickness)

def copy_color(color, alpha=None):
    if alpha:
        return pygame.Color(color.r, color.g, color.b, alpha)
    else:
        return pygame.Color(color.r, color.g, color.b, color.a)
        
def average_color(image):
    pixels = [0, 0, 0]
    for k in range(image.get_rect().w):
        for j in range(image.get_rect().h):
            color = image.get_at((k, j))
            pixels[0] += color.r
            pixels[1] += color.g
            pixels[2] += color.b
    avg_color = pygame.Color(round(pixels[0]/k/j), round(pixels[1]/k/j), round(pixels[2]/k/j), 255)
    return avg_color
        
