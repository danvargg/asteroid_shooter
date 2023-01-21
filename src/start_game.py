"""Asteroid Shooter Game."""
import sys
from random import randint

import pygame as pg

from shooter import DISPLAY_SURFACE, CLOCK, BACKGROUND_SURFACE, WINDOW_WIDTH
from shooter.vehicles import Ship
from shooter.enemies import Asteroid
from shooter.statistics import Score

# Sprite groups
spaceship_group = pg.sprite.Group()
laser_group = pg.sprite.Group()
asteroid_group = pg.sprite.Group()

# Sprite creation
ship = Ship(groups=spaceship_group)
asteroid_timer = pg.event.custom_type()
pg.time.set_timer(asteroid_timer, millis=400)

score = Score()

# Game loop
while True:
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == asteroid_timer:
            asteroid_y_pos = randint(-150, -50)
            asteroid_x_pos = randint(-100, WINDOW_WIDTH + 100)
            Asteroid(pos=(asteroid_x_pos, asteroid_y_pos), groups=asteroid_group)

    # Delta time
    dt = CLOCK.tick() / 1000

    # Background
    DISPLAY_SURFACE.blit(BACKGROUND_SURFACE, (0, 0))

    # Update
    spaceship_group.update(laser_group=laser_group)
    laser_group.update(dt=dt)
    asteroid_group.update(dt=dt)
    score.display()

    # Graphics
    spaceship_group.draw(DISPLAY_SURFACE)
    laser_group.draw(DISPLAY_SURFACE)
    asteroid_group.draw(DISPLAY_SURFACE)

    # Draw the frame
    pg.display.update()
