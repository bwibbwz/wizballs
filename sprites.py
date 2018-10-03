#!/usr/bin/env python3

import pygame
import logging as l
from conf import *
from groups import SingleSelectableSpriteGroup

class SelectableSprite(pygame.sprite.Sprite):
    def __init__(self, main_color=CL_ALPHA, selected_color=CL_RED):
        pygame.sprite.Sprite.__init__(self, self.groups)
        self._selected = False
        self._selected_color = selected_color
        self._main_color = main_color
        self._active_color = main_color

    def select(self):
        self._active_color = self._selected_color
        self._selected = True
        for group in self.groups:
            if group.__class__ == SingleSelectableSpriteGroup:
                group.deselect_all_other_sprites(self)
        self.update()

    def deselect(self):
        self._active_color = self._main_color
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
