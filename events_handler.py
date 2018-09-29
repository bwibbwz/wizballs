#!/usr/bin/env python3

import pygame, logging
from basic_functions import quit_game

# Set up shorthand for logging
l = logging.getLogger()

def process_events(events):
    for event in events:
        l.debug(event)
        if event.type == pygame.QUIT:
            l.info('User quit the game.')
            quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                l.info('Key pressed: RIGHT')
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                l.info('Key pressed: LEFT')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                l.info('Key pressed: DOWN')
            if event.key == pygame.K_UP or event.key == ord('w'):
                l.info('Key pressed: UP')
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                l.info('Key pressed: ESCAPE')

