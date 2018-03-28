# Kurs Pygame
Materiały pochodzą z serii fimów [LINK](https://www.youtube.com/watch?v=nGufy7weyGY&list=PLsk-HSGFjnaH5yghzu7PcOzm9NhsW0Urw&index=4), którą serdecznie polecam. Ta strona jest dla mnie poligonem doświadczalnym do nauki dla siebie. Jeśli przy okazji ktoś inny z tego skorzysta to bardzo się cieszę.

## Szablon gry

Spróbujmy przeanalizować plik znajdujący się poniżej. Importujemy bibliotekę **pygame**. Następnie ustalamy szerokość, wysokość i ilość klatek na sekundę. Wygodnie jest przechowywać w zmiennych globalnych. Wygodną praktyką jest też przechowywanie podtawowych kolorów w postaci zmiennych, ponieważ mogą nam się przydać do kolorowania obiektów.

Pygame.init i pygame.mixer.init służą nam do inicjowania samego pygame'a oraz muzyki. Następnie do zmiennej screen wrzucamy inicjalizację ekranu w której podajemy ustalone wcześniej wymiary okna. Później możemy wybrać sobie tytuł naszej gry. Inicjalizacja zegara będzie nam potrzebna podczas liczenia klatek na sekundę.

**All_sprites** przechowuje dane na temat wyświetlanych obiektów. astępnie potrzebujemy pętli która będzie na wyświetlać i rysować nasze obiekty. Zmienna **running** służy do kończenia pętli w momencie gdy użytkownik np. będzie chciał wyłączyć grę (funkcja wyłączająca program jest przy pierwszym if'ie). Należy pamiętać o tym, żeby obiekty były odświerzane, więc potrzebujemy  
**all_sprites.update()**
Na końcu wypełniamy ekran czarnym kolorem i wyświelamy go.

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
# PIERWSZA GRA
## Tworzenie postaci

