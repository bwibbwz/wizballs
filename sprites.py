#!/usr/bin/env python3

import pygame
import logging as l
from conf import *

class SelectableSprite(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self._selected = False

    def select(self):
        self._selected = True
        self.update()

    def deselect(self):
        self._selected = False
        self.update()

    def is_selected(self):
        return self._selected == True

    def update(self):
        if self.is_selected():
            self.update_selected()
        else:
            self.update_unselected()

    def update_selected(self):
        pass

    def update_unselected(self):
        pass