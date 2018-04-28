#Pygame template - skeleton for a new pygame project
import pygame
import random
from settings import *
import random
font_name = pygame.font.match_font('timesnewroman')

#initialize pygame and creat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y-size//2)
    surf.blit(text_surface, text_rect)

def ListPrint(tab):
    for i in range(0, len(tab)):
        print(tab[i])
    print("\n")

def addNumber():
    options = []
    for i in range (0,4):
        for j in range (0,4):
            if GRID[i][j] == 0:
                options.append([i,j])
    rand = random.randint(0, len(options)-1)
    if len(options) > 0:
        r = random.randint(0, 2)
        if r == 0:
            GRID[options[rand][0]][options[rand][1]] = 2
        else:
            GRID[options[rand][0]][options[rand][1]] = 4

ListPrint(GRID)
addNumber()
ListPrint(GRID)
addNumber()
ListPrint(GRID)
def updateDraw():
    for i in range(0,4):
        for j in range(0,4):
            if GRID[i][j] == 0:
                pygame.draw.rect(screen, YELLOW, (i*TILE+5*(i+1), j*TILE+5*(j+1), 99,99))
            else:
                pygame.draw.rect(screen, (200,200,200-20*GRID[i][j] ), (i*TILE+5*(i+1), j*TILE+5*(j+1), 99,99))
                draw_text(screen, str(GRID[i][j]), 60, i*TILE+5*(i+1)+50, j*TILE+5*(j+1)+50)
all_sprites = pygame.sprite.Group()
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
    updateDraw()
    
    # Draw / render
    screen.fill(BLACK)
    updateDraw()
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()
pygame.quit()
