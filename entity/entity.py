import pygame as pg
from locations import Movement, Coordinate


class Entity:
    def __init__(self, location, image, ghost):
        self.location = location

        if ghost:
            self.add_location = self.location.add_if_valid_for_ghosts
        else:
            self.add_location = self.location.add_if_valid

        self.image = pg.transform.scale(image,  (20, 20))
        self.flip_image = pg.transform.flip(self.image, True, False)
        self.direction = Movement.RIGHT

    def draw(self, screen):
        # draw this entity, also flip the image if the entity is moving right
        if self.direction == Movement.RIGHT:
            image = self.flip_image
        else:
            image = self.image

        screen.blit(image, self.location.to_screen_coordinate())

    def move(self, movement):
        if movement == Movement.UP:
            self.add_location(0, -1)
        elif movement == Movement.RIGHT:
            self.direction = movement
            self.add_location(1, 0)
        elif movement == Movement.DOWN:
            self.add_location(0, 1)
        elif movement == Movement.LEFT:
            self.direction = movement
            self.add_location(-1, 0)
