import pygame
import numpy as np

# Colors are triplets containint RGB values

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)



W, H = 900, 900  # Size of the graphic window size
# Note that (0,0) is at the *upper* left hand corner of the screen.

center_x = W // 2
center_y = H // 2

pygame.init()
screen = pygame.display.set_mode((W, H), pygame.DOUBLEBUF)
pygame.display.set_caption('Troxler illusion')
screen.fill(WHITE)



radius = 40
place = W//3




size = 200

point1 = (center_x - size, center_y + size)
point2 = (center_x + size, center_y + size)
point3 = (center_x, center_y - size*np.sqrt(2))
pygame.draw.lines(screen, BLACK, True, (point1, point2, point3), 5) # drawing the line

point4 = (center_x - size, center_y - size)
point5 = (center_x + size, center_y - size)
point6 = (center_x, center_y + size*np.sqrt(2))


pygame.draw.circle(screen, BLACK,   point4, radius, width=0)
pygame.draw.circle(screen, BLACK,   point5, radius, width=0)
pygame.draw.circle(screen, BLACK,   point6, radius, width=0)



pygame.draw.polygon(screen, WHITE, (point4, point5, point6), 0)
pygame.display.flip()  # display the backbuffer

# save the image into a file
pygame.image.save(screen, "kanizsa_triangle.png")

# wait until the window is closed
done = False
while not done:
    pygame.time.wait(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

