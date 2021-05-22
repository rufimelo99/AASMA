import pygame as pg
from .settings import TILE_SIZE
from .settings import TILE_SIZE
from .settings import GRID_WIDTH
from .settings import GRID_HEIGHT
from .settings import BUILD_SIZE
from .car import Car
from .person import Person
from .GPS import GPS
from .carState import carState
import random

class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        
        self.width_materials = self.width * 0.65
        self.height_materials = self.height * 0.05

        #self.grass_tiles = pg.Surface((width, height))
        self.list_persons = []
        self.list_Cars = []
        self.tiles = self.load_images()
        self.world = self.create_world()
        self.GPS=GPS()
        self.locals = ['A', 'B', 'C', 'D', 'E', 'F', 'G']

        self.a = 0
        
        

        
    
    #def udpate_car(self, x, y, screen, camera, car):
        #render_pos =  self.world[x][y]["render_pos"]
        #screen.blit(self.tiles[car.orientation], (render_pos[0] + self.width_materials * 1.017 + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
    def new_caminho(self):
        if(self.list_Cars != []):
            for car in self.list_Cars:
                car.new_caminho()
    
    def update_car(self):
        copy_list_person = self.list_persons.copy()
        if(self.list_persons != []):
            for person in copy_list_person:
                for park in self.GPS.interestPointsDic[person.origem].closest_parking_lots:
                    if(self.GPS.interestPointsDic[park].cars != []):
                        car = self.GPS.interestPointsDic[park].cars.pop(0)
                        for i in range(len(self.GPS.interestPointsDic[park].parkingSpots)):
                            if(self.GPS.interestPointsDic[park].parkingSpots[i].Id == car.parkingSpotID):
                                    self.GPS.interestPointsDic[park].parkingSpots[i].available=True
                        if(park != person.origem):
                            car.caminho = self.GPS.interestPointsDic[park].paths[person.origem] + self.GPS.interestPointsDic[person.origem].paths[person.destino]
                        else:
                            car.caminho = self.GPS.interestPointsDic[park].paths[person.destino].copy()   
                        self.list_persons.remove(person)
                        car.setperson(person)
                        car.state = carState.OCCUPIED
                        car.local = person.destino
                        break
                        
                    
                    
        
        if(self.list_Cars != []):
            for car in self.list_Cars:
                if(car.caminho != []):
                    new = car.caminho.pop(0)
                    car.update(new[0],new[1]) 
                    if(car.person != None and car.state == carState.OCCUPIED):
                        if(car.person.cordenadas[0] == car.position_x and car.person.cordenadas[1] == car.position_y):
                            self.GPS.interestPointsDic[car.person.origem].numberpersons -= 1
                            
                
                elif(car.state == carState.OCCUPIED):
                    car.person = None
                    #car.selectRandomNewParkingLot(self.locals,self.GPS.interestPointsDic)
                    car.selectClosestParkingLot(self.GPS.interestPointsDic)
                   
                elif(car.state == carState.SEARCH_NEW_PARK):
                    parkingSpot = self.GPS.parkingLot(car.local)
                    if(parkingSpot != None):
                        parkingSpot.available = False
                        car.parkingSpotID =  parkingSpot.Id
                        car.position_x = parkingSpot.posX
                        car.position_y =  parkingSpot.posY
                        car.state = carState.FREE
                        self.GPS.interestPointsDic[car.local].cars.append(car)
                    else:
                        if(car.selectClosestParkingLot2(self.GPS.interestPointsDic)):
                            None
                        else:
                            car.selectRandomNewParkingLot(self.locals,self.GPS.interestPointsDic)

                        #car.selectRandomNewParkingLot(self.locals,self.GPS.interestPointsDic)

                        


                        
                    


    def generate_person(self):
        pessoas = 0
        ticketA = int(random.random() * 99) + 1 
        ticketB = int(random.random() * 99) + 1 
        ticketC = int(random.random() * 99) + 1 
        ticketD = int(random.random() * 99) + 1 
        ticketE = int(random.random() * 99) + 1 
        ticketF = int(random.random() * 99) + 1 
        ticketG = int(random.random() * 99) + 1
        
        if(ticketA <= 30):
            pessoas += 1
            print("A")
            destino = new_local = random.choice(self.locals)
            while(destino == 'A'):
                destino = new_local = random.choice(self.locals)
            
            print(destino)
            personA = Person('A','B',[10,3])
            self.GPS.interestPointsDic['A'].numberpersons += 1
            self.list_persons.append(personA)
        '''
        if(ticketB <= 40):
            pessoas += 1
            print("B")
            destino = new_local = random.choice(self.locals)
            while(destino == 'B'):
                destino = new_local = random.choice(self.locals)
            print(destino)
            personB = Person('B',destino,[3,10])
            self.GPS.interestPointsDic['B'].numberpersons += 1
            self.list_persons.append(personB)
        '''
        
        

        
        if(ticketC <= 20):
            pessoas += 1
            print("C")
            destino = new_local = random.choice(self.locals)
            while(destino == 'C'):
                destino = new_local = random.choice(self.locals)
            
            print(destino)
            personC = Person('C','B',[3,26])
            self.GPS.interestPointsDic['C'].numberpersons += 1
            self.list_persons.append(personC)
            
        

        
        
        if(ticketD <= 50):
            pessoas += 1
            print("D")
            destino = new_local = random.choice(self.locals)
            while(destino == 'D'):
                destino = new_local = random.choice(self.locals)
            
            print(destino)
            personD = Person('D','B',[10,32])
            self.GPS.interestPointsDic['D'].numberpersons += 1
            self.list_persons.append(personD)
        
        if(ticketE <= 100):
            pessoas += 1
            print("E")
            destino = new_local = random.choice(self.locals)
            while(destino == 'E'):
                destino = new_local = random.choice(self.locals)
            
            print(destino)
            personE = Person('E','B',[14,23])
            self.GPS.interestPointsDic['E'].numberpersons += 1
            self.list_persons.append(personE)
        
        if(ticketF <= 5):
            pessoas += 1
            print("F")
            destino = new_local = random.choice(self.locals)
            while(destino == 'F'):
                destino = new_local = random.choice(self.locals)
            
            print(destino)
            personF = Person('F','B',[14,9])
            self.GPS.interestPointsDic['F'].numberpersons += 1
            self.list_persons.append(personF)
            
        if(ticketG <= 20):
            pessoas += 1
            print("G")
            destino = new_local = random.choice(self.locals)
            while(destino == 'G'):
                destino = new_local = random.choice(self.locals)
            
            print(destino);
            personG = Person('G','B',[9,17])
            self.GPS.interestPointsDic['G'].numberpersons += 1
            self.list_persons.append(personG)
            
        
        print(pessoas)
        
        
        
    
    
    def draw_people(self, screen, camera):
        
        for i in self.GPS.interestPointsDic:
            if(self.GPS.interestPointsDic[i].numberpersons > 0):
                if(self.GPS.interestPointsDic[i].Id == 'A'):
                    x = 11
                    y = 1
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["man"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))
                elif(self.GPS.interestPointsDic[i].Id == 'B'):
                    x = 2
                    y = 8
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["basicman"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))
                elif(self.GPS.interestPointsDic[i].Id == 'C'):
                    x = 2
                    y = 24
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["basicman"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))   
                elif(self.GPS.interestPointsDic[i].Id == 'D'):
                    x = 9
                    y = 30
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["man"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))
                elif(self.GPS.interestPointsDic[i].Id == 'E'):
                    x = 13
                    y = 23
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["basicman"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))
                elif(self.GPS.interestPointsDic[i].Id == 'F'):
                    x = 13
                    y = 9
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["basicman"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))
                elif(self.GPS.interestPointsDic[i].Id == 'G'):
                    x = 8
                    y = 15
                    render_pos =  self.world[x][y]["render_pos"]
                    screen.blit(self.tiles["man"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["man"].get_height() - TILE_SIZE))* 1.2))  
        

        


    
    def draw_road_x(self, x_initial, x_final, y, screen, camera):
        for x in range(x_initial, x_final):
            render_pos =  self.world[x][y]["render_pos"]
            screen.blit(self.tiles["road_y"], (render_pos[0] + self.width_materials + camera.scroll.x , render_pos[1] + camera.scroll.y + self.height_materials))
            

    def draw_road_y(self, y_initial, y_final, x, screen, camera):
        if(x < GRID_WIDTH/2):
            render_pos =  self.world[x][y_initial-1]["render_pos"]
            screen.blit(self.tiles["road_26"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
            render_pos =  self.world[x][y_final]["render_pos"]
            screen.blit(self.tiles["road_24"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
        else:
            render_pos =  self.world[x][y_initial-1]["render_pos"]
            screen.blit(self.tiles["road_25"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
            render_pos =  self.world[x][y_final]["render_pos"]
            screen.blit(self.tiles["road_27"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
        
        for y in range(y_initial, y_final):
            if(y == ((GRID_HEIGHT/2)-1) and x < GRID_WIDTH/2):
                render_pos =  self.world[x][y]["render_pos"]
                screen.blit(self.tiles["road_35"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
            elif(y == ((GRID_HEIGHT/2)-1) and x > GRID_WIDTH/2):
                render_pos =  self.world[x][y]["render_pos"]
                screen.blit(self.tiles["road_33"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
            else:        
                render_pos =  self.world[x][y]["render_pos"]
                screen.blit(self.tiles["road_x"], (render_pos[0] + self.width_materials + camera.scroll.x , render_pos[1] + camera.scroll.y + self.height_materials))
    

    def draw_car_x(self, screen, camera, car):
        render_pos =  self.world[car.position_x][car.position_y]["render_pos"]
        screen.blit(self.tiles[car.orientation], (render_pos[0] + self.width_materials * 1.017 + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
    def draw(self, screen, camera, first):
        #screen.blit(self.world.grass_tiles, (0, 0))

        for x in range(self.grid_length_x):
            for y in range(self.grid_length_y):

                #sq = self.world.world[x][y]["cart_rect"]
                #rect = pg.Rect(sq[0][0], sq[0][1], TILE_SIZE, TILE_SIZE)
                #pg.draw.rect(screen, (0, 0, 255), rect, 1)
                

                render_pos =  self.world[x][y]["render_pos"]
                screen.blit(self.tiles["block"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + self.height_materials + camera.scroll.y))
                if( x == int(GRID_WIDTH*0.7) and y == 3):
                    screen.blit(self.tiles["hospital"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]  + camera.scroll.y + (self.height_materials - (self.tiles["hospital"].get_height() - TILE_SIZE))* 1.3))
                if( x == 1 and y == int(GRID_HEIGHT*0.3)):
                    screen.blit(self.tiles["restaurant"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + (self.height_materials - (self.tiles["restaurant"].get_height() - TILE_SIZE))* 1.4))
                if( x == int(GRID_WIDTH*0.5) and y == int(GRID_HEIGHT*0.46)):
                    screen.blit(self.tiles["market"], (render_pos[0] + self.width_materials + camera.scroll.x , render_pos[1] + camera.scroll.y + (self.height_materials - (self.tiles["market"].get_height() - TILE_SIZE))* 3))
                if( x == 1 and y == int(GRID_HEIGHT*0.8)):
                    screen.blit(self.tiles["school"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + (self.height_materials - (self.tiles["school"].get_height() - TILE_SIZE))* 1.3))
                if( x == int(GRID_WIDTH*0.5) and y == int(GRID_HEIGHT*0.87)):
                    screen.blit(self.tiles["skyscraper"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1]+ camera.scroll.y + (self.height_materials - (self.tiles["skyscraper"].get_height() - TILE_SIZE))* 1.1))
                if( x == int(GRID_WIDTH*0.7) and y == int(GRID_HEIGHT*0.72)):
                    screen.blit(self.tiles["building"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + (self.height_materials - (self.tiles["building"].get_height() - TILE_SIZE))* 1.1))
                if( x == int(GRID_WIDTH*0.7) and y == int(GRID_HEIGHT*0.35)):
                    screen.blit(self.tiles["court"], (render_pos[0] + self.width_materials + camera.scroll.x, render_pos[1] + camera.scroll.y + (self.height_materials - (self.tiles["court"].get_height() - TILE_SIZE))* 1.4))
                
                

                #p = self.world[x][y]["iso_poly"]
                #p = [(x + self.width_materials, y + self.height_materials) for x, y in p] #change position grid
                #pg.draw.polygon(screen, (0, 0, 255), p, 1)

    

        self.draw_road_x(4, GRID_WIDTH-4, 3, screen, camera)
        self.draw_road_x(4, GRID_WIDTH-4, GRID_HEIGHT-4, screen, camera)
        self.draw_road_x(4, GRID_WIDTH-4, int((GRID_HEIGHT/2)-1), screen, camera)
        self.draw_road_y(4, GRID_HEIGHT-4, 3, screen, camera)
        self.draw_road_y(4, GRID_HEIGHT-4, GRID_WIDTH-4, screen, camera)

        
        if(self.list_Cars != []):
            for car in self.list_Cars:
                self.draw_car_x(screen, camera, car)
        
        if(self.people()):
            self.draw_people(screen, camera)
        
        if(first == 0):
            '''
            carteste1 = Car(1, 0, 5, 'B', 0)
            self.GPS.interestPointsDic['B'].cars.append(carteste1)
            for i in range(len(self.GPS.interestPointsDic['B'].parkingSpots)):
                if(self.GPS.interestPointsDic['B'].parkingSpots[i].Id == 0):
                    self.GPS.interestPointsDic['B'].parkingSpots[i].available=False

            carteste2 = Car(2, 15, 23, 'E', 0)
            self.GPS.interestPointsDic['E'].cars.append(carteste2)
            for i in range(len(self.GPS.interestPointsDic['E'].parkingSpots)):
                if(self.GPS.interestPointsDic['E'].parkingSpots[i].Id == 0):
                    self.GPS.interestPointsDic['E'].parkingSpots[i].available=False
            
            self.list_Cars.append(carteste1)
            self.list_Cars.append(carteste2)
            self.draw_car_x(screen, camera, carteste1)
            self.draw_car_x(screen, camera, carteste2)
            '''
            
            
            car = Car(1, 10 , 18, 'G', 0)
            self.GPS.interestPointsDic['G'].cars.append(car)
            for i in range(len(self.GPS.interestPointsDic['G'].parkingSpots)):
                if(self.GPS.interestPointsDic['G'].parkingSpots[i].Id == 0):
                    self.GPS.interestPointsDic['G'].parkingSpots[i].available=False

            car2 = Car(2, 6, 0, 'A', 0)
            self.GPS.interestPointsDic['A'].cars.append(car2)
            for i in range(len(self.GPS.interestPointsDic['A'].parkingSpots)):
                if(self.GPS.interestPointsDic['A'].parkingSpots[i].Id == 0):
                    self.GPS.interestPointsDic['A'].parkingSpots[i].available=False
            
            car3 = Car(3, 0, 19, 'C', 0)
            self.GPS.interestPointsDic['C'].cars.append(car3)
            for i in range(len(self.GPS.interestPointsDic['C'].parkingSpots)):
                if(self.GPS.interestPointsDic['C'].parkingSpots[i].Id == 0):
                    self.GPS.interestPointsDic['C'].parkingSpots[i].available=False
            
            
            car4 = Car(4, 15, 23, 'D', 0)
            self.GPS.interestPointsDic['D'].cars.append(car4)
            for i in range(len(self.GPS.interestPointsDic['D'].parkingSpots)):
                if(self.GPS.interestPointsDic['D'].parkingSpots[i].Id == 0):
                    self.GPS.interestPointsDic['D'].parkingSpots[i].available=False

            car5 = Car(5, 7, 0, 'A', 0)
            self.GPS.interestPointsDic['A'].cars.append(car5)
            for i in range(len(self.GPS.interestPointsDic['A'].parkingSpots)):
                if(self.GPS.interestPointsDic['A'].parkingSpots[i].Id == 1):
                    self.GPS.interestPointsDic['A'].parkingSpots[i].available=False

            self.list_Cars.append(car)
            self.list_Cars.append(car2)
            self.list_Cars.append(car3)
            self.list_Cars.append(car4)
            self.list_Cars.append(car5)
            self.draw_car_x(screen, camera, car)
            self.draw_car_x(screen, camera, car2)
            self.draw_car_x(screen, camera, car3)
            self.draw_car_x(screen, camera, car4)
            self.draw_car_x(screen, camera, car5)
            
            
        
        

    def people(self):
        for i in self.GPS.interestPointsDic:
            if(self.GPS.interestPointsDic[i].numberpersons > 0):
                return True
        return False
    def create_world(self):

        world = []

        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

                #render_pos = world_tile["render_pos"]
                #self.grass_tiles.blit(self.tiles["block"], (render_pos[0] + self.width_materials, render_pos[1] + self.height_materials))
        
        return world
    
    def grid_to_world(self, grid_x, grid_y):

        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]

        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        minx = min([x for x, y in iso_poly])
        miny = min([y for x, y in iso_poly])

    

        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx, miny]
        }

        

        return out
    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):
        block = pg.image.load("assets/block.png").convert_alpha()
        pavement = pg.image.load("assets/pavement.png").convert_alpha()
        court = pg.image.load("assets/court.png").convert_alpha()
        building = pg.image.load("assets/building.png").convert_alpha()
        hospital = pg.image.load("assets/hospital.png").convert_alpha()
        restaurant = pg.image.load("assets/restaurant.png").convert_alpha()
        skyscraper = pg.image.load("assets/skyscraper.png").convert_alpha()
        market = pg.image.load("assets/market.png").convert_alpha()
        school = pg.image.load("assets/school.png").convert_alpha()
        road_x = pg.image.load("assets/road-20.png").convert_alpha()
        road_y = pg.image.load("assets/road-21.png").convert_alpha()
        road_24 = pg.image.load("assets/road-24.png").convert_alpha()
        road_25 = pg.image.load("assets/road-25.png").convert_alpha()
        road_26 = pg.image.load("assets/road-26.png").convert_alpha()
        road_27 = pg.image.load("assets/road-27.png").convert_alpha()
        road_33 = pg.image.load("assets/road-33.png").convert_alpha()
        road_35 = pg.image.load("assets/road-35.png").convert_alpha()
        taxi_NW = pg.image.load("assets/taxi_NW.png").convert_alpha()
        taxi_SE = pg.image.load("assets/taxi_SE.png").convert_alpha()
        taxi_SW = pg.image.load("assets/taxi_SW.png").convert_alpha()
        taxi_NE = pg.image.load("assets/taxi_NE.png").convert_alpha()
        man = pg.image.load("assets/man.png").convert_alpha()
        basicman = pg.image.load("assets/basicman.png").convert_alpha()
        return {"block": block, "pavement": pavement, "road_x": road_x, "road_y": road_y,"road_24": road_24, "road_25": road_25,"road_26": road_26, "road_27": road_27,"road_33": road_33, "road_35": road_35, "hospital": hospital, "restaurant": restaurant, "market": market, "school": school, "skyscraper": skyscraper, "building" : building, "court": court, "taxi_NW": taxi_NW, "taxi_SE": taxi_SE, "taxi_SW": taxi_SW, "taxi_NE": taxi_NE, "man": man, "basicman": basicman}