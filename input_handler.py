import pygame as pg
from locations import Movement


class Input_handler:
    def __init__(self):
        self.next_update = True

    def get_input(self, pacman, events):
        if self.next_update:
            for event in events:
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        pacman.move(Movement.LEFT)
                        self.next_update = False
                    elif event.key == pg.K_RIGHT:
                        pacman.move(Movement.RIGHT)
                        self.next_update = False
                    elif event.key == pg.K_UP:
                        pacman.move(Movement.UP)
                        self.next_update = False
                    elif event.key == pg.K_DOWN:
                        pacman.move(Movement.DOWN)
                        self.next_update = False
                    elif event.key == pg.K_ESCAPE:
                        exit(0)

    def reset_update(self):
        self.next_update = True
