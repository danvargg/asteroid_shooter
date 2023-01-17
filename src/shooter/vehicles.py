"""Base classes for space vehicles."""
import pygame as pg

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

class Ship(pg.sprite.Sprite):
    """Base class for all ships."""

    def __init__(self, groups: pg.sprite.Group) -> None:
        """Initialize the ship."""  # TODO: docs
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

class ShipLaser(pg.sprite.Sprite):
    """Base class for all ship lasers."""

    def __init__(self, position, groups) -> None:  # TODO: what a bout the instance (self) for position and groups?
        """Initialize the ship laser."""  # TODO: docs
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
