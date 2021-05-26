import pygame as pg
import sys
import seaborn as sns
import matplotlib.pyplot as plt
from .world import World
from .settings import TILE_SIZE
from .settings import GRID_WIDTH
from .settings import GRID_HEIGHT
from .settings import BUILD_SIZE
from .settings import FPS
from .utils import draw_text
from .camera import Camera
from .hud import Hud

import time

class Game:

    def __init__(self, screen, clock, mode):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.hud = Hud(self.width,self.height)
        self.mode = mode
        self.world = World(GRID_WIDTH, GRID_HEIGHT, self.width, self.height,self.hud,self.mode)
        self.pause = False
        self.width_materials = self.width * 0.65
        self.height_materials = self.height * 0.05
        self.camera = Camera(self.width, self.height)
        

    def run(self,move_event,spawn_event,count_event,count,move,spawnPeople):
        self.move = move
        self.spawnPeople = spawnPeople
        self.playing = True
        self.move_event = move_event
        self.spawn_event = spawn_event
        self.count_envet = count_event
        x = 0
        time_elapsed_since_last_action1 = 0
        time_elapsed_since_last_action2 = 0
        time_elapsed_since_last_action3 = 0
        while self.playing == True:
            self.dt = self.clock.tick(FPS)
            '''
            time_elapsed_since_last_action1 += self.dt
            time_elapsed_since_last_action2 += self.dt
            time_elapsed_since_last_action3 += self.dt
            if time_elapsed_since_last_action1 > 100:
                self.world.update_car(self.move)
                time_elapsed_since_last_action1 = 0
            
            if time_elapsed_since_last_action2 > 3000:
                self.world.generate_person()
                time_elapsed_since_last_action2 = 0
            
            if time_elapsed_since_last_action3 > 1000:
                self.world.add()
                time_elapsed_since_last_action3 = 0
            '''
            self.events()
            self.update()
            self.draw(x)
            x = 1
            
                
            
        
            
            

    def events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
                if event.key == pg.K_p:
                    self.pause = True
                    self.paused()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_0:
                    self.world.new_caminho()
                if event.key == pg.K_9:
                    self.world.q_values()
                if event.key == pg.K_x:
                    self.plot()
            if event.type == self.move_event:
                self.world.update_car(self.move)
            if event.type == self.spawn_event:
                self.world.generate_person()
            if(event.type == self.count_envet):
                self.world.add()
                

    def update(self):

        self.camera.update()
    
    def plot(self):
        
        
        
        f = open('communicationplot_teste2.py', 'w+')
        f.write('communication_times = [')
        for i in range(len(self.world.times) - 1):
            f.write(str(self.world.times[i]) + ', ')

        f.write(str(self.world.times[-1]))
        f.write(']\n')

        f.write('communication_times_total = [')
        for i in range(len(self.world.wait_list) - 1):
            f.write(str(self.world.wait_list[i]) + ', ')

        f.write(str(self.world.wait_list[-1]))
        f.write(']\n')

        f.write('communication_path_length_client = [')
        for i in range(len(self.world.all_cars_path_to_client) - 1):
            f.write(str(self.world.all_cars_path_to_client[i]) + ', ')

        f.write(str(self.world.all_cars_path_to_client[-1]))
        f.write(']\n')

        f.write('communication_path_length_park = [')
        for i in range(len(self.world.all_cars_path_to_park) - 1):
            f.write(str(self.world.all_cars_path_to_park[i]) + ', ')

        f.write(str(self.world.all_cars_path_to_park[-1]))
        f.write(']\n')

        f.write('communication_time_avalable = [')
        for i in range(len(self.world.all_cars_wait_time_client) - 1):
            f.write(str(self.world.all_cars_wait_time_client[i]) + ', ')

        f.write(str(self.world.all_cars_wait_time_client[-1]))
        f.write(']\n')

        
        

        

        f.close()
        
        plt.show()

    def paused(self):
        while self.pause:
            for event in pg.event.get():
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_p:
                        self.pause = False
                    if event.key == pg.K_ESCAPE:
                        pg.quit()
                        sys.exit()
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()


    def draw(self,x):
        self.screen.fill((0, 0, 0)) #background

        
        self.world.draw(self.screen, self.camera,x)


        
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )



        pg.display.flip()


