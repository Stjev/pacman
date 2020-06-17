from entity.entity import Entity
from locations import Coordinate


class Ghost(Entity):
    def __init__(self, image):
        Entity.__init__(self, Coordinate(13, 14), image, True)

        self.vulnerable = False


def update_ghosts(ghosts):
    for ghost in ghosts:
        ghost.move()
