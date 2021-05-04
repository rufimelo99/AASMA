import pygame as pg
from .settings import TILE_SIZE
from .settings import TILE_SIZE
from .settings import GRID_WIDTH
from .settings import GRID_HEIGHT
from .settings import BUILD_SIZE
from .car import Car

class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height
        
        self.width_materials = self.width * 0.65
        self.height_materials = self.height * 0.05
        print(self.width_materials)

        #self.grass_tiles = pg.Surface((width, height))
        self.list_Cars = []
        self.tiles = self.load_images()
        self.world = self.create_world()
    
    #def udpate_car(self, x, y, screen, camera, car):
        #render_pos =  self.world[x][y]["render_pos"]
        #screen.blit(self.tiles[car.orientation], (render_pos[0] + self.width_materials * 1.017 + camera.scroll.x, render_pos[1] + camera.scroll.y + self.height_materials))
    def new_caminho(self):
        if(self.list_Cars != []):
            for car in self.list_Cars:
                car.new_caminho()
    def update(self):
       if(self.list_Cars != []):
            for car in self.list_Cars:
                print(car.caminho)
                if(car.caminho != []):
                    new = car.caminho.pop(0)
                    car.update(new[0],new[1]) 

    
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
    

    def draw_car_x(self, x, y, screen, camera, car):
        render_pos =  self.world[x][y]["render_pos"]
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
                self.draw_car_x(car.position_x, car.position_y, screen, camera, car) 
        
        if(first == 0):
            car = Car(int(GRID_WIDTH*0.7) , 3)
            self.list_Cars.append(car)
            self.draw_car_x(int(GRID_WIDTH*0.7), 3, screen, camera, car)
        
        


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
        return {"block": block, "pavement": pavement, "road_x": road_x, "road_y": road_y,"road_24": road_24, "road_25": road_25,"road_26": road_26, "road_27": road_27,"road_33": road_33, "road_35": road_35, "hospital": hospital, "restaurant": restaurant, "market": market, "school": school, "skyscraper": skyscraper, "building" : building, "court": court, "taxi_NW": taxi_NW, "taxi_SE": taxi_SE, "taxi_SW": taxi_SW, "taxi_NE": taxi_NE}