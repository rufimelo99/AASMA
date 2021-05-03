import pygame as pg
import sys
from .world import World
from .settings import TILE_SIZE
from .settings import GRID_WIDTH
from .settings import GRID_HEIGHT
from .settings import BUILD_SIZE
from .utils import draw_text
from .camera import Camera
class Game:

    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()
        
        self.world = World(GRID_WIDTH, GRID_HEIGHT, self.width, self.height)

        self.width_materials = self.width * 0.65
        self.height_materials = self.height * 0.05
        self.camera = Camera(self.width, self.height)

    def run(self):
        self.playing = True
        
        while self.playing == True:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()
            
                
            
        
            
            

    def events(self): 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()

    def update(self):

        self.camera.update()
        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )


    def draw(self):
        self.screen.fill((0, 0, 0)) #background

        
        self.world.draw(self.screen, self.camera)

        draw_text(
            self.screen,
            'fps={}'.format(round(self.clock.get_fps())),
            25,
            (255, 255, 255),
            (10, 10)
        )



        pg.display.flip()


