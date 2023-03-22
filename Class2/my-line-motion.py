import pygame

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

# Draw a rectangle at the center of the screen (in the backbuffer)
size = 10  # dimensions of the rectangle in pixels
delta= 5
left_x = 0  # x coordinate of topleft corner
top_y = center_y - 3*size // 2 
top_y_flash = center_y + 3*size // 2 
pygame.draw.rect(screen, RED, (left_x, top_y, size,size))
pygame.display.flip()  # display the backbuffer on the screen
pygame.time.wait(50)

# Wait until the window is closed
quit_button_pressed = False
while not quit_button_pressed:
    screen.fill(WHITE)
    
    left_x += delta
    if (left_x <= 0) or (left_x >=  W-size) :
        delta = -delta

    if left_x==center_x:
        pygame.draw.rect(screen, RED, (left_x, top_y_flash, size,size))

    pygame.draw.rect(screen, RED, (left_x, top_y, size,size))
    pygame.display.flip()  # display the backbuffer on the screen
    pygame.time.wait(50)




    pygame.time.wait(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit_button_pressed = True

pygame.quit()