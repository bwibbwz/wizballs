import pygame
import random
from players import Player, Balls, Wizard
from groups import PlayerGroup
from conf import *

pygame.init()

screen = pygame.display.set_mode([X_SIZE, Y_SIZE])

def player_placement(s, p):
    # Placement of players on field according to rules...
    # ...dummy func: dont place them such that they render outside screen
    return random.randrange(s-p)

# List of active players on field
player_list = PlayerGroup()
wizard_list = PlayerGroup()
ball_list = PlayerGroup()

for i in range(6):
    c_idx = random.randint(0,5)
    player = Player(c_idx, GRID_SIZE, 1)

    player.rect.x = player_placement(X_SIZE, GRID_SIZE)
    player.rect.y = player_placement(Y_SIZE, GRID_SIZE)
    player_list.add(player)

radius = 10
ball = Balls(radius, GRID_SIZE)
ball.rect.x = 50
ball.rect.y = 50

ball_list.add(ball)

for i in range(2):
    c_idx = random.randint(0,2)
    wizard = Wizard(c_idx, GRID_SIZE, 1)
    wizard.rect.x = player_placement(X_SIZE, GRID_SIZE)
    wizard.rect.y = player_placement(Y_SIZE, GRID_SIZE)
    wizard_list.add(wizard)

import time

test=True

while test:
    screen.fill(CL_BG)
    player_list.draw(screen)
    wizard_list.draw(screen)
    ball_list.draw(screen)
    pygame.display.flip()

    time.sleep(0.5)
    test=False

pygame.quit()
