  
import pygame as pg
from .parkingSpot import parkingSpot

class interestPoints:
    def __init__(self, Id, entryX, entryY, parkingSpots,closest_parking_lots):
        #gonna have the entries/deliveries of each interest point so each driver knows where to deliver and name
        self.Id = Id
        self.entryX = entryX
        self.entryY = entryY
        #place to park after
        self.parkingSpots = parkingSpots
        self.closest_parking_lots = closest_parking_lots
        self.paths = {'A': [], 'B': [], 'C': [], 'D': [], 'E': [], 'F': [], 'G': []}
        self.pathToA = []
        self.pathToB = []
        self.pathToC = []
        self.pathToD = []
        self.pathToE = []
        self.pathToF = []
        self.pathToG = []
        self.cars = []
        self.numberpersons = 0