
from .settings import GRID_HEIGHT
from .settings import GRID_WIDTH

#car states 1 - search parking | lot 2 - free | 3 - occupied

class Car:
    def __init__(self, ID, position_x, position_y, local,parkingSpotID):
        self.id = ID
        self.parkingSpotID = parkingSpotID
        self.state = 2
        self.position_x = position_x
        self.position_y = position_y
        self.caminho = []
        self.local = local
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
        
            
            