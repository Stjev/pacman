import json
import enum


class Location:
    instance = None

    def __init__(self):
        with open("assets/locations.json", "r") as locations_file:
            self.locations = json.load(locations_file)

        self.width, self.height = len(self.locations[0]), len(self.locations)

        self.valid = list()
        for y, row in enumerate(self.locations):
            for x, field_val in enumerate(row):
                if field_val in [0, 6, 8]:
                    self.valid.append(Coordinate(x, y))

    @staticmethod
    def get_instance():
        if Location.instance is None:
            instance = Location()

        return instance

    def is_valid(self, coordinate):
        return coordinate in self.valid


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def add_if_valid(self, x, y):
        """
        This will only add the given x, y if the coordinate would become a valid new coordinate
        """
        locations = Location.get_instance()

        newCoordinate = self.add_create_new_coord(x, y)

        if locations.is_valid(newCoordinate):
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

    def copy(self, other):
        self.x = other.x
        self.y = other.y

    def to_screen_coordinate(self):
        return [self.x * 16 - 2, self.y * 16 - 2]

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"

    def __eq__(self, other):
        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        return False


class Movement(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
