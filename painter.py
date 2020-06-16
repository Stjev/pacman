import pygame as pg


class Painter():
    def __init__(self, screen, pacman, blinky, pinky, inky, clyde):
        self.bg = pg.image.load("assets/images/map.jpg")

        self.screen = screen
        self.pacman = pacman
        self.blinky = blinky
        self.pinky = pinky
        self.inky = inky
        self.clyde = clyde

    def draw(self):
        self.screen.blit(self.bg, [0, 0])  # draw the background
        self.pacman.draw(self.screen)

