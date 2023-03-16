#lab1
import random
import pygame as pg
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
posX, posY = 20, 20
size=0
x=1

while(1):
    screen.fill((255, 255, 255))
    Color1 = random.randrange(255)
    Color2 = random.randrange(255)
    Color3 = random.randrange(255)
    pg.draw.circle(screen,(Color1,Color2,Color3),(win_x/2,win_y/2),size)
    
    size+=x
        
    pg.time.delay(1) #หน่วงเวลา
    if (size<=0):
      x=1
    elif(size>=win_y/2):
      x=-1
    pg.display.update()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

#Mouse Click

import pygame as pg
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
posX, posY = 20, 20

while(1):
    screen.fill((255, 255, 255))
    
    if pg.mouse.get_pressed()[0] == 1: # Check mouse pressed
        (posX, posY) = pg.mouse.get_pos()
        print(1)
    else:
      print(0)
    pg.draw.circle(screen,(100,100,100),(posX,posY),20)
    pg.display.update()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()


#Free Fall
import random
import pygame as pg
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
posX, posY = 20, 20
size=0
x=0

while(1):
    screen.fill((255, 255, 255))
    Color1 = random.randrange(255)
    Color2 = random.randrange(255)
    Color3 = random.randrange(255)
    pg.draw.circle(screen,(Color1,Color2,Color3),(posX,posY),20)
    posY+=x
    x+=1
    pg.time.delay(20) #หน่วงเวลา
    pg.display.update()
    if(posY>=win_y-20):
      exit()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

#Projectile
import math
import pygame as pg
pg.init()
win_x, win_y = 800, 480
screen = pg.display.set_mode((win_x, win_y))
posX, posY = 20, 400
V1=15
Degree=50
G=1
Vy=-1*math.sin(Degree*3.14/180)*V1
Vx=math.cos(Degree*3.14/180)*V1
t=0
while(1):
    screen.fill((255, 255, 255))
    pg.draw.circle(screen,(0,0,0),(posX,posY),20)
    
    posX+=Vx
    posY+=Vy +(0.5*G*t**2)
    
    
    pg.time.delay(100) #หน่วงเวลา
    t+=0.1
    pg.display.update()
    if(posY>=win_y):
      exit()
    
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

