"""Base classes for space vehicles."""
import pygame as pg

from shooter import WINDOW_WIDTH, WINDOW_HEIGHT


class Ship(pg.sprite.Sprite):
    """Base class for all ships."""

    def __init__(self, groups: pg.sprite.Group) -> None:
        """Initialize the ship."""

        # 1. Super the class
        super().__init__(groups)

        # 2. Create surface
        self.image = pg.image.load('src/graphics/ship.png').convert_alpha()

        # 3. Create rectangle
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # 4. Add a mask
        self.mask = pg.mask.from_surface(self.image)

        # Timer
        self.can_shoot = True
        self.shoot_time = None

        self.laser_sound = pg.mixer.Sound('src/sounds/laser.ogg')

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

            self.laser_sound.play()

    def asteroid_collision(self, asteroid_group) -> None:
        """Check for collisions with asteroids."""
        if pg.sprite.spritecollide(self, asteroid_group, False, pg.sprite.collide_mask):
            pg.quit()
            sys.exit()

    def update(self, laser_group, asteroid_group) -> None:
        """Update the ship."""
        self.laser_timer()
        self.laser_shoot(laser_group)
        self.input_position()
        self.asteroid_collision(asteroid_group)


class ShipLaser(pg.sprite.Sprite):
    """Base class for all ship lasers."""

    def __init__(self, position, groups) -> None:
        """Initialize the ship laser."""
        super().__init__(groups)

        self.image = pg.image.load('src/graphics/laser.png').convert_alpha()
        self.rect = self.image.get_rect(midbottom=position)
        self.mask = pg.mask.from_surface(self.image)

        # Float based position
        self.pos = pg.math.Vector2(self.rect.topleft)
        self.direction = pg.math.Vector2(0, -1)
        self.speed = 600

        self.explosion_sound = pg.mixer.Sound('src/sounds/explosion.wav')

    def asteroid_collision(self, asteroid_group) -> None:
        """Check for collisions with asteroids."""
        if pg.sprite.spritecollide(self, asteroid_group, True, pg.sprite.collide_mask):
            self.kill()
            self.explosion_sound.play()

    def update(self, dt: float, asteroid_group) -> None:
        """Update the ship laser."""
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

        if self.rect.bottom < 0:
            self.kill()

        self.asteroid_collision(asteroid_group)
