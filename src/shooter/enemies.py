"""Asteroids module."""
from random import randint, uniform

import pygame as pg


class Asteroid(pg.sprite.Sprite):
    """Asteroid class."""

    def __init__(self, pos: tuple, groups: pg.sprite.Group) -> None:
        """Initialize an asteroid."""  # TODO: docs
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/meteor.png').convert_alpha()
        self.rect = self.image.get_rect(center=pos)
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(uniform(-0.5, 0.5), 1)
        self.speed = randint(400, 600)

    def update(self, dt: float) -> None:
        """Update the asteroid."""
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
