import pygame
from sys import exit
from Database import *
from Function import *

pygame.init()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                Menu_start = False
                Game_start = True
            if event.button == 1 and Game_start and input_diterima:
                flap.play()
                gravity = -7 
        if event.type == pygame.KEYDOWN:       
            if event.key == pygame.K_SPACE and Menu_start and input_diterima:
                Menu_start = False
                Game_start = True
            if event.key == pygame.K_SPACE and Game_start and input_diterima:
                flap.play()
                gravity = -7

    # display
    screen.blit(sky,sky_rect)

    # Main menu
    if Menu_start:
        # score
        screen.blit(text_score_menu,text_rect_menu)
        text_score_menu = font.render(f"Score : {score_menu}", True, (255, 255, 255))

        # koin
        for koin_menu_rect in koin_list_menu.copy():
            if koin_menu_rect.colliderect(bird_rect_menu):
                koin_list_menu.remove(koin_menu_rect)
                score_menu += 1
                new_koin_menu()
                point.play()
            else:
                screen.blit(koin,koin_menu_rect)

        # animation
        bouncing()
        # menu
        main_menu()

    # Game start
    if Game_start:
        screen.blit(bird,bird_rect)
        
        for image, rect in image_rect_pairs:
            screen.blit(image, rect)

        for pipe in pipes:
            if (bird_rect.colliderect(pipe[0]) or bird_rect.colliderect(pipe[1])) and input_diterima:
                speed = 0
                die.play()
                gravity = -7
                input_diterima = False
                Game_start = False
                Menu_start = True

            elif pipe[0].x <= -225 and pipe[1].x <= -225:
                pipe[0].x,pipe[1].x = 800,800
            
            else :
                pipe[0].x -= speed
                pipe[1].x -= speed

        if (bird_rect.y >= 400 or bird_rect.y <= 0) and input_diterima:
            speed = 0
            gravity = -10
            die.play()
            input_diterima = False
            Game_start = False
            Menu_start = True

        gravity += 0.5
        bird_rect.y += gravity
        if bird_move_r:
            bird_rect.x += speed
            if bird_rect.x >= 200:
                bird_move_r = False

        screen.blit(text_score_main,text_rect_main)
        text_score_main = font.render(f"Score : {score_main}", True, (255, 255, 255))

    # Game Over :

        



    
    pygame.display.flip()
    clock.tick(60)

