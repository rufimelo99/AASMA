
from .settings import GRID_HEIGHT
from .settings import GRID_WIDTH
from .interestPoints import interestPoints
from .parkingSpot import parkingSpot
from .driverAgent import driverAgent

class Car:
    def __init__(self, position_x, position_y, driverAgent):
        self.driverAgent = driverAgent
        self.position_x = position_x
        self.position_y = position_y
        self.caminho = []
        self.actualInterestPoint = None
        self.nextInterestPoint = None
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

    def new_caminho(self):
        self.caminho = [[11,3], [10,3], [9,3], [8,3], [7,3], [6,3], [5,3], [4,3], [3,3], [3,4], [3,5],[3,6],[3,7],[3,8],[3,9],[3,10],[3,11], [3,12], [3,13], [3,14]]
        
        
    def update(self , x, y):
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
        
            
            