import pygame as pg
import random as r

from entity.ghost import Ghost
from locations import Coordinate, Movement
from pathfinder import a_star


class Blinky(Ghost):
    def __init__(self):
        Ghost.__init__(self, pg.image.load("assets/images/blinky.png"))

    def move(self, pacman_location):
        self.location = a_star(self.location, pacman_location)
