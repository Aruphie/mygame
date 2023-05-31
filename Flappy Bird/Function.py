from Database import *
from random import randint


def bouncing():
    global animate_x, animate_y
    bird_rect_menu.x += animate_x
    bird_rect_menu.y += animate_y

    if bird_rect_menu.right >= screen_width or bird_rect_menu.left <= 0:
        animate_x *= -1
        hit.play()
    if bird_rect_menu.bottom >= screen_height or bird_rect_menu.top <= 0:
        animate_y *= -1
        hit.play()

def main_menu():
    screen.blit(bird,bird_rect_menu)
    screen.blit(menu,menu_rect)
    screen.blit(play_button,play_button_rect)
    
def new_koin_menu():
    rand_x_koin = randint(0, screen.get_width() - koin.get_width())
    rand_y_koin = randint(0, screen.get_height() - koin.get_height())
    koin_menu_rect = koin.get_rect(center=(rand_x_koin,rand_y_koin))
    koin_list_menu.append(koin_menu_rect)

def game_over(aplha):
    text_game_over.set_alpha(int(alpha))
    restart.set_alpha(int(alpha))
    screen.blit(text_game_over,text_game_over_rect)
    screen.blit(restart,restart_rect)


    
    