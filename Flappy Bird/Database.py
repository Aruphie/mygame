import pygame
from random import randint

pygame.init()

screen_width = 800
screen_height = 400
screen_size = (screen_width,screen_height)

screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption('Flappy Bird')

# pipa rand pos
pipa_y = []
for i in range(5):
    rand_pipa_y = randint(0,250)
    gap = rand_pipa_y + 125
    koin_y = rand_pipa_y + 50
    pipa_y.append((gap,rand_pipa_y,koin_y))

# text
score_menu = 0
score_main = 0
font = pygame.font.Font('assets/Pixel.ttf', 20)
text_score_menu = font.render(f"Score : {score_menu}", True, (255, 255, 255))
text_rect_menu = text_score_menu.get_rect(center=(100,30))
text_score_main = font.render(f"Score : {score_main}", True, (255, 255, 255))
text_rect_main = text_score_main.get_rect(center=(100,30))
text_game_over = font.render("GAME OVER", True, (255,255,255))
text_game_over_rect = text_game_over.get_rect(center=(200,200))


# image
menu = pygame.image.load('assets/Menu.png')
menu = pygame.transform.scale(menu,(360,180))
menu_rect = menu.get_rect(center=(400,150))

play_button = pygame.image.load('assets/Play_button.png')
play_button = pygame.transform.scale(play_button,(67.2,60.8))
play_button_rect = play_button.get_rect(center=(400,260))

restart = pygame.image.load('assets/Restart.png')
restart = pygame.transform.scale(restart,(67.2,60.8))
restart_rect = restart.get_rect(center=(400,260))

sky = pygame.image.load('assets/Sky.png')
sky = pygame.transform.scale(sky,(1570,442))
sky_rect = sky.get_rect(topleft=(0,0))

bird = pygame.image.load('assets/Flappy.png')
bird = pygame.transform.scale(bird,(48,33.6))
bird_rect_menu = bird.get_rect(midright=(400,250))
bird_rect = bird.get_rect(midright=(200,250))
flap = pygame.mixer.Sound('sound/flap.mp3')
die = pygame.mixer.Sound('sound/die.mp3')
hit = pygame.mixer.Sound('sound/hit.mp3')
point = pygame.mixer.Sound('sound/point.mp3')

koin = pygame.image.load('assets/Koin.png')
koin = pygame.transform.scale(koin,(18,25.5))

# koin rand pos
koin_list_menu = []
for i in range(20):
    rand_x_koin = randint(0, screen.get_width() - koin.get_width())
    rand_y_koin = randint(0, screen.get_height() - koin.get_height())
    koin_menu_rect = koin.get_rect(center=(rand_x_koin,rand_y_koin))
    koin_list_menu.append(koin_menu_rect)

koin_rect1 = koin.get_rect(topleft=(1025,pipa_y[0][2]))
koin_rect2 = koin.get_rect(topleft=(1225,pipa_y[1][2]))
koin_rect3 = koin.get_rect(topleft=(1425,pipa_y[2][2]))
koin_rect4 = koin.get_rect(topleft=(1625,pipa_y[3][2]))
koin_rect5 = koin.get_rect(topleft=(1825,pipa_y[4][2]))

pipa = pygame.image.load('assets/Pipe.png')
pipa = pygame.transform.scale(pipa,(78,300))
pipa_rect1 = pipa.get_rect(topleft=(1000,pipa_y[0][0]))
pipa_rect2 = pipa.get_rect(topleft=(1200,pipa_y[1][0]))
pipa_rect3 = pipa.get_rect(topleft=(1400,pipa_y[2][0]))
pipa_rect4 = pipa.get_rect(topleft=(1600,pipa_y[3][0]))
pipa_rect5 = pipa.get_rect(topleft=(1800,pipa_y[4][0]))

pipa_down = pygame.transform.flip(pipa,True,True)
pipa_down_rect1 = pipa_down.get_rect(bottomleft=(1000,pipa_y[0][1]))
pipa_down_rect2 = pipa_down.get_rect(bottomleft=(1200,pipa_y[1][1]))
pipa_down_rect3 = pipa_down.get_rect(bottomleft=(1400,pipa_y[2][1]))
pipa_down_rect4 = pipa_down.get_rect(bottomleft=(1600,pipa_y[3][1]))
pipa_down_rect5 = pipa_down.get_rect(bottomleft=(1800,pipa_y[4][1]))

pipes = [
    (pipa_rect1, pipa_down_rect1),
    (pipa_rect2, pipa_down_rect2),
    (pipa_rect3, pipa_down_rect3),
    (pipa_rect4, pipa_down_rect4),
    (pipa_rect5, pipa_down_rect5)
]

koins = [
    (koin_rect1,koin_rect2,koin_rect3,koin_rect4,koin_rect5),
    (koin_rect1,koin_rect2,koin_rect3,koin_rect4,koin_rect5),
]

image_rect_pairs = [
    (pipa, pipa_rect1), 
    (pipa, pipa_rect2),
    (pipa, pipa_rect3), 
    (pipa, pipa_rect4), 
    (pipa, pipa_rect5),
    (pipa_down,pipa_down_rect1),
    (pipa_down,pipa_down_rect2),
    (pipa_down,pipa_down_rect3),
    (pipa_down,pipa_down_rect4),
    (pipa_down,pipa_down_rect5),
]

gravity = 1
speed = 3
alpha = 0
animate_x = 5
animate_y = 5
index_koin = 0

bird_move_r = False
input_diterima = True
Game_start = False
Game_over = False
Menu_start = True
