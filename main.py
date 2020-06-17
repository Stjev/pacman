import pygame as pg
import time

from input_handler import Input_handler
from painter import Painter
from game_state import update_game_state
from entity.pacman import Pacman
from entity.blinky import Blinky
from entity.pinky import Pinky
from entity.inky import Inky
from entity.clyde import Clyde

from locations import Movement


def setup():
    pg.init()
    size = 448, 496
    screen = pg.display.set_mode(size)
    pg.display.set_caption('Pacman')

    return screen


def start_game():
    screen = setup()

    pacman = Pacman()
    blinky = Blinky()
    pinky = Pinky()
    inky = Inky()
    clyde = Clyde()

    painter = Painter(screen, pacman, blinky, pinky, inky, clyde)

    input_handler = Input_handler()

    clock = pg.time.Clock()

    while 1:
        events = pg.event.get()

        input_handler.get_input(pacman, events)
        update_game_state(pacman, [blinky, pinky, inky, clyde])

        painter.draw()

        pg.display.update()

        clock.tick(2)


if __name__ == '__main__':
    start_game()
