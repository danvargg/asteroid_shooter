"""A simple blank window."""
import sys

import pygame as pg



def laser_update(laser_list: list = [], speed: int = 300):
    """Update the laser position."""
    for rect in laser_list:
        rect.y -= round(speed * dt)

        if rect.bottom < 0:
            laser_list.remove(rect)


def display_score():
    """Display the score on the screen."""
    score_text = f'Score: {pg.time.get_ticks() // 1000}'
    # True: anti-aliasing, soft edges, False: pixelated edges
    text_surface = font.render(score_text, True, (255, 255, 255))
    text_rectangle = text_surface.get_rect(midbottom=(WINDOW_WIDTH / 2, WINDOW_HEIGHT - 80))
    display_surface.blit(text_surface, text_rectangle)
    pg.draw.rect(display_surface, 'white', text_rectangle.inflate(50, 25), width=5, border_radius=10)


def laser_timer(can_shoot: bool, duration: int = 500):
    """Check if the laser can shoot."""
    if not can_shoot:
        current_time = pg.time.get_ticks()

        if current_time - shoot_time >= duration:
            can_shoot = True
    
    return can_shoot

# Game init
pg.init()
WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
display_surface = pg.display.set_mode(size=(WINDOW_WIDTH, WINDOW_HEIGHT))  # width, height
pg.display.set_caption('Asteroid Shooter')
clock = pg.time.Clock()

ship_surface = pg.image.load('graphics/ship.png').convert_alpha()  # .png does not run fast
# ship_reversed_surface = pg.transform.flip(ship_surface, False, True)  # flip horizontally, vertically
ship_rectangle = ship_surface.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

laser_surface = pg.image.load('graphics/laser.png').convert_alpha()
# laser_rectangle = laser_surface.get_rect(midbottom=ship_rectangle.midtop)
laser_list = []

can_shoot = True
shoot_time = None

# print(ship_rectangle)  # <rect(351, 263, 99, 75)>: left, top, width, height

background_surface = pg.image.load('graphics/background.png').convert()  # no alpha convert

font = pg.font.Font('fonts/subatomic.ttf', 30)

test_rectangle = pg.Rect(100, 200, 400, 500)  # left, top, width, height

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

    # 1.5. frame rate limit
    dt = clock.tick(120) / 1000
    # print(clock.get_fps())

    ship_rectangle.center = pg.mouse.get_pos()

    laser_update(laser_list)
    can_shoot = laser_timer(can_shoot, 500)

    pg.time.get_ticks()  # milliseconds since pygame.init()

    #2. update game state
    display_surface.fill((0, 0, 0))
    display_surface.blit(background_surface, (0, 0))
    
    display_score()
    
    for rect in laser_list:
        display_surface.blit(laser_surface, rect)

    display_surface.blit(ship_surface, ship_rectangle)

    #3. update display surface / show frame to player
    pg.display.update()
