import pygame as pg
import random as r

from entity.ghost import Ghost
from locations import Coordinate, Movement


class Blinky(Ghost):
    def __init__(self):
        Ghost.__init__(self, pg.image.load("assets/images/blinky.png"))

    def move(self):
        next_move = r.choice(list(Movement))

        Ghost.move(self, next_move)
