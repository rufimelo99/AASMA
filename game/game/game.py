import pygame as pg
import sys
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

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        self.hud = Hud(self.width,self.height)
        self.world = World(GRID_WIDTH, GRID_HEIGHT, self.width, self.height)
        self.pause = False
        self.width_materials = self.width * 0.65
        self.height_materials = self.height * 0.05
        self.camera = Camera(self.width, self.height)

    def run(self,move_event,spawn_event):
        self.playing = True
        self.move_event = move_event
        self.spawn_event = spawn_event
        x = 0
        while self.playing == True:
            self.dt = self.clock.tick(FPS) / 1000
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
            if event.type == self.move_event:
                self.world.update_car()
            if event.type == self.spawn_event:
    
                self.world.generate_person()
                

    def update(self):

        self.camera.update()

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


        self.hud.draw(self.screen)
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )



        pg.display.flip()

