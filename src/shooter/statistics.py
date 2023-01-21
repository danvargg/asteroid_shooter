"""Game statistics."""
import pygame as pg

from shooter import WINDOW_WIDTH, WINDOW_HEIGHT, DISPLAY_SURFACE


class Score:
    """Score class."""

    def __init__(self):
        """Initialize the score."""
        self.font = pg.font.Font('src/fonts/subatomic.ttf', 50)

    def display(self):
        """Display the score."""
        score_text = f'Score: {pg.time.get_ticks() // 1000}'
        text_surface = self.font.render(score_text, True, (255, 255, 255))
        text_rectangle = text_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
        DISPLAY_SURFACE.blit(text_surface, text_rectangle)
        pg.draw.rect(DISPLAY_SURFACE, (255, 255, 255), text_rectangle.inflate(30, 30), width=8, border_radius=5)
