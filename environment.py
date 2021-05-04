import pygame as pg
from game.game import Game
MOVE = 1000
def main():

    running = True
    playing = True

    pg.init()   
    pg.mixer.init()
    move_event = pg.USEREVENT + 1
    pg.time.set_timer(move_event, MOVE)
    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    clock = pg.time.Clock()

    # implement menus

    # implement game
    game = Game(screen, clock)

    while running:

        # start menu goes here

        while playing:
            # game loop here
            game.run(move_event)

if __name__ == "__main__":
    main()
