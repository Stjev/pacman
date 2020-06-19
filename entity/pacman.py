import pygame as pg

from entity.entity import Entity
from locations import Coordinate, Movement


class Pacman(Entity):
    def __init__(self):
        Entity.__init__(self, Coordinate(13, 23),
                        pg.image.load("assets/images/pacman.png"), False)

    def draw(self, screen):
        # draw this entity, also flip the image if the entity is moving right
        if self.direction == Movement.RIGHT:
            image = self.flip_image
        elif self.direction == Movement.LEFT:
            image = self.image
        elif self.direction == Movement.UP:
            image = pg.transform.rotate(self.image, -90)
        else:
            image = pg.transform.rotate(self.image, 90)

        screen.blit(image, self.location.to_screen_coordinate())

    def move(self, movement):
        if movement == Movement.UP:
            self.add_location(0, -1)
        elif movement == Movement.RIGHT:
            self.add_location(1, 0)
        elif movement == Movement.DOWN:
            self.add_location(0, 1)
        elif movement == Movement.LEFT:
            self.add_location(-1, 0)

        self.direction = movement
