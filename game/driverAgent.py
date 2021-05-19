import pygame as pg
from .GPS import GPS
import random


class driverAgent:
    def __init__(self, Id, gps):
        self.Id = Id
        self.gps = gps

    #should be atached to a client.. this is temporary
    def generateRandomTrip(self):
        randomChoice = random.choice(list(self.gps.interestPointsDic))
        print("Destination: "+randomChoice)
        #return self.gps.interestPointsDic[randomChoice].entryX, self.gps.interestPointsDic[randomChoice].entryY
        return randomChoice