import pygame as pg
import random as r

from entity.ghost import Ghost
from locations import Coordinate, Movement


class Pinky(Ghost):
    def __init__(self):
        Ghost.__init__(self, Coordinate(1, 1),
                       pg.image.load("assets/images/pinky.png"))

    def move(self):
        next_move = r.choice(list(Movement))

        Ghost.move(self, next_move)