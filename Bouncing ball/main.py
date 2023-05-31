import pygame,sys
from setting import *

class Game:
    def __init__(self) -> None:
       pass

    def run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.fill((30,30,30))

        pygame.display.flip()
        clock.tick(60)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    pygame.display.set_caption('Bouncing ball')
    clock = pygame.time.Clock()

    game = Game()

    while True:
        game.run()

