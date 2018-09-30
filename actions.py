""" Class to handle possible actions

    MOVE actions: RIGHT, LEFT, UP, DOWN

"""

import pygame
import random

from conf import *

dr = GRID_SIZE

class WizBallsActions:

    def __init__(self, pos):
        # LOG previous player actions
        self.log = []
        self.pos = pos

    def check_log(self):
        #
        pass

    def update(self, action):
        # Movement
        if action == 'RIGHT':
            self.pos[0] += 1
        elif action == 'LEFT':
            self.pos[0] -= 1
        elif action == 'UP':
            self.pos[1] -= 1
        elif action == 'DOWN':
            self.pos[1] += 1
        # SFX
        elif action == 'EXPLODE':
            pass
