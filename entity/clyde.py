import pygame as pg
import random as r

from entity.ghost import Ghost
from locations import Coordinate, Movement


class Clyde(Ghost):
    def __init__(self):
        Ghost.__init__(self, pg.image.load("assets/images/clyde.png"))

    def move(self, pacman_location):
        next_move = r.choice(list(Movement))

        Ghost.move(self, next_move)
