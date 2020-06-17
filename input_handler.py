import pygame as pg
from locations import Movement


class Input_handler:
    def __init__(self):
        self.current_direction = Movement.RIGHT

    def get_input(self, pacman, events):
        for event in events:
            if event.type == pg.QUIT:
                exit(0)

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit(0)

                if event.key == pg.K_LEFT:
                    self.current_direction = Movement.LEFT
                elif event.key == pg.K_RIGHT:
                    self.current_direction = Movement.RIGHT
                elif event.key == pg.K_UP:
                    self.current_direction = Movement.UP
                elif event.key == pg.K_DOWN:
                    self.current_direction = Movement.DOWN

        pacman.move(self.current_direction)
