import json
import enum
import math


class Location:
    instance = None

    def __init__(self):
        with open("assets/locations.json", "r") as locations_file:
            self.locations = json.load(locations_file)

        self.width, self.height = len(self.locations[0]), len(self.locations)

        self.valid = list()
        self.ghost_only = list()
        for y, row in enumerate(self.locations):
            for x, field_val in enumerate(row):
                if field_val in [0, 6, 8]:
                    self.valid.append(Coordinate(x, y))
                if field_val == 2:
                    self.ghost_only.append(Coordinate(x, y))

    @staticmethod
    def get_instance():
        if Location.instance is None:
            instance = Location()

        return instance

    def is_valid(self, coordinate):
        return coordinate in self.valid

    def is_valid_for_ghosts(self, coordinate):
        return coordinate in self.valid or coordinate in self.ghost_only

    def get_valid_for_ghosts_coords(self):
        return self.valid + self.ghost_only


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def add_if_valid(self, x, y):
        locations = Location.get_instance()
        self.__add_if_valid(x, y, locations.is_valid)

    def add_if_valid_for_ghosts(self, x, y):
        locations = Location.get_instance()
        self.__add_if_valid(x, y, locations.is_valid_for_ghosts)

    def __add_if_valid(self, x, y, validator):
        """
        This will only add the given x, y if the coordinate would become a valid new coordinate
        """
        newCoordinate = self.add_create_new_coord(x, y)

        if validator(newCoordinate):
            self.copy(newCoordinate)

    def add_create_new_coord(self, x, y):
        newx = self.x + x
        newy = self.y + y

        if newy == 14:
            if newx == -1:
                newx = 27
            elif newx == 28:
                newx = 0

        return Coordinate(newx, newy)

    def go_in_direction(self, direction):
        if direction == Movement.UP:
            self.add(0, -1)
        elif direction == Movement.RIGHT:
            self.add(1, 0)
        elif direction == Movement.DOWN:
            self.add(0, 1)
        elif direction == Movement.LEFT:
            self.add(-1, 0)

    def copy(self, other):
        self.x = other.x
        self.y = other.y

    def manhatten_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def to_screen_coordinate(self):
        return [self.x * 16 - 2, self.y * 16 - 2]

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    # get the neighbours of the current coordinate
    def get_neighbours(self):
        unfiltered = [self.add_create_new_coord(
            x, y) for (x, y) in [(-1, 0), (1, 0), (0, -1), (0, 1)]]
        filtered = [
            coord for coord in unfiltered if Location.get_instance().is_valid_for_ghosts(coord)]
        return filtered

    def __hash__(self):
        return self.x * 100 + self.y

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False


class Movement(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

    @staticmethod
    def inverses(movement1, movement2):
        return (movement1 == Movement.UP and movement2 == Movement.DOWN) or \
            (movement1 == Movement.LEFT and movement2 == Movement.RIGHT) or \
            (movement2 == Movement.UP and movement1 == Movement.DOWN) or \
            (movement2 == Movement.LEFT and movement1 == Movement.RIGHT)
