#!/usr/bin/env python3

import pygame, sys, logging

# Shorthand for logging
l = logging.getLogger()

def quit_game(quit_code=0):
    l.info('Exit game.')
    pygame.quit()
    sys.exit(quit_code)

