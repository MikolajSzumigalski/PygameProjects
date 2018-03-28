# Kurs Pygame
## Szablon gry

Spróbujmy przeanalizować plik znajdujący się poniżej. Importujemy bibliotekę **pygame**. Następnie ustalamy szerokość, wysokość i ilość klatek na sekundę. Wygodnie jest przechowywać w zmiennych globalnych. Wygodną praktyką jest też przechowywanie podtawowych kolorów w postaci zmiennych, ponieważ mogą nam się przydać do kolorowania obiektów.

Pygame.init i pygame.mixer.init służą nam do inicjowania samego pygame'a oraz muzyki. Następnie do zmiennej screen wrzucamy inicjalizację ekranu w której podajemy ustalone wcześniej wymiary okna. Później możemy wybrać sobie tytuł naszej gry. Inicjalizacja zegara będzie nam potrzebna podczas liczenia klatek na <b>sekundę</b>
```python
#Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0, 255,0)
BLUE = (0,0,255)

#initialize pygame and creat window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()

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


    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()
```
Jak 
