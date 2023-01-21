"""Asteroids module."""
from random import randint, uniform

import pygame as pg

from shooter import WINDOW_HEIGHT


class Asteroid(pg.sprite.Sprite):
    """Asteroid class."""

    def __init__(self, pos: tuple, groups: pg.sprite.Group) -> None:
        """Initiate the asteroid.

        Args:
            pos (tuple): _description_
            groups (pg.sprite.Group): _description_
        """
        super().__init__(groups)

        self.asteroid_surface = pg.image.load('src/graphics/meteor.png').convert_alpha()
        self.asteroid_size = pg.math.Vector2(self.asteroid_surface.get_size()) * uniform(0.5, 1.5)
        self.scaled_surface = pg.transform.scale(self.asteroid_surface, self.asteroid_size)
        self.image = self.scaled_surface
        self.rect = self.image.get_rect(center=pos)
        self.mask = pg.mask.from_surface(self.image)
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(300, 500)

        # Rotation
        self.rotation = 0
        self.rotation_speed = uniform(20, 50)

    def rotate(self, dt: float) -> None:
        """Rotate the asteroid."""
        self.rotation += self.rotation_speed * dt
        self.image = pg.transform.rotozoom(self.scaled_surface, self.rotation, 1)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.mask = pg.mask.from_surface(self.image)

    def update(self, dt: float) -> None:
        """
        Update the asteroid.

        :param dt: The delta time.
        """
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
        self.rotate(dt=dt)

        if self.rect.top > WINDOW_HEIGHT:
            self.kill()
