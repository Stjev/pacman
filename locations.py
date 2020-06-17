import json
import enum


class Location:
    def __init__(self):
        with open("assets/locations.json", "r") as locations_file:
            self.locations = json.load(locations_file)

        self.width, self.height = len(self.locations[0]), len(self.locations)

        self.valid = []
        for y, row in enumerate(self.locations):
            for x, field_val in enumerate(row):
                if field_val == 0:
                    self.valid.append(Coordinate(x, y))


class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, x, y):
        self.x += x
        self.y += y

    def to_screen_coordinate(self):
        return [self.x * 16 - 2, self.y * 16 - 2]

    def __str__(self):
        return "(" + str(self.x) + ", " + str(self.y) + ")"


class Movement(enum.Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
