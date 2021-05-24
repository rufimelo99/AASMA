import pygame as pg
from game.game import Game
MOVE = 1
SPAWN_PEOPLE = 50
COUNT = 1000


def draw_text(text, font, color, surface, x, y):
        

        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)
    


def menu(screen):

    width, height = screen.get_size()
    font = pg.font.SysFont(None, int(width/30))
        
    click = False
    while True:

        screen.fill((0,0,0))
        draw_text('main menu', font, (255, 255, 255), screen, 20, 20)

        mx, my = pg.mouse.get_pos()

        centers = [(width / 2, height / 5), (width / 2, 2 * height / 5), (width / 2, 3 * height / 5), (width / 2, 4 * height / 5)]

        size = (width / 3, height/10)


        button_1 = pg.Rect(50,100, size[0], size[1])
        button_1.center = centers[0]
        button_2 = pg.Rect(50,100, size[0], size[1])
        button_2.center = centers[1]
        button_3 = pg.Rect(50,100, size[0], size[1])
        button_3.center = centers[2]
        button_4 = pg.Rect(50,100, size[0], size[1])
        button_4.center = centers[3]

        if button_1.collidepoint((mx, my)):
            if click:
                return 0
        if button_2.collidepoint((mx, my)):
            if click:
                return 1
        if button_3.collidepoint((mx, my)):
            if click:
                return 2
        if button_4.collidepoint((mx, my)):
            if click:
                return 3
        pg.draw.rect(screen, (255, 0, 0), button_1)
        screen.blit(font.render('Random!', True, (0,0,255)), (centers[0][0] - (font.size("Random!")[0]/2), centers[0][1] - (font.size("Random!")[1]/2)))
        pg.draw.rect(screen, (255, 0, 0), button_2)
        screen.blit(font.render('Nearest!', True, (0,0,255)), (centers[1][0] - (font.size("Nearest!")[0]/2), centers[1][1] - (font.size("Nearest!")[1]/2)))
        pg.draw.rect(screen, (255, 0, 0), button_3)
        screen.blit(font.render('Learning!', True, (0,0,255)), (centers[2][0] - (font.size("Learning!")[0]/2), centers[2][1] - (font.size("Learning!")[1]/2)))
        pg.draw.rect(screen, (255, 0, 0), button_4)
        screen.blit(font.render('Communicating!', True, (0,0,255)), (centers[3][0] - (font.size("Communicating!")[0]/2), centers[3][1] - (font.size("Communicating!")[1]/2)))

        click = False
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    pg.quit()
                    sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pg.display.update()
    return 0







def main():

    running = True
    playing = True

    pg.init()   
    pg.mixer.init()
    move_event = pg.USEREVENT + 1
    spawn_event = pg.USEREVENT + 2
    count_event = pg.USEREVENT + 3
    pg.time.set_timer(move_event, MOVE)
    pg.time.set_timer(spawn_event, SPAWN_PEOPLE)
    pg.time.set_timer(count_event, COUNT)
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()
    
    
    

    # implement menus

    mode = menu(screen)
    # implement game
    game = Game(screen, clock, mode)
    

    while running:

        # start menu goes here

        while playing:
            # game loop here
            game.run(move_event,spawn_event,count_event,COUNT, MOVE,SPAWN_PEOPLE)

if __name__ == "__main__":
    main()
