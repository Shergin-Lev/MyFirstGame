from typing import Tuple

from perlin_noise import PerlinNoise
import pygame

from config import *


class MapGenerator:
    range_x: range
    range_y: range
    octave: float
    noise: PerlinNoise

    def __init__(self, surface: pygame.Surface, coords: Tuple[int, int], seed: int = 1, map_level: float = 0):
        self.surface = surface
        self.coords = coords
        self.octave = 3
        self.seed = seed
        self.grass1 = pygame.image.load('images/grass1.png')
        self.rock1 = pygame.image.load('images/rock1.png')
        self.tree1 = pygame.image.load('images/tree1.png')
        self.water1 = pygame.image.load('images/water1.png')
        self.map_level = map_level
        self.set_noise_octave(self.octave)


    def set_map_level(self, map_level: float):
        if -0.2 <= map_level <= 0.2:
            self.map_level = map_level

    def set_noise_octave(self, octave: float):
        if 1 <= octave <= 5:
            self.octave = octave
            self.noise = PerlinNoise(octaves=self.octave, seed=self.seed)

    def get_range(self):
        self.range_x = range(self.coords[0],
                             int(self.coords[0] + SCALED_DISPLAY_W + 1))
        self.range_y = range(self.coords[1],
                             int(self.coords[1] + SCALED_DISPLAY_H + 1))

    def get_map(self):
        pic_num = [[self.noise([y/SCALED_DISPLAY_W, x/SCALED_DISPLAY_H])
                    for x in self.range_x] for y in self.range_y]
        return pic_num

    def set_tilesmap(self):
        self.get_range()
        pic_num = self.get_map()
        for x in range(0, int(DISPLAY_WIDTH / DISPLAY_SCALE), TILE_STEP):
            for y in range(0, int(DISPLAY_HEIGHT / DISPLAY_SCALE), TILE_STEP):
                xx = int((x) / TILE_STEP)
                yy = int((y) / TILE_STEP)
                if pic_num[yy][xx] <= self.map_level + 0.4:
                    self.surface.blit(self.grass1, (x, y))
                    if self.map_level - 0.3 <= pic_num[yy][xx] <= self.map_level:
                        self.surface.blit(self.tree1, (x, y))
                    elif pic_num[yy][xx] <= self.map_level - 0.3:
                        self.surface.blit(self.rock1, (x, y))
                else:
                    self.surface.blit(self.water1, (x, y))
        return self.surface
