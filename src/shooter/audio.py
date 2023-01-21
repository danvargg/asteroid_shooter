"""Game sounds."""
import pygame as pg


class Sound:
    """Sound class."""

    def __init__(self):
        """Initialize the sounds."""
        self.laser_sound = pg.mixer.Sound('sounds/laser.ogg')
        self.explosion_sound = pg.mixer.Sound('sounds/explosion.wav')
        self.background_music = pg.mixer.Sound('sounds/music.wav')
        self.background_music.play(loops=-1)

    def play_laser(self):
        """Play the laser sound."""
        self.laser_sound.play()

    def play_explosion(self):
        """Play the explosion sound."""
        self.explosion_sound.play()

    def play_music(self):
        """Play the background music."""
        self.background_music.play()
