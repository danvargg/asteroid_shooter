"""Asteroid Shooter Game."""
import sys

import pygame as pg

from shooter import DISPLAY_SURFACE, CLOCK, BACKGROUND_SURFACE
from shooter.vehicles import Ship, ShipLaser

# Sprite groups
spaceship_group = pg.sprite.Group()
laser_group = pg.sprite.Group()

# Sprite creation
ship = Ship(groups=spaceship_group)
laser = ShipLaser(position=(100, 300), groups=laser_group)

# Game loop
while True:
    # event loop
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

    # Delta time
    dt = CLOCK.tick() / 1000

    # Background
    DISPLAY_SURFACE.blit(BACKGROUND_SURFACE, (0, 0))

    # Update
    spaceship_group.update()

    # Graphics
    spaceship_group.draw(DISPLAY_SURFACE)
    laser_group.draw(DISPLAY_SURFACE)

    # Draw the frame
    pg.display.update()
