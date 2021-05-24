
from .settings import GRID_HEIGHT
from .settings import GRID_WIDTH
from .carState import carState
import random
import numpy as np
import numpy.random as rnd

#car states 1 - search parking | lot 2 - free | 3 - occupied

class Car:
    def __init__(self, ID, position_x, position_y, local,parkingSpotID):
        self.state = carState.FREE
        self.id = ID
        self.parkingSpotID = parkingSpotID
        self.position_x = position_x
        self.position_y = position_y
        self.states = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
        self.mapStates = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E':4, 'F': 5, 'G': 6}
        self.mapStates2 = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G'}
        self.qinit = np.zeros((len(self.states), len(self.states)))
        self.numberOfTrips = 0
        self.waitime = 0
        self.allwaitime = 0
        self.meanWaitime = 0
        self.lengthpathClient = 0
        self.meanlengthpathClient = 0
        self.allengthpathClient = 0
        self.persondestino = None
        self.pathtoparkinglot = 0
        self.allpathtoparkinglot = 0
        self.meanpathtoparkinglot = 0
        self.caminho = []
        self.local = local
        self.closestParkinglots = []
        self.tripsPerTimeUnit = 0
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
        self.persondestino = person.destino
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

    def selectRandomNewParkingLot2(self, localss,interestPointsDic):
        new_local = random.choice(localss)
        print("novo estacionamento" + new_local)
        
        while(new_local == self.local):
            new_local = random.choice(localss)
            print("novo estacionamento" + new_local)
        
        self.caminho = interestPointsDic[self.local].paths[new_local].copy()
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
        

    def qlearningIteration(self, nextstate):
        
        state = self.mapStates[self.persondestino]
        action = self.mapStates[self.local]
        cost = self.pathtoparkinglot + self.waitime + self.lengthpathClient
        nextState = self.mapStates[nextstate]

       

       


        self.qinit[state][action] += 0.3*(cost + 0.9 * np.min(self.qinit[nextState]) - self.qinit[state][action])

    
    def selectLearningParkinglot(self, interestPointsDic, state_values):

        self.closestParkinglots = interestPointsDic[self.local].closest.copy()



        
        
        aux = rnd.choice(len(state_values))
        
        aux1 = rnd.choice(np.where(state_values == np.min(state_values))[0])


        
        index = rnd.choice([aux, aux1], p = [0.15, 0.85])

        new_local = self.mapStates2[index]

        self.closestParkinglots.remove(new_local)
        
        print("1novo estacionamento" + new_local)

        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK


  
              
        