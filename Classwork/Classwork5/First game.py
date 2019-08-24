import pygame

pygame.init()

WHITE = (255, 255, 255)  
#ORANGE = (255, 150, 100)
PINK = (230, 50, 230)

DISPLAY_WIDTH = 400 
DISPLAY_HEIGH = 400 

gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGH))

pygame.display.set_caption("My first game")

clock=pygame.time.Clock()

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  for event in pygame.event.get(): # User did something
    if event.type == pygame.QUIT: # If user clicked close
        done = True # Flag that we are done so we exit this loop
  
  # --- Game logic should go here
  # --- Drawing code should go here
  # First, clear the screen to white. Don't put other 
  # drawing commands above this, 
  # or they will be erased with this command.
  
  gameDisplay.fill(PINK)
  
  # --- Go ahead and update the screen with what we've drawn.
  pygame.display.update()
  
  # --- Limit to 60 frames per second
  clock.tick(60)


3


import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primitives")
clock = pygame.time.Clock()
WHITE=(255,255,255)
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    
    pygame.draw.line(screen, (255,255,255), [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE, [10, 30], [290, 15], 3)
    pygame.draw.line(screen, WHITE, [10, 50], [290, 35])
    
    #aaline згладжена лінія, товщина в цьому
    # випадку не задається
    pygame.draw.aaline(screen, WHITE, [10, 70], [290, 55])
   
    pygame.display.update()
    pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
    #pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
    pygame.draw.aalines(screen, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])







2


import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primitives")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
      
    передається прямокутна область, в якій промальовується еліпс

    pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100))

    pygame.display.update()

    
    r1 = pygame.Rect((150, 20, 100, 75))
 
    pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    pygame.draw.rect(screen, YELLOW, r1, 8)


коло
    pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
    pygame.draw.circle(screen, PINK, (200, 100), 50)

  5  
import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primitives")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
PI = 3.14
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
    
    pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)

    pygame.display.update()

    pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)