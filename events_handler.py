#!/usr/bin/env python3

import pygame
import logging as l
from basic_functions import quit_game
from controls import right, left, up, down

def process_events(events, all_sprites, player_group, court_group):
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
                    sprite[0].update(right)
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                l.info('Key pressed: LEFT')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update(left)
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                l.info('Key pressed: DOWN')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update(down)
            if event.key == pygame.K_UP or event.key == ord('w'):
                l.info('Key pressed: UP')
                sprite = [s for s in player_group if s.is_selected()]
                if sprite:
                    sprite[0].update(up)
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

            # NB: It would be NICE to manage this without passing the individual groups as arguments.
            player_sprites_clicked = [sprite for sprite in all_sprites_clicked if player_group.has(sprite)]
            court_sprites_clicked = [sprite for sprite in all_sprites_clicked if court_group.has(sprite)]

            if len(court_sprites_clicked) == 1:
                court_sprites_clicked[0].select()
            elif len(court_sprites_clicked) < 1:
                court_group.deselect_all_sprites()

            if len(player_sprites_clicked) == 1:
                player_sprites_clicked[0].select()
            elif len(player_sprites_clicked) < 1:
                player_group.deselect_all_sprites()
            else:
                for s in player_sprites_clicked:
                    s.update('EXPLODE')
                pass
                # NYI errors or features if multiple players are selected at once.
