"""A simple blank window."""
import sys

import pygame as pg

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600

pg.init()

display_surface = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # width, height

pg.display.set_caption('Blank Window')

ship_surface = pg.image.load('archive/graphics/ship.png').convert_alpha()  # .png does not run fast
ship_rectangle = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

# print(ship_rectangle)  # <rect(351, 263, 99, 75)>: left, top, width, height

background_surface = pg.image.load('archive/graphics/background.png').convert()  # no alpha convert

font = pg.font.Font('archive/fonts/subatomic.ttf', 30)

# True: anti-aliasing, soft edges, False: pixelated edges
text_surface = font.render('Asteroid Shooter', True, (255, 255, 255))
text_rectangle = text_surface.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

clock = pg.time.Clock()

while True:
    # 1. player input -> events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # 1.5. frame rate limit
    clock.tick(120)

    #2. update game state
    # display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))
    # ship_rectangle.center = pg.mouse.get_pos()
    if ship_rectangle.top > 0:
        ship_rectangle.y -= 4
    display_surface.blit(ship_surface, ship_rectangle)
    display_surface.blit(text_surface, text_rectangle)

    #3. update display surface / show frame to player
    pg.display.update()
