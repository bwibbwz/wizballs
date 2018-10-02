""" Class to handle possible actions

    MOVE actions: RIGHT, LEFT, UP, DOWN

"""

import pygame
import random

from conf import *

actions = {'M': ('LEFT','RIGHT','UP','DOWN')}

class WizBallsActions:

    def __init__(self):
        # LOG previous player actions
        self.log = []
        self.has_moved = False
        self.has_changed = False

    def check_log(self):
        #
        pass

    def update(self, action, pos=None):
        # Movement - need more logical control here
        if action in actions['M'] and pos is None:
            return

        if action == 'RIGHT':
            pos[0] += 1
            self.has_moved = True
        elif action == 'LEFT':
            pos[0] -= 1
            self.has_moved = True
        elif action == 'UP':
            pos[1] -= 1
            self.has_moved = True
        elif action == 'DOWN':
            pos[1] += 1
            self.has_moved = True
        # SFX
        elif action == 'EXPLODE':
            pass

        self.log.append(action)
