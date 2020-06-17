import pygame as pg
import time

from input_handler import Input_handler
from painter import Painter
from entity import Pacman

from locations import Movement


def update():
    return


def setup():
    pg.init()
    size = width, height = 448, 496
    screen = pg.display.set_mode(size)
    pg.display.set_caption('Pacman')

    return screen

# TODO: https://stackoverflow.com/questions/54981456/how-to-implement-a-pygame-timed-game-loop


def start_game():
    screen = setup()

    pacman = Pacman()
    painter = Painter(screen, pacman, None, None, None, None)

    input_handler = Input_handler()

    clock = pg.time.Clock()

    while 1:
        events = pg.event.get()

        input_handler.get_input(pacman, events)

        update()
        painter.draw()

        pg.display.update()

        clock.tick(2)


if __name__ == '__main__':
    start_game()
