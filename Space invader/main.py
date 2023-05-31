import pygame,sys


class PLAYER(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect(midbottom=(screen_width/2,screen_height-10))
        # variable
        self.speed = 8

        # call laser sprite
        self.lasers = pygame.sprite.Group()
        

    
    def move(self,event): 
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rect.x += self.speed
        elif key[pygame.K_a]:
            self.rect.x -= self.speed
        elif key[pygame.K_SPACE]:
            self.laser_shoot()
        # if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
        #     self.laser_shoot()
    
    def laser_shoot(self):
        self.lasers.add(LASERS(self.rect.center))
        print(self.rect.center)

   
    def update(self) -> None:
        self.move(event)
        self.lasers.update()

class LASERS(pygame.sprite.Sprite):
    def __init__(self,pos) -> None:
        super().__init__()
        self.image = pygame.Surface((5,20))
        self.image.fill((0,0,0))
        self.rect = self.image.get_rect(center=pos)
        self.speed = 10
    
    def update(self):
        self.rect.y -= 9



pygame.init()
screen_width = 800
screen_height = 800
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('SPACE INVADER')
clock = pygame.time.Clock()

player = pygame.sprite.GroupSingle(PLAYER())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # else:
        #     player.update()
        #     pass
    
    screen.fill((50,50,50))

    player.draw(screen)
    player.sprite.lasers.draw(screen)
    player.update()

    pygame.display.flip()
    clock.tick(60)