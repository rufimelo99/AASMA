import pygame as pg
from .utils import draw_text


class Hud:

    def __init__(self, width, height):
        self.width = width
        self.height = height


        self.hud_colour = (198, 155, 93, 175)


        self.car_surface = pg.Surface((width * 0.5, height * 0.2), pg.SRCALPHA)
        self.car_surface.fill(self.hud_colour)

        self.images = self.load_images()


    def draw(self,carlist, screen,meanwaitimepersons):



        

        screen.blit(self.car_surface, (self.width * 0.5 , self.height * 0.8))
        

        posx = self.width * 0.5 
        posy = self.height * 0.8
        for resource in ["id:", "park:","  nº of trips","mean wait time", "    mean path to client","     mean path to park", "         trips/unit"]:
            draw_text(screen, resource, 25, (255, 255, 255), (posx, posy))
            posx = posx * 1.1
        
        posx = self.width * 0.5 
        posy = posy * 1.04
        for car in carlist:
            for i in range(7):
                if(i == 0):
                    draw_text(screen, " " + str(car.id), 25, (255, 255, 255), (posx, posy))
                    posx = posx * 1.1
                elif(i == 1):
                    draw_text(screen, "   " + str(car.local), 25, (255, 255, 255), (posx, posy))
                    posx = posx * 1.1
                elif(i == 2):
                    draw_text(screen, "       " + str(car.numberOfTrips) , 25, (255, 255, 255), (posx, posy))
                    posx = posx * 1.1
                elif(i == 3):
                    draw_text(screen, "            " + str(round(car.meanWaitime,2)) , 25, (255, 255, 255), (posx, posy))
                    posx = posx * 1.1
                elif(i == 4):
                    draw_text(screen, "                   " + str(round(car.meanlengthpathClient,2)) , 25, (255, 255, 255), (posx, posy))
                    posx = posx * 1.1
                elif(i == 5):
                    draw_text(screen, "                   " + str(round(car.meanpathtoparkinglot,2)) , 25, (255, 255, 255), (posx, posy))
                    posx = posx * 1.1
                else:
                    draw_text(screen, "          " + str(round(car.tripsPerTimeUnit,2)) , 25, (255, 255, 255), (posx, posy)) 
            posx = self.width * 0.5 
            posy = posy * 1.04
        
        posx = self.width * 0.9
        posy = self.height *0.1

        draw_text(screen,str(meanwaitimepersons) , 25, (255, 255, 255), (posx, posy))

    

    def scale_image(self, image, w=None, h=None):
    
        if (w == None) and (h == None):
            pass
        elif h == None:
            scale = w / image.get_width()
            h = scale * image.get_height()
            image = pg.transform.scale(image, (int(w), int(h)))
        elif w == None:
            scale = h / image.get_height()
            w = scale * image.get_width()
            image = pg.transform.scale(image, (int(w), int(h)))
        else:
            image = pg.transform.scale(image, (int(w), int(h)))

        return image

    def load_images(self):
        taxi_NW = pg.image.load("assets/taxi_NW.png").convert_alpha()
        taxi_SE = pg.image.load("assets/taxi_SE.png").convert_alpha()
        taxi_SW = pg.image.load("assets/taxi_SW.png").convert_alpha()
        taxi_NE = pg.image.load("assets/taxi_NE.png").convert_alpha()
        return {"taxi_NW": taxi_NW, "taxi_SE": taxi_SE, "taxi_SW": taxi_SW, "taxi_NE": taxi_NE}