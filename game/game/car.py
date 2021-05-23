
from .settings import GRID_HEIGHT
from .settings import GRID_WIDTH
from .carState import carState
import random

#car states 1 - search parking | lot 2 - free | 3 - occupied

class Car:
    def __init__(self, ID, position_x, position_y, local,parkingSpotID):
        self.state = carState.FREE
        self.id = ID
        self.parkingSpotID = parkingSpotID
        self.position_x = position_x
        self.position_y = position_y
        self.numberOfTrips = 0
        self.waitime = 0
        self.meanWaitime = 0
        self.caminho = []
        self.local = local
        self.closestParkinglots = []
        self.person = None
        if(position_x == 3 and position_y < GRID_HEIGHT-4 and position_y >= 3):
            self.orientation = "taxi_SW"
        elif(position_y == 3 and position_x > 3 and position_x <= GRID_WIDTH-4):
            self.orientation = "taxi_NW"
        elif(position_y == (int(GRID_HEIGHT/2) - 1) and position_x > 3 and position_x < GRID_WIDTH-4):
            self.orientation = "taxi_SE"
        elif(position_y == GRID_HEIGHT - 4 and position_x >= 3 and position_x < GRID_WIDTH-4):
            self.orientation = "taxi_SE"
        else:
            self.orientation = "taxi_NE"
        
        
    def setperson(self, person):
        self.person = person
    def new_caminho(self):
        self.caminho = [[9,17],[10,17],[11,17],[12,17],[13,17],[14,17],[14,16],[14,15],[14,14],[14,12],[14,11],[14,10],[14,9],[14,8],[14,7],[14,6],[14,5],[14,4],[14,3],[13,3],[12,3], [11,3], [10,3], [9,3], [8,3], [7,3], [6,3], [5,3], [4,3], [3,3], [3,4], [3,5],[3,6],[3,7]]
    def update(self, x, y):
        self.position_x = x
        self.position_y = y
        if(self.position_x == 3 and self.position_y < GRID_HEIGHT-4 and self.position_y >= 3):
            self.orientation = "taxi_SW"
        elif(self.position_y == 3 and self.position_x > 3 and self.position_x <= GRID_WIDTH-4):
            self.orientation = "taxi_NW"
        elif(self.position_y == (int(GRID_HEIGHT/2) - 1) and self.position_x > 3 and self.position_x < GRID_WIDTH-4):
            self.orientation = "taxi_SE"
        elif(self.position_y == GRID_HEIGHT - 4 and self.position_x >= 3 and self.position_x < GRID_WIDTH-4):
            self.orientation = "taxi_SE"
        else:
            self.orientation = "taxi_NE"
        


    def selectRandomNewParkingLot(self, localss,interestPointsDic):
        new_local = random.choice(localss)
        print("novo estacionamento" + new_local)
        
        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK  
    
    def selectClosestParkingLot(self,interestPointsDic):
        self.closestParkinglots = interestPointsDic[self.local].closest.copy()

        
        new_local = self.closestParkinglots.pop(0)
        print("1novo estacionamento" + new_local)

        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK


    
    def selectClosestParkingLot2(self,interestPointsDic):
        if(self.closestParkinglots == []):
            return False
        new_local = self.closestParkinglots.pop(0)
        print("2novo estacionamento" + new_local)

        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK

        return True
        

  
              
        