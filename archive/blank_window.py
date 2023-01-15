"""A simple blank window."""
import sys

import pygame as pg

# Game init
pg.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # width, height
pg.display.set_caption('Blank Window')
clock = pg.time.Clock()

ship_surface = pg.image.load('graphics/ship.png').convert_alpha()  # .png does not run fast
ship_rectangle = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pg.image.load('graphics/laser.png').convert_alpha()
laser_rectangle = laser_surface.get_rect(midbottom=ship_rectangle.midtop)

# print(ship_rectangle)  # <rect(351, 263, 99, 75)>: left, top, width, height

background_surface = pg.image.load('graphics/background.png').convert()  # no alpha convert

font = pg.font.Font('fonts/subatomic.ttf', 30)

# True: anti-aliasing, soft edges, False: pixelated edges
text_surface = font.render('Asteroid Shooter', True, (255, 255, 255))
text_rectangle = text_surface.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))

while True:
    # 1. player input -> events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # 1.5. frame rate limit
    clock.tick(120)

    # ship_rectangle.center = pg.mouse.get_pos()
    laser_rectangle.y -= 10

    #2. update game state
    # display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))
    display_surface.blit(ship_surface, ship_rectangle)
    display_surface.blit(text_surface, text_rectangle)
    display_surface.blit(laser_surface, laser_rectangle)

    #3. update display surface / show frame to player
    pg.display.update()
