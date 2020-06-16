import pygame as pg

from locations import Movement, Coordinate


class Entity:
    def __init__(self, location, image):
        self.image = pg.transform.scale(image,  (20, 20))
        self.flip_image = pg.transform.flip(self.image, True, False)
        self.location = location
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
            self.location.add(0, -1)
        elif movement == Movement.RIGHT:
            self.direction = movement
            self.location.add(1, 0)
        elif movement == Movement.DOWN:
            self.location.add(0, 1)
        elif movement == Movement.LEFT:
            self.direction = movement
            self.location.add(-1, 0)


class Ghost(Entity):
    def __init__(self, location, image):
        Entity.__init__(self, location, image)

        self.vulnerable = False


class Pacman(Entity):
    def __init__(self):
        Entity.__init__(self, Coordinate(13, 23),
                        pg.image.load("assets/images/pacman.png"))
