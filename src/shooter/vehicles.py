"""Base classes for space vehicles."""
import pygame as pg

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720  # TODO: move to init


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

    def laser_shoot(self) -> None:
        """Shoot a laser."""
        if pg.mouse.get_pressed()[0] and self.can_shoot:
            self.can_shoot = False
            self.shoot_time = pg.time.get_ticks()

            print('laser shoot')

    def update(self) -> None:
        """Update the ship."""
        self.laser_timer()
        self.laser_shoot()
        self.input_position()


class ShipLaser(pg.sprite.Sprite):
    """Base class for all ship lasers."""

    def __init__(self, position, groups) -> None:  # TODO: what a bout the instance (self) for position and groups?
        """Initialize the ship laser."""  # TODO: docs
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
