import pygame
from sys import exit
from random import randint


class Bird(pygame.sprite.Sprite):
    def __init__(self) -> None:
        super().__init__()
        self.image = pygame.image.load('assets/Flappy.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(48,33.6))
        self.rect = self.image.get_rect(midright=(200,250))
        self.hit = pygame.mixer.Sound('sound/hit.mp3')
        self.point = pygame.mixer.Sound('sound/point.mp3')

    def animation(self):
        global x_speed, y_speed
        self.rect.x += x_speed
        self.rect.y += y_speed
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.hit.play()
            x_speed *= -1
        if self.rect.bottom >= 400 or self.rect.top <= 0:
            self.hit.play()
            y_speed *= -1

    def update(self) -> None:
        self.animation()
        for koin_rect in group_objek.sprites()[0].koin_list:
            if self.rect.colliderect(koin_rect):
                group_objek.sprites()[0].koin_list.remove(koin_rect)
                group_objek.sprites()[0].add_new_koin()
                self.point.play()


class Objek(pygame.sprite.Sprite):
    def __init__(self, tipe) -> None:
        super().__init__()
        if tipe == 'koin':
            self.image = pygame.image.load('assets/Koin.png')
            self.image = pygame.transform.scale(self.image, (18, 25.5))
            self.koin_list = []
            
            for i in range(30):
                koin_x_pos = randint(10, screen.get_width() - 10)
                koin_y_pos = randint(10, screen.get_height() - 10)
                self.rect = self.image.get_rect(center=(koin_x_pos, koin_y_pos))
                self.koin_list.append(self.rect)

        if tipe == 'pipe':
            self.image = pygame.image.load('assets/Pipe.png')
            self.image = pygame.transform.scale(self.image, (78,300))
            self.image_flip = pygame.transform.flip(self.image, True, False)
            self.pipa_list = []
            pipa_x_pos = 1000
            for i in range(5):
                pipa_y_pos = randint(100,275)
                self.pipa_up_rect = self.image.get_rect(topleft=(pipa_x_pos,pipa_y_pos))
                self.pipa_down_rect = self.image.get_rect(topleft=(pipa_x_pos,pipa_y_pos + 150))
                pipa_x_pos += 200
                self.pipa_list.append((self.pipa_up_rect,self.pipa_down_rect))
            
    
    def add_new_koin(self):
        koin_x_pos = randint(10, screen.get_width() - 10)
        koin_y_pos = randint(10, screen.get_height() - 10)
        self.rect = self.image.get_rect(center=(koin_x_pos, koin_y_pos))
        self.koin_list.append(self.rect)

    def update(self) -> None:
        for koin_rect in self.koin_list:
            screen.blit(self.image, koin_rect)

        for pipa_rect in self.pipa_list:
            screen.blit(self.image,pipa_rect)

            pipa_rect.x -= 3
            if pipa_rect.x <= 225:
                pipa_rect.x = 800
        

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('Flappy bird')
clock = pygame.time.Clock()

# Group
Flappy = pygame.sprite.GroupSingle()
Flappy.add(Bird())

group_objek = pygame.sprite.Group()
koin = Objek('koin')
group_objek.add(koin)

pipa = Objek('pipa')
group_objek.add(pipa)

# image
sky = pygame.image.load('assets/Sky.png')
sky = pygame.transform.scale(sky,(1570,442))

x_speed,y_speed = 5,5


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky,(0,0))

    Flappy.draw(screen)
    Flappy.update()

    group_objek.draw(screen,'koin')
    group_objek.update()

    group_objek.draw(screen,'pipe')
    group_objek.update()

    pygame.display.flip()
    clock.tick(60)