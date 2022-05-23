import pygame
import pygame as pg
from config import *

from map_generator import MapGenerator

pg.init()
display = pg.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))
screen = pg.Surface((DISPLAY_WIDTH / DISPLAY_SCALE, DISPLAY_HEIGHT / DISPLAY_SCALE))
pg.display.set_caption(' -=- My First Game -=- ')

font = pg.font.Font(FONT_FILE, 40)

game = True
text1 = '#'
text2 = '1'
i = 1

text1_font = font.render(text1, False, BLACK)
text2_font = font.render(text2, False, BLACK)

x, y = 1, 1

map = MapGenerator(surface=screen, coords=(x, y), seed=1, map_level=0)
screen.fill(WHITE)
screen = map.set_tilesmap()

move = True

while game:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
            pg.quit()
            quit()

    if move:
        map.coords = (x, y)
        screen = map.set_tilesmap()
        move = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        y -= 1
        move = True
    if keys[pygame.K_a]:
        x -= 1
        move = True
    if keys[pygame.K_s]:
        y += 1
        move = True
    if keys[pygame.K_d]:
        x += 1
        move = True
    if keys[pygame.K_q]:
        map.set_map_level(map.map_level - 0.01)
        move = True
    if keys[pygame.K_e]:
        map.set_map_level(map.map_level + 0.01)
        move = True
    if keys[pygame.K_f]:
        map.set_noise_octave(map.octave - 0.01)
        move = True
    if keys[pygame.K_r]:
        map.set_noise_octave(map.octave + 0.01)
        move = True

    # font_size_done = False
    # if not font_size_done:
    #     if text1_font.get_rect()[2] >= DISPLAY_WIDTH / DISPLAY_SCALE - font.render('#', False, BLACK).get_rect()[2]:
    #         font_size_done = True
    #     else:
    #         text2 = str(i) + " " + str(text1_font.get_rect())
    #         text1 = '#' * i
    #         text1_font = font.render(text1, False, BLACK)
    #         text2_font = font.render(text2, False, BLACK)
    #         i += 1
    # text3_font = font.render(str(screen.get_rect()), False, BLACK)

    text1_font = font.render(f'map level: {map.map_level:0.2f}', False, BLACK)
    text2_font = font.render(f'map octave: {map.octave:0.2f}', False, BLACK)
    text3_font = font.render(f'map coords: {x, y}', False, BLACK)
    screen.blit(text1_font, (0, 0))
    screen.blit(text2_font, (0, 10))
    screen.blit(text3_font, (0, 20))
    display.blit(pg.transform.scale(screen, display.get_rect().size), (0, 0))

    pg.display.update()





