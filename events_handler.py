#!/usr/bin/env python3

import pygame, logging
from basic_functions import quit_game

# Set up shorthand for logging
l = logging.getLogger()

def process_events(events, player_group):
    for event in events:
        l.debug(event)
        if event.type == pygame.QUIT:
            l.info('User quit the game.')
            quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                l.info('Key pressed: RIGHT')
                sprite = [s for s in player_group if s.selected]
                sprite[0].update('RIGHT')
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                l.info('Key pressed: LEFT')
                sprite = [s for s in player_group if s.selected]
                sprite[0].update('LEFT')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                l.info('Key pressed: DOWN')
                sprite = [s for s in player_group if s.selected]
                sprite[0].update('DOWN')
            if event.key == pygame.K_UP or event.key == ord('w'):
                l.info('Key pressed: UP')
                sprite = [s for s in player_group if s.selected]
                sprite[0].update('UP')
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                l.info('Key pressed: ESCAPE')
        elif event.type == pygame.MOUSEBUTTONUP:
            l.info('Mouse button pressed')
            pos = pygame.mouse.get_pos()
            clicked_sprite = [s for s in player_group 
                              if s.rect.collidepoint(pos)]
            not_clicked_sprite = [s for s in player_group
                                  if not s.rect.collidepoint(pos)]

            if clicked_sprite:            
                clicked_sprite[0].selected = True
            for s in not_clicked_sprite:
                s.selected = False
            
