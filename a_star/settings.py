WIDTH = 400
HEIGHT = 400

FPS = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)

COLS = 5
ROWS = 5

W = WIDTH // COLS
H = HEIGHT // ROWS

GRID = []
OPENSET = []
CLOSESET = []

def gridPrint(grid):
    for i in range (0, len(grid)):
        print(grid[i])
