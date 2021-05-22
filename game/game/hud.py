import pygame as pg


class Hud:

    def __init__(self, width, height):
        self.width = width
        self.height = height


        self.hud_colour = (198, 155, 93, 175)


        self.car_surface = pg.Surface((width * 0.15, height * 0.25), pg.SRCALPHA)
        self.car_surface.fill(self.hud_colour)


    def draw(self, screen):

        screen.blit(self.car_surface, (self.width * 0.84 , self.height * 0.74))
        