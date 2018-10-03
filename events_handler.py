#!/usr/bin/env python3

import pygame
import logging as l
from basic_functions import quit_game

def process_events(events, player_group, all_sprites, court_group):
    for event in events:
        l.debug(event)
        if event.type == pygame.QUIT:
            l.info('User quit the game.')
            quit_game()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                l.info('Key pressed: RIGHT')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update('RIGHT')
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                l.info('Key pressed: LEFT')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update('LEFT')
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                l.info('Key pressed: DOWN')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update('DOWN')
            if event.key == pygame.K_UP or event.key == ord('w'):
                l.info('Key pressed: UP')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update('UP')
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
                l.info('Key pressed: ESCAPE')
            if event.key == pygame.K_SPACE:
                l.info('Key pressed: EXPLODE')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update('EXPLODE')
        elif event.type == pygame.MOUSEBUTTONUP:
            l.info('Mouse button pressed')
            pos = pygame.mouse.get_pos()

            all_sprites_clicked = [sprite for sprite in all_sprites if sprite.rect.collidepoint(pos)]
            player_sprites_clicked = [sprite for sprite in all_sprites_clicked if player_group.has(sprite)] # NB: Want to implement a way to detect a player without passing the player group as an argument.
            court_sprites_clicked = [sprite for sprite in all_sprites_clicked if court_group.has(sprite)] # NB: Want to implement a way to detect a player without passing the player group as an argument.

            if len(court_sprites_clicked) == 1:
                court_sprites_clicked[0].select()
            elif len(court_sprites_clicked) < 1:
                # NB: This is a terrible implementation of deselection all the players but it'll have to do for now.
                for c in court_group:
                    c.deselect()

            if len(player_sprites_clicked) == 1:
                player_sprites_clicked[0].select()
            elif len(player_sprites_clicked) < 1:
                # NB: This is a terrible implementation of deselection all the players but it'll have to do for now.
                for p in player_group:
                    p.deselect()
            else:
                pass
                # NYI errors or features if multiple players are selected at once.
