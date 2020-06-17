from entity.entity import Entity

from locations import Coordinate, Location, Movement


class Ghost(Entity):
    def __init__(self, image):
        Entity.__init__(self, Coordinate(13, 14), image, True)
        self.movement = Movement.UP

    def move(self, movement):
        locations = Location.get_instance()

        next_coord = Coordinate(
            self.location.x, self.location.y)
        next_coord.go_in_direction(movement)

        if not Movement.inverses(self.movement, movement) and locations.is_valid_for_ghosts(next_coord):
            self.movement = movement
        super().move(self.movement)


def update_ghosts(ghosts):
    for ghost in ghosts:
        ghost.move()
