#Pygame template - skeleton for a new pygame project
import pygame
import random
from settings import *

#initialize pygame and creat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

class Spot(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.f = 0
        self.g = 0
        self.h = 0
        self.image = pygame.Surface((W-1, W-1))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x+ W /2, self.y+ W/2)



all_sprites = pygame.sprite.Group()

for i in range(0, COLS):
    GRID.append([])

for i in range(0, COLS):
    for j in range(0, ROWS):
        GRID[i].append(Spot(i,j))
        all_sprites.add(GRID[i][j])
START = GRID[0][0]
END = GRID[COLS-1][ROWS-1]

OPENSET.append(START)


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
    #while len(OPENSET) > 0:
    all_sprites.update()
        # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
