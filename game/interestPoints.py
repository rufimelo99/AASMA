import pygame as pg
from .parkingSpot import parkingSpot

class interestPoints:
    def __init__(self, Id, entryX, entryY, parkingSpots):
        #gonna have the entries/deliveries of each interest point so each driver knows where to deliver and name
        self.Id = Id
        self.entryX = entryX
        self.entryY = entryY
        #place to park after
        self.parkingSpots = parkingSpots
        self.pathToA = []
        self.pathToB = []
        self.pathToC = []
        self.pathToD = []
        self.pathToE = []
        self.pathToF = []
        self.pathToG = []
        


