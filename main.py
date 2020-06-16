import pygame as pg


def get_input():
    pass


def update():
    pass


def draw():
    pass


def start_game():
    pg.init()

    size = width, height = 320, 240

    screen = pg.display.set_mode(size)

    while 1:
        get_input()
        update()
        draw_models()


if __name__ == '__main__':
    start_game()
