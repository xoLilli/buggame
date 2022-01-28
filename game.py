
#colors
white = (255,255,255)
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
black = (0,0,0)
orange = (255,100,10)
yellow = (255,255,0)
blue_green = (0,255,170)
marroon = (115,0,0)
lime = (180,255,100)
pink = (255,100,180)
purple = (240,0,255)
gray = (127,127,127)
magenta = (255,0,230)
brown = (100,40,0)
forest_green = (0,50,0)
navy_blue = (0,0,100)
rust = (210,150,75)
dandilion_yellow = (255,200,0)
highlighter = (255,255,100)
sky_blue = (171,252,255)
light_gray = (200,200,200)
dark_gray = (50,50,50)
tan = (230,220,170)
coffee_brown = (200,190,140)
moon_glow = (235,245,255)
#

import pygame
import sys
import random
 
 
# initialize the constructor
pygame.init()
res = (900, 800)
 
# randomly assigns a value to variables
# ranging from lower limit to upper
colorone = random.randint(125, 255) 
colortwo = random.randint(0, 255)
colorthree = random.randint(0, 255)
 
screen = pygame.display.set_mode(res)
clock = pygame.time.Clock()
bugout_colorone = 0
bugout_colortwo = 0
bugout_colorthree = 254
bugout_c4 = 254
  
# light shade of menu buttons
startl = (169, 169, 169) 
 
# dark shade of menu buttons
startd = (100, 100, 100) 
white = (255, 255, 255)
start = (255, 255, 255)
width = screen.get_width()
height = screen.get_height()
 
# initial X position of player
lead_x = 60
 
# initial y position of player
lead_y = height / 2
x = 300
y = 290
width1 = 100
height1 = 40
enemy_size = 20
 
# defining a font
smallfont = pygame.font.SysFont('Corbel', 35)
bigfont = pygame.font.SysFont('Corbel', 60)
 
# texts to be rendered on screen
text = smallfont.render('Start', True, white)
exit1 = smallfont.render('Exit', True, white)
 
# game title
bugout = bigfont.render('Bugout', True, (colorthree, colortwo, colorone)) 
x1 = random.randint(width / 2, width)
y1 = random.randint(100, height / 2)
x2 = 40
y2 = 40
speed = 15
 
# score of the player
score = 0
 
# enemy position
enemy_pos = [width, random.randint(20, height - 20)] 
enemy_pos1 = [random.randint(width, width + 100), random.randint(50, height
        - 100)]
  
enemy_pos2 = [width, random.randint(20, height - 20)] 
enemy_pos12 = [random.randint(width, width + 100), random.randint(50, height
        - 100)]

# function for game_over
def game_over():
     
    while True:
         
        # if the player clicks the cross
        # button
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
                 
            if ev.type == pygame.MOUSEBUTTONDOWN:
                if 100 < mouse1[0] < 140 and height - 100 < mouse1[1] \
                    < height - 80:
                    pygame.quit()
                     
                if ev.type == pygame.MOUSEBUTTONDOWN:
                    if width - 180 < mouse1[0] < width - 100 and height \
                        - 100 < mouse1[1] < height - 80:
                         
                        # calling function game
                        game(lead_x, lead_y, speed, score) 
  
        # fills the screen with specified image
        ##
        smallfont = pygame.font.SysFont('Corbel', 60)
        smallfont1 = pygame.font.SysFont('Corbel', 25)
        game_over = smallfont.render('GAME OVER', True, white)
        game_exit = smallfont1.render('Leave', True, white)
        restart = smallfont1.render('Try Again', True, white)
        mouse1 = pygame.mouse.get_pos()
  
        # exit
        if 100 < mouse1[0] < 140 and height - 100 < mouse1[1] < height - 80:
            pygame.draw.rect(screen, startl, [100, height - 100, 40,20])
        else:
            pygame.draw.rect(screen, startd, [100, height - 100, 40,20])
  
        # restart
        if width - 180 < mouse1[0] < width - 100 and height - 100 < mouse1[1] < height - 80:
            pygame.draw.rect(screen, startl, [width - 180, height- 100, 80, 20])
        else:
            pygame.draw.rect(screen, startd, [width - 180, height- 100, 80, 20])
  
        screen.blit(game_exit, (100, height - 100))
     
        # superimposes one object on other
        screen.blit(restart, (width - 180, height - 100)) 
        screen.blit(game_over, (width / 2 - 150, 295))
         
        # updates frames of the game
        pygame.display.update()
  
  
pygame.draw.rect(screen, startd, [100, height - 100, 40, 20])
pygame.draw.rect(screen, startd, [width - 180, height - 100, 40, 50])
  
 
 
# function for body of the game
def game(
    lead_y,
    lead_x,
    speed,
    score,
    ):
  
    while True:
        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                pygame.quit()
  
        # player control
        # keeps track of the key pressed
        keys = pygame.key.get_pressed() 
        if keys[pygame.K_UP]:
             
            # if up key is pressed then the players
            # y pos will decrement by 10
            lead_y -= 10 
        if keys[pygame.K_DOWN]:
             
            # if down key is pressed then the y pos
            # of the player is incremented by 10
            lead_y += 10 
        if keys[pygame.K_LEFT]:

            # if left key is pressed then x pos
            # of the player is decremented by 10 
            lead_x -= 15
        
        if keys[pygame.K_RIGHT]:
            #you get the point
            lead_x += 10

        #background
        bg = pygame.image.load("images/background.png")
        bgsize = (900,800)
        bg_size = pygame.transform.scale(bg, bgsize)
        screen.blit(bg_size, (0,0))
        
        #title and icon       
        pygame.display.set_caption('Bugout')
        #speed
        clock.tick(speed)
         
        # this block line spawns the player
        bug = pygame.image.load("images/bug.png")
        size = (45,45)
        bug_size =  pygame.transform.scale(bug, size)
        screen.blit(bug_size, (lead_x, lead_y))

        ##
        smallfont = pygame.font.SysFont('Corbel', 35)
        exit2 = smallfont.render('Exit', True, white)
  
        # enemy position
        if enemy_pos[0] > 0 and enemy_pos[0] <= width:
             
            # if the enemy block's X coordinate is between 0 and
            # the width of the screen the X value gets
            # decremented by 10
            enemy_pos[0] -= 10 
        else:
            if enemy_pos[1] <= 40 or enemy_pos[1] >= height - 40:
                enemy_pos[1] = height / 2
            if enemy_pos1[1] <= 40 or enemy_pos1[1] >= height - 40:
                enemy_pos1[1] = random.randint(40, height - 40)
            enemy_pos[1] = random.randint(enemy_size, height - enemy_size)
            enemy_pos[0] = width
 
        # game over
        # collision detection
        if lead_x <= enemy_pos[0] <= lead_x + 40 and lead_y >= enemy_pos[1] >= lead_y - 40:
            game_over() 
             
        # checks if the player block has collided with the enemy block
        if lead_y <= enemy_pos[1] + enemy_size <= lead_y + 40 and lead_x <= enemy_pos[0] <= lead_x + 40:
            game_over()

        #enemy block
        spider = pygame.image.load("images/spider.png")
        spidersize = (60,60)
        spider_size = pygame.transform.scale(spider, spidersize)
        screen.blit(spider_size, [enemy_pos[0], enemy_pos[1], enemy_size,enemy_size])        
        
        ###
        if enemy_pos1[0] > 0 and enemy_pos1[0] <= width + 100:
            enemy_pos1[0] -= 10
        else:
            if enemy_pos1[1] <= 40 or enemy_pos1[1] >= height - 40:
                enemy_pos1[1] = height / 2
            enemy_pos1[1] = random.randint(enemy_size, height - 40)
            enemy_pos1[0] = width + 100
  
        if lead_x <= enemy_pos1[0] <= lead_x + 40 and lead_y >= enemy_pos1[1] >= lead_y - 40:
            enemy_pos1[0] = width + 100
            enemy_pos1[1] = random.randint(40, height - 40)
            score += 1
            speed += 1
        
        if lead_y <= enemy_pos1[1] + enemy_size <= lead_y + 40 and lead_x <= enemy_pos1[0] <= lead_x + 40:
            enemy_pos1[0] = width + 100
            enemy_pos1[1] = random.randint(40, height - 40)
             
            # increases the score when blue box is hit
            score += 1 
             
            # increases the speed as score increases
            speed + 1 
  
            if score >= 45:
         
                # freezes the game FPS to 60 if
                # score reaches 45 or more
                speed = 60 
  
        if lead_y <= 38 or lead_y >= height - 38:
            game_over()
        if enemy_pos1[0] <= 0:
            game_over()

        #food block
        food = pygame.image.load("images/food.png")
        foodsize = (40,40)
        food_size = pygame.transform.scale(food, foodsize)
        screen.blit(food_size, [enemy_pos1[0], enemy_pos1[1], enemy_size, enemy_size])

        #score
        currentscore = smallfont.render("%d" % tuple([score]), 1, (10, 10, 10))
        screen.blit(currentscore, (width - 120, height - 40))
        pygame.display.update()
  
# intro
def intro(
    bugout_colorone,
    bugout_colortwo,
    bugout,
    exit1,
    text,
    ):
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.fill((65, 25, 64))
        mouse = pygame.mouse.get_pos()
        
        pygame.display.set_caption('Bugout')

        # start screen
        if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
             
            # if mouse is hovered on a button
            # its colour shade becomes lighter
            pygame.draw.rect(screen, startl, [x, y, width1, height1]) 
        else:
            
                if x < mouse[0] < width1 + x and y + 140 < mouse[1] < y + 140 + height1:
                    pygame.draw.rect(screen, startl, [x, y + 140,width1,height1])
                else:
                    pygame.draw.rect(screen, startd, [x, y, width1,height1])
                    pygame.draw.rect(screen, startd, [x, y + 140,width1, height1])
  
        # start button
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x < mouse[0] < x + width1 and y < mouse[1] < y + height1:
                game(lead_y, lead_x, speed, score)
  
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x < mouse[0] < width1 + x and y + 140 < mouse[1] < y + 140 + height1:
                pygame.quit()
  
        # this handles the colour breezing effect
        if 0 <= bugout_colorone <= 254 or 0 <= bugout_colortwo <= 254:
            bugout_colorone += 1
            bugout_colortwo += 1
        if bugout_colorone >= 254 or bugout_colortwo >= 254:
            bugout_colorone = colorthree
            bugout_colortwo = colorthree
  

        ##

        smallfont = pygame.font.SysFont('Bug Out', 35)
        name = smallfont.render('Created By xoLilli', True, white)
        text = smallfont.render('Start', True, white)
        exit1 = smallfont.render('Exit', True, white)
        bugout = smallfont.render('Bugout', True, (colorone, bugout_colorone,
                                 bugout_colortwo))
        screen.blit(bugout, (320, 50))
        screen.blit(text, (320, 295))
        screen.blit(exit1, (320, 435))
        screen.blit(name, (320, height - 50))
        clock.tick(60)
        pygame.display.update()
  
  
intro(
    bugout_colorone,
    bugout_colortwo,
    bugout,
    exit1,
    text,
    )