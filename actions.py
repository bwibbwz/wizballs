""" Class to handle possible actions

"""

import pygame
import random

from conf import *

from controls import Direction

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
        # Movement - need more logical ctrl here
        if action in ACTIONS['M'] and pos is None:
            pass

        if action.__class__ == Direction:
            try:
                pos.move(action)
                self.has_moved = True
            except Exception as err:
                pass
        # SFX
        elif action == 'EXPLODE':
            # A) need to 'kill' sprite
            # B) need to spawn Fragment sprites
            self.has_changed = True

        elif action == 'VIBRATE':
            pass

        #spassg.append(action)
