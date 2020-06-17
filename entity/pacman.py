import pygame as pg

from entity.entity import Entity
from locations import Coordinate


class Pacman(Entity):
    def __init__(self):
        Entity.__init__(self, Coordinate(13, 23),
                        pg.image.load("assets/images/pacman.png"))
