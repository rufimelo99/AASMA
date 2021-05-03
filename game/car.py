
from .settings import GRID_HEIGHT
from .settings import GRID_WIDTH

class Car:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
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
        
        


    def update_x(self, x):
        self.position_x = x
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
        
    def update_y(self, y):
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
            
            