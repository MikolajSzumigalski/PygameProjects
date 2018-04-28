#Pygame template - skeleton for a new pygame project
import pygame
import random
from cell import *
from settings import *
import random

#initialize pygame and creat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

all_sprites = pygame.sprite.Group()
for i in range(0, ROWS):
    for j in range(0, COLS):
        all_sprites.add(GRID[i][j])
OPTIONS =[]
for i in range(0, ROWS):
    for j in range(0, COLS):
        OPTIONS.append([i,j])

print(OPTIONS)

for v in range(0, TOTALBEES):
    index = random.randint(0, len(OPTIONS)-1)
    choice = OPTIONS[index]
    i = choice[0]
    j = choice[1]
    OPTIONS.remove(choice)
    GRID[i][j].bee = True
print(OPTIONS)

for i in range(0, ROWS):
    for j in range(0, COLS):
        GRID[i][j].countNeighbors(GRID)

pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


#Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pygame.event.get():
        # check for closing the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    all_sprites.update()



    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
