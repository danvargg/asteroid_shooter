"""Asteroid Shooter Initializer."""
import pygame as pg

__version__ = '0.0.1'

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# Basic setup
pg.init()
DISPLAY_SURFACE = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption('Asteroid Shooter')

BACKGROUND_SURFACE = pg.image.load('src/graphics/background.png').convert_alpha()

CLOCK = pg.time.Clock()
