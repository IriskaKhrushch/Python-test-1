1

#pylint: disable=C0321 
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
#clock = pygame.time.Clock()

done = False
clock = pygame.time.Clock()

x=50
y=50
width=40
height=60
vol=5

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    keys=pygame.key.get_pressed()        

    if keys[pygame.K_LEFT]:
        x=x-vol
    if keys[pygame.K_RIGHT]:
        x=x+vol
    if keys[pygame.K_UP]:
        y=y-vol
    if keys[pygame.K_DOWN]:
        y=y+vol
    

    pygame.draw.rect(screen, (255,0,0), [55, 50, 80, 55])
    
    
    pygame.display.update()
  #clock.tick(60)


2
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("My first game")
#clock = pygame.time.Clock()

x=50
y=50
width=40
height=60
vol=5


run = True
clock = pygame.time.Clock()

while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            run=False

    keys=pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>vol:
        x=x-vol
    if keys[pygame.K_RIGHT] and x<500-width-vol:
        x=x+vol
    if keys[pygame.K_UP] and y>vol:
        y=y-vol
    if keys[pygame.K_DOWN] and y<500-height-vol:
        y=y+vol


    #without trace
    screen.fill((0,0,0))          
    
    pygame.draw.rect(screen, (255,0,0), [x, y, width, height])
    pygame.display.update()
  #clock.tick(60)


3


import pygame
 
FPS = 60
W = 700  # ширина екрана
H = 300  # висота екрана
WHITE = (255, 255, 255)
BLUE = (0, 70, 225)
 
pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координати і радіус круга
x = W // 2
y = H // 2
r = 50
 
while 1:
    sc.fill(WHITE)
 
    pygame.draw.circle(sc, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                x -= 3
            elif i.key == pygame.K_RIGHT:
                x += 3
 
    clock.tick(FPS)

5
import pygame
pygame.init()
gameDisplay=pygame.display.set_mode((400,300))
pygame.display.set_caption("My first game")
clock=pygame.time.Clock()
crashed=False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
        elif event.type == pygame.KEYDOWN:
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("User pressed a mouse button")

        
    pygame.display.update()

    clock.tick(60)

pygame.quit()
quit()


6
import pygame

pygame.init()

gameDisplay=pygame.display.set_mode((400,300))

pygame.display.set_caption("my first game")

clock=pygame.time.Clock()

crashed=False
while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True

        print(event)

    pygame.display.update()

    clock.tick(60)

pygame.quit()
#quit()