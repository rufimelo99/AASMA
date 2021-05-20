import pygame as pg

class parkingSpot:
    def __init__(self, Id, posX, posY):
        #position
        self.Id = Id
        self.posX = posX
        self.posY = posY
        self.available=True