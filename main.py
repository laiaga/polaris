""" Entry point of the game """

import sys
import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = 800, 600
BLACK = 0, 0, 0
SCREEN = pygame.display.set_mode(SIZE)

while 1:
  for event in pygame.event.get():
    if event.type == pygame.QUIT: sys.exit()

  SCREEN.fill(BLACK)