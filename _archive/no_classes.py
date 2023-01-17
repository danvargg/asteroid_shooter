"""A simple blank window."""
import sys
from random import randint, uniform

import pygame as pg


def laser_update(laser_list: list = None, speed: int = 300) -> None:
    """Update the laser position."""
    for rect in laser_list:
        rect.y -= round(speed * dt)

        if rect.bottom < 0:
            laser_list.remove(rect)


def display_score() -> None:
    """Display the score on the screen."""
    score_text = f'Score: {pg.time.get_ticks() // 1000}'
    text_surface = font.render(score_text, True, (255, 255, 255))
    text_rectangle = text_surface.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surface, text_rectangle)
    pg.draw.rect(display_surface, 'white', text_rectangle.inflate(50, 25), width=5, border_radius=10)


def laser_timer(can_shoot: bool, duration: int = 500) -> bool:
    """Check if the laser can shoot."""
    if not can_shoot:
        current_time = pg.time.get_ticks()

        if current_time - shoot_time >= duration:
            can_shoot = True

    return can_shoot


def meteor_update(meteor_list: list = None, speed: int = 300) -> None:
    """Update the meteor position."""
    for meteor_tuple in meteor_list:
        direction = meteor_tuple[1]
        meteor_rectangle = meteor_tuple[0]
        meteor_rectangle.center += direction * speed * dt
        if meteor_rectangle.top > WINDOW_HEIGHT:
            meteor_list.remove(meteor_tuple)


# Game init
pg.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
display_surface = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # width, height
pg.display.set_caption('Asteroid Shooter')
clock = pg.time.Clock()

ship_surface = pg.image.load('graphics/ship.png').convert_alpha()  # .png does not run fast
ship_rectangle = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pg.image.load('graphics/laser.png').convert_alpha()
laser_list = []

can_shoot = True
shoot_time = None

background_surface = pg.image.load('graphics/background.png').convert()  # no alpha convert

font = pg.font.Font('fonts/subatomic.ttf', 30)

# Meteor
meteor_surface = pg.image.load('graphics/meteor.png').convert_alpha()
meteor_list = []

# meteor timer
meteor_timer = pg.event.custom_type()
pg.time.set_timer(meteor_timer, 1000)

test_rectangle = pg.Rect(100, 200, 400, 500)  # left, top, width, height

# Sound
laser_sound = pg.mixer.Sound('sounds/laser.ogg')
explosion_sound = pg.mixer.Sound('sounds/explosion.wav')
background_music = pg.mixer.Sound('sounds/music.wav')
background_music.play(loops=-1)

while True:
    # 1. player input -> events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            sys.exit()

        if event.type == pg.MOUSEBUTTONDOWN and can_shoot:
            laser_rectangle = laser_surface.get_rect(midbottom=ship_rectangle.midtop)
            laser_list.append(laser_rectangle)

            # timer
            can_shoot = False
            shoot_time = pg.time.get_ticks()

            # play laser sound
            laser_sound.play()

        if event.type == meteor_timer:
            x_pos = randint(-100, WINDOW_WIDTH + 100)
            y_pos = randint(-100, -50)
            meteor_rectangle = meteor_surface.get_rect(center=(x_pos, y_pos))
            direction = pg.math.Vector2(uniform(-0.5, 0.5), 1)
            meteor_list.append((meteor_rectangle, direction))

    # 1.5. frame rate limit
    dt = clock.tick(120) / 1000

    ship_rectangle.center = pg.mouse.get_pos()

    laser_update(laser_list)
    meteor_update(meteor_list)
    can_shoot = laser_timer(can_shoot, 500)

    # Meteor and ship collisions
    for meteor_tuple in meteor_list:
        meteor_rectangle = meteor_tuple[0]
        if meteor_rectangle.colliderect(ship_rectangle):
            pg.quit()
            sys.exit()  # TODO: print game over and score

    # Laser and meteor collisions
    for laser_rect in laser_list:
        for meteor_tuple in meteor_list:
            meteor_rectangle = meteor_tuple[0]
            if laser_rect.colliderect(meteor_rectangle):
                laser_list.remove(laser_rect)
                meteor_list.remove(meteor_tuple)
                explosion_sound.play()

    pg.time.get_ticks()  # milliseconds since pygame.init()

    # 2. update game state
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))

    display_score()

    for rect in laser_list:
        display_surface.blit(laser_surface, rect)

    for meyeor_tuple in meteor_list:
        display_surface.blit(meteor_surface, meyeor_tuple[0])

    display_surface.blit(ship_surface, ship_rectangle)

    # 3. update display surface / show frame to player
    pg.display.update()
