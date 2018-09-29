import pygame
import random
from players import Player
from groups import PlayerGroup

pygame.init()

# Screen stuff
width  = 700
height = 400

white = (255,255,255)

screen = pygame.display.set_mode([width, height])

def player_placement(s, p):
    # Placement of players on field according to rules...
    # ...dummy func: dont place them such that they render outside screen
    return random.randrange(s-p)

# List of active players on field
player_list = PlayerGroup()

for i in range(5):
    c_idx = random.randint(0,2)
    player = Player(c_idx,20,20)

    player.rect.x = player_placement(width, 20)
    player.rect.y = player_placement(height, 20)

    player_list.add(player)

import time

test=True

while test:
    screen.fill(white)
    player_list.draw(screen)
    pygame.display.flip()

    time.sleep(0.5)
    test=False

pygame.quit()
