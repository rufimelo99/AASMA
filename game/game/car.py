
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
        '''
        self.qinit = np.array([[442.87655921, 488.28185108, 544.51697938, 564.70452657, 558.42562394,
  555.89631061, 517.43063337],
 [512.71809233, 430.04345327, 544.45816399, 546.81711971, 618.13744336,
  515.90611056, 533.40815479],
 [519.19178154, 571.14251479, 477.64635278, 531.04529539, 553.06598011,
  562.97720474, 573.97079415],
 [548.65719829, 571.99750867, 563.63716439, 474.40041987, 538.91606104,
  544.11159731, 549.58670028],
 [504.20977866, 550.42841196, 566.23473663, 562.75083911, 473.91057599,
  561.13573992, 551.70076632],
 [491.5074289, 508.7723295,  550.52838097, 596.51448055, 577.33091411,
  465.9211291,  528.62981209],
 [486.64190725, 527.56930372, 578.24974099, 579.10507857, 586.94585257,
  514.7669176,  446.12709123]])
  '''
        self.numberOfTrips = 0
        self.personWaitime = 0
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
        self.numberOfPersons = 0
        self.timeClient = 0
        self.allPersonWaitTime = 0
        self.meanAllPersonWaitTime = 0
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
    def new_caminho2(self):
        self.caminho = [[11, 17],[12, 17],[13, 17],[14,17],[14, 16],[14,15],[14,14]]
    
    def new_caminho3(self):
        self.caminho = [[14, 20],[14, 19],[14, 18],[14,17],[14, 16],[14,15],[14,14],[14,13],[14,12]]
    def new_caminho1(self):
        self.caminho = [[14, 21],[14, 20],[14, 19],[14, 18],[14,17],[14, 16],[14,15],[14,14],[14,13]]

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
        
        
        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK

    def selectRandomNewParkingLot2(self, localss,interestPointsDic):
        new_local = random.choice(localss)
        
        
        while(new_local == self.local):
            new_local = random.choice(localss)
            
        
        self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK 
    
    def selectClosestParkingLot(self,interestPointsDic):
        self.closestParkinglots = interestPointsDic[self.local].closest.copy()

        
        new_local = self.closestParkinglots.pop(0)
        

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
        

        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK

        return True
        

    def qlearningIteration(self,stat,act, nextstate,c):
        
        state = self.mapStates[stat]
        action = self.mapStates[act]
        cost = c
        nextState = self.mapStates[nextstate]

       

       


        self.qinit[state][action] += 0.3*(cost + 0.9 * np.min(self.qinit[nextState]) - self.qinit[state][action])

    
    def selectLearningParkinglot(self, interestPointsDic, state_values):

        self.closestParkinglots = interestPointsDic[self.local].closest.copy()



        
        
        aux = rnd.choice(len(state_values))
        
        aux1 = rnd.choice(np.where(state_values == np.min(state_values))[0])


        
        index = rnd.choice([aux, aux1], p = [0.15, 0.85])

        new_local = self.mapStates2[index]

        self.closestParkinglots.remove(new_local)
        
        

        if(new_local != self.local):
            self.caminho = interestPointsDic[self.local].paths[new_local].copy()
        else:
            self.caminho = []
        self.local = new_local
        self.state = carState.SEARCH_NEW_PARK


  
              
        