#!/usr/bin/env python3

import pygame
import logging as l
from conf import *
#from groups import Group, CourtTilesGroup
#from sprites import SelectableSprite, HighlightableSprite
#from graphics_functions import draw_border, copy_color

class Direction():
    directions = {'RIGHT': (1, 0),
                  'LEFT':  (-1, 0),
                  'UP':    (0, -1),
                  'DOWN':  (0, 1)}

    def __init__(self, name):
        self._name = name
        self._x = self.directions[name][0]
        self._y = self.directions[name][1]
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def dir(self):
        return self.x, self.y
    
    @property
    def name(self):
        return self._name
            
    def __getitem__(self, key):
        if key == 0:
            return self.x
        elif key == 1:
            return self.y
        else:
            raise IndexError('There are only 2 values possible, 0 and 1 (%i was given)' % key)

    def __str__(self):
        return self.name

right = Direction('RIGHT')
left  = Direction('LEFT')
up    = Direction('UP')
down  = Direction('DOWN')

