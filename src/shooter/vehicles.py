"""Base classes for space vehicles."""
import pygame as pg

from shooter import WINDOW_WIDTH, WINDOW_HEIGHT


class Ship(pg.sprite.Sprite):  # TODO: add setup code
    """Base class for all ships."""

    def __init__(self, groups: pg.sprite.Group) -> None:
        """Initialize the ship."""  # TODO: docs
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/ship.png').convert_alpha()
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # Timer
        self.can_shoot = True
        self.shoot_time = None

    def laser_timer(self) -> None:
        """Timer for the laser."""
        if not self.can_shoot:
            current_time = pg.time.get_ticks()
            if current_time - self.shoot_time >= 500:
                self.can_shoot = True

    def input_position(self) -> None:
        """Get the position of the mouse."""
        pos = pg.mouse.get_pos()
        self.rect.center = pos

    def laser_shoot(self, laser_group) -> None:
        """Shoot a laser."""
        if pg.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pg.time.get_ticks()

            ShipLaser(position=self.rect.midtop, groups=laser_group)

    def update(self, laser_group) -> None:
        """Update the ship."""
        self.laser_timer()
        self.laser_shoot(laser_group)
        self.input_position()


class ShipLaser(pg.sprite.Sprite):
    """Base class for all ship lasers."""

    def __init__(self, position, groups) -> None:  # TODO: what a bout the instance (self) for position and groups?
        """Initialize the ship laser."""  # TODO: docs
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)

        # Float based position
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(0, -1)
        self.speed = 600

    def update(self, dt: float) -> None:
        """Update the ship laser."""
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))
