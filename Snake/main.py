import pygame,sys,random
from pygame.math import Vector2

class SNAKE:
    def __init__(self) -> None:
        self.reset()

        # Head
        self.head_up = pygame.image.load('assets/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('assets/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('assets/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('assets/head_right.png').convert_alpha()
        # Body
        self.body_bl = pygame.image.load('assets/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('assets/body_br.png').convert_alpha()
        self.body_tl = pygame.image.load('assets/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('assets/body_tr.png').convert_alpha()
        self.body_horizontal = pygame.image.load('assets/body_horizontal.png').convert_alpha()
        self.body_vertical = pygame.image.load('assets/body_vertical.png').convert_alpha()
        # Head
        self.tail_up = pygame.image.load('assets/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('assets/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('assets/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('assets/tail_right.png').convert_alpha()
    
    def draw(self):
        self.graphic()
        for index,block in enumerate(self.body):
            self.pos = Vector2(block.x,block.y)
            self.rect = pygame.Rect(self.pos.x*cell_size,self.pos.y*cell_size,cell_size,cell_size)
            if index == 0:
                screen.blit(self.head,self.rect)
            elif index == len(self.body) -1:
                screen.blit(self.tail,self.rect)
            else:
                prev_block = self.body[index + 1] - block
                next_block = self.body[index - 1] - block
                if prev_block.x == next_block.x:
                    screen.blit(self.body_vertical,self.rect)
                elif prev_block.y == next_block.y:
                    screen.blit(self.body_horizontal,self.rect)
                else:
                    if prev_block.x == -1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == -1:
                        screen.blit(self.body_tl,self.rect)
                    if prev_block.x == 1 and next_block.y == -1 or prev_block.y == -1 and next_block.x == 1:
                        screen.blit(self.body_tr,self.rect)
                    if prev_block.x == -1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == -1:
                        screen.blit(self.body_bl,self.rect)
                    if prev_block.x == 1 and next_block.y == 1 or prev_block.y == 1 and next_block.x == 1:
                        screen.blit(self.body_br,self.rect)

    def graphic(self):
        # head
        head_direction = self.body[1]-self.body[0]
        if head_direction.y == 1: self.head = self.head_up
        if head_direction.y == -1: self.head = self.head_down
        if head_direction.x == 1: self.head = self.head_left
        if head_direction.x == -1: self.head = self.head_right
        # tail
        tail_direction = self.body[-2]-self.body[-1]
        if tail_direction.y == 1: self.tail = self.tail_up
        if tail_direction.y == -1: self.tail = self.tail_down
        if tail_direction.x == 1: self.tail = self.tail_left
        if tail_direction.x == -1: self.tail = self.tail_right

    def move(self):
        if self.start:
            if self.grow :
                body_copy = self.body[:]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy
                self.grow = False
            else:
                body_copy = self.body[:-1]
                body_copy.insert(0,body_copy[0] + self.direction)
                self.body = body_copy

    def animation(self):
        self.direction = Vector2(1,0)
        body_copy = self.body[:-1]
        body_copy.insert(0,body_copy[0] + self.direction)
        self.body = body_copy

        if self.body[-1].x > cell_amount-2:
            self.body[0].x = -1   


    def reset(self):
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(0,0)
        self.grow = False
        self.start = False
    

class FRUIT:
    def __init__(self) -> None:
        self.randomize()

    def draw(self):
        self.rect = pygame.Rect(self.x,self.y,cell_size,cell_size)
        screen.blit(apple,self.rect)

    def randomize(self):
        x = random.randint(0,cell_amount-1)
        y = random.randint(0,cell_amount-1)
        self.pos = Vector2(x,y)
        self.x = self.pos.x*cell_size
        self.y = self.pos.y*cell_size


class GAME:
    def __init__(self) -> None:
        self.snake = SNAKE()
        self.fruit = FRUIT()
    
    def grass(self):
        color = (167,209,61)
        for row in range(cell_amount):
            if row % 2 != 0:
                for col in range(cell_amount):
                    if col % 2 == 0 :
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,color,grass_rect,cell_size)
            else:
                for col in range(cell_amount):
                    if col % 2 != 0 :
                        grass_rect = pygame.Rect(col*cell_size,row*cell_size,cell_size,cell_size)
                        pygame.draw.rect(screen,color,grass_rect,cell_size)

    def score_bar(self):
        score = str(len(self.snake.body)-3)
        score_text = font_game.render(score,True,(50,50,50))
        score_rect = pygame.Rect(50,10,cell_size,cell_size)
        apple_rect = apple.get_rect(midright=(score_rect.left,score_rect.centery))
        border_rect = pygame.Rect(apple_rect.left,apple_rect.top,score_rect.x+len(score)*16+7,apple_rect.height)

        pygame.draw.rect(screen,(167,209,61),border_rect,border_radius=5)
        pygame.draw.rect(screen,(50,50,50),border_rect,2,5)
        screen.blit(score_text,score_rect)
        screen.blit(apple,apple_rect)
    
    def collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize()
            self.snake.grow = True
            crunch.play()
        if not 0 <= self.snake.body[0].x < cell_amount or not 0 <= self.snake.body[0].y < cell_amount:
            self.snake.reset()
            die.play()
        for body in self.snake.body[1:]:
            if self.snake.body[0] == body:
                self.snake.reset()
                hit.play()

    def update(self):
        self.snake.move()
        self.collision()

        
class MENU:
    def __init__(self) -> None:
        self.snake = SNAKE()
        self.direction = Vector2(1,0)
        self.fruit = FRUIT()
        self.menu_title = font_title.render('PYTHON SNAKE',True,(50,50,50))
        self.menu_desk = font_desk.render('Click anywhere to start',True,(50,50,50))
        self.menu_rect = pygame.Rect(3*cell_size,cell_size,12*cell_size,2*cell_size)

    def draw(self):
        pygame.draw.rect(screen,(167,209,61),self.menu_rect,)
        pygame.draw.rect(screen,(50,50,50),self.menu_rect,5,20)
        screen.blit(self.menu_title,(4*cell_size+28,cell_size+5))
        screen.blit(self.menu_desk,(4*cell_size,15*cell_size))
        screen.blit(apple,(10*cell_size,10*cell_size))
        screen.blit(python,(7*cell_size+20,4*cell_size+20))
        self.snake.draw()

    def update(self):
        self.snake.animation()


pygame.init()
cell_size = 40
cell_amount = 18
screen = pygame.display.set_mode((cell_amount*cell_size,cell_amount*cell_size))
clock = pygame.time.Clock()

font_desk = pygame.font.Font(None,50)
font_title = pygame.font.Font('assets/PoetsenOne.ttf',50)
font_game = pygame.font.Font('assets/PoetsenOne.ttf',32)
apple = pygame.image.load('assets/apple.png').convert_alpha()
python = pygame.image.load('assets/python.png').convert_alpha()
python = pygame.transform.scale(python,(3*cell_size,3*cell_size))
hit = pygame.mixer.Sound('assets/hit.mp3')
die = pygame.mixer.Sound('assets/die.mp3')
crunch = pygame.mixer.Sound('assets/crunch.wav')

menu_start = True
game_start = False

game = GAME()
menu = MENU()

SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,150)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == SCREEN_UPDATE:
            game.update()
            menu.update()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                game_start = True
                menu_start = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and game.snake.direction.y != 1:
                game.snake.direction = Vector2(0,-1)
                game.snake.start = True
            if event.key == pygame.K_a and game.snake.direction.x != 1:
                game.snake.direction = Vector2(-1,0)
                game.snake.start = True
            if event.key == pygame.K_s and game.snake.direction.y != -1:
                game.snake.direction = Vector2(0,1)
                game.snake.start = True
            if event.key == pygame.K_d and game.snake.direction.x != -1:
                game.snake.direction = Vector2(1,0)
                game.snake.start = True
    
    # screen
    screen.fill((175,215,70))
    text_start = font_desk.render("Click 'W/A/S/D' to play!",True,(50,50,50))

    if menu_start:
        game.grass()
        menu.draw()

    # game
    if game_start:
        if not game.snake.start:
            game.grass()
            game.fruit.draw()
            game.snake.draw()
            game.score_bar()
            screen.blit(text_start,(4*cell_size,15*cell_size))
        else:
            game.grass()
            game.fruit.draw()
            game.snake.draw()
            game.score_bar()

    pygame.display.flip()
    clock.tick(60)