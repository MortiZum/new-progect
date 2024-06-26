from pygame import *
import random

font.init()
screen = display.set_mode((800, 600))
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 800
dis_height = 600
dis = display.set_mode((dis_width, dis_height))
display.set_caption('sssssssss змея')
clock = time.Clock()
snake_block = 10
snake_speed = 10
font_style = font.SysFont("bahnschrift", 25)
score_font = font.SysFont("comicsansms", 35)
 
def Your_score(score):
   value = score_font.render("Ваш счёт: " + str(score), True, red)
   dis.blit(value, [0, 0])
 
def our_snake(snake_block, snake_list):
   for x in snake_list:
       draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])
 
def message(msg, color):
   mesg = font_style.render(msg, True, color)
   dis.blit(mesg, [dis_width / 6, dis_height / 3])
 

game_over = False
game_close = False
x1 = dis_width / 2
y1 = dis_height / 2
x1_change = 0
y1_change = 0
snake_List = []
Length_of_snake = 1
foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
while not game_over:
    if game_close == True:
        dis.fill(black)
        message("         Вы проиграли! Q-выход C-заново.", red)
        Your_score(Length_of_snake - 1)
        display.update()
        for e in event.get():
            if e.type == KEYDOWN:
                if e.key == K_q:
                    game_over = True
                    game_close = False
                if e.key == K_c:
                    game_close = False
                    x1 = 400
                    y1 = 300
                    y1_change = 0
                    x1_change = 0
    else:
        for e in event.get():
            if e.type == QUIT:
                game_over = True
            if e.type == KEYDOWN:
                if e.key == K_a:
                    x1_change = -snake_block
                    y1_change = 0
                elif e.key == K_d:
                    x1_change = snake_block
                    y1_change = 0
                elif e.key == K_w:
                    y1_change = -snake_block
                    x1_change = 0
                elif e.key == K_s:
                    y1_change = snake_block
                    x1_change = 0
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        display.update()
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
        clock.tick(snake_speed)

snake_speed
