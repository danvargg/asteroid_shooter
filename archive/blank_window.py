"""A simple blank window."""
import sys

import pygame as pg

WINDOW_WIDTH, WINDOW_HEIGHT = 400, 300

pg.init()

display_surface = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # width, height

test_surface = pg.Surface((200, 150))

pg.display.set_caption('Blank Window')

while True:
    # 1. player input -> events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    #2. update game state
    display_surface.fill((15, 140, 122))
    test_surface.fill((52, 235, 149))
    display_surface.blit(test_surface, (50, 70))

    #3. update display surface / show frame to player
    pg.display.update()
