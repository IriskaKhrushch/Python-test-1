
import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
#PINK = (230, 50, 230)
# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([500, 500])
 
# This sets the name of the window
pygame.display.set_caption('Smile')
 
clock = pygame.time.Clock()


#обновляємо екран 
pygame.display.update()

x=50
y=50
width=40
height=60
vol=5

# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("C:\\Users\\Iriska\\Desktop\\Фото\\smile.gif").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True  
    keys=pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x>vol:
        x=x-vol
    if keys[pygame.K_RIGHT] and x<400-width-vol:
        x=x+vol
    if keys[pygame.K_UP] and y>vol:
        y=y-vol
    if keys[pygame.K_DOWN] and y<420-height-vol:
        y=y+vol
    screen.fill((0,0,0))
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    # player_position = pygame.mouse.get_pos()
    # x = player_position[0]
    # y = player_position[1]
 
    # Copy image to screen:
#копіює картинку на екран
    screen.blit(player_image, [x, y])
    
#обновляємо екран
    
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()