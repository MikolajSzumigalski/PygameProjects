
import pygame as pg
from settings import *
font_name = pg.font.match_font('timesnewroman')

def draw_text(surf, text, size, x, y, bgcolor):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y-size//2)
    surf.blit(text_surface, text_rect)

class Cell(pg.sprite.Sprite):
    def __init__(self, x, y, w):
        pg.sprite.Sprite.__init__(self)
        self.i = x // w
        self.j = y // w
        self.x = x
        self.y = y
        self.w = w
        self.myNeighbor = 0
        self.bee = False
        self.revealed = False
        self.image = pg.Surface((w-1, w-1))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (self.x+ self.w /2, self.y+ self.w/2)
        self.flag = False


    def isClicked(self):
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if(click[0] == 1 and (self.flag == False)):
            if( self.x < mouse[0]< self.x+ self.w and self.y < mouse[1]< self.y+ self.w):
                self.revealed = True
                self.image.fill(LIGHT_GREY)
                if(self.myNeighbor>0):
                    draw_text(self.image,  str(self.myNeighbor), 20, self.w//2, self.w//2, BLACK)
                else:
                    if(self.myNeighbor==0):
                        self.floodFill()
                if (self.bee):
                    self.bomb = pg.draw.circle(self.image, BLACK, [ self.w//2,  self.w//2],  self.w//4)
        else:
            if(click[0] == 1 and self.flag):
                if( self.x < mouse[0]< self.x+ self.w and self.y < mouse[1]< self.y+ self.w):
                    self.image.fill(BLUE)
                    self.flag = False
            else:
                if(click[2] == 1 and (self.revealed == False)):
                    if( self.x < mouse[0]< self.x+ self.w and self.y < mouse[1]< self.y+ self.w):
                        self.flag = True
                        draw_text(self.image,  "F", 20, self.w//2, self.w//2, BLACK)
    def countNeighbors(self, gr):
        total = 0
        if(self.bee):
            total =  -10
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.i+i!=-1 and self.j+j!=-1and self.i+i!=COLS and self.j+j!=ROWS):
                    if(gr[self.i+i][self.j+j].bee):
                        total = total + 1
        self.myNeighbor = total
    def isRevealed(self):
        if(self.revealed):
            self.image.fill(LIGHT_GREY)
            if(self.myNeighbor>0):
                draw_text(self.image,  str(self.myNeighbor), 20, self.w//2, self.w//2, BLACK)
            else:
                if(self.myNeighbor==0):
                    self.floodFill()
            if (self.bee):
                self.bomb = pg.draw.circle(self.image, BLACK, [ self.w//2,  self.w//2],  self.w//4)
                self.gameOver()
    def update(self):
        self.isClicked()
        self.isRevealed()

    def floodFill(self):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if(self.i+i!=-1 and self.j+j!=-1and self.i+i!=COLS and self.j+j!=ROWS):
                    if(not GRID[self.i+i][self.j+j].bee):
                        GRID[self.i+i][self.j+j].revealed = True
    def gameOver(self):
        for i in range(0, ROWS):
            for j in range(0, COLS):
                GRID[i][j].revealed = True
def make2DArray(rows):
    arr = []
    for i in range(0, rows):
        arr.append([])
    return arr

GRID = make2DArray(ROWS)
for i in range(0, ROWS):
    for j in range(0, COLS):
        GRID[i].append(Cell(i*W, j*W, W))
