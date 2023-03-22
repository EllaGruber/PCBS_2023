import pygame
import numpy as np

# Colors are triplets containint RGB values
# see <https://www.rapidtables.com/web/color/RGB_Color.html>
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (127, 127, 127)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#  create the window
W, H = 500, 500  # Size of the graphic window
# Note that (0,0) is at the *upper* left hand corner of the screen.
center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('square')

screen.fill(WHITE)  # fill it with white

screen.fill(WHITE)  # fill it with white

# Draw a rectangle at the center of the screen (in the backbuffer)
 # x coordinate of topleft corner
center_circle_size= 10
min_periph_circle_size = 5
max_periph_circle_size= 40
delta=1
distance_center_periph=100
fixation_circle_size= 3
diagonal= int(np.sqrt(2)/2 *(distance_center_periph  + max_periph_circle_size))
pygame.draw.circle(screen, BLACK, (center_x , center_y), center_circle_size,width=0)
pygame.draw.circle(screen, (255,255,0), (center_x , center_y), fixation_circle_size,width=0)



def draw_periph_circle(size_periph):
    pygame.draw.circle(screen, BLACK, (center_x - distance_center_periph - max_periph_circle_size , center_y), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x + distance_center_periph+ max_periph_circle_size , center_y), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x, center_y - distance_center_periph - max_periph_circle_size), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x, center_y + distance_center_periph + max_periph_circle_size), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x - diagonal, center_y - diagonal), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x + diagonal, center_y - diagonal), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x - diagonal, center_y + diagonal), size_periph,width=0)
    pygame.draw.circle(screen, BLACK, (center_x + diagonal, center_y + diagonal), size_periph,width=0)

size_periph = min_periph_circle_size
draw_periph_circle(size_periph)
pygame.display.flip()  # display the backbuffer on the screen
pygame.time.wait(50)

# Wait until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    screen.fill(WHITE)
    pygame.draw.circle(screen, BLACK, (center_x , center_y), center_circle_size,width=0)
    pygame.draw.circle(screen, (255,255,0), (center_x , center_y), fixation_circle_size,width=0)

    size_periph += delta
    if (size_periph <= min_periph_circle_size) or (size_periph >=  max_periph_circle_size) :
        delta = -delta

    draw_periph_circle(size_periph)

    pygame.display.flip()  # display the backbuffer on the screen
    pygame.time.wait(50)




    pygame.time.wait(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()