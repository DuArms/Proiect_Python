from constants import *
from utilitare import *
from Imagine import Imagine
from GameLogic import *

import time
# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([GAME_WIDTH, GAME_HIGHT])

r = R
p = [250, r]

poza_soarece = pygame.image.load("resurse/rat.png")
poza_soarece = pygame.transform.scale(poza_soarece, (52, 52))

tabla = generate_table(p, r)

soarece = Imagine(
    poza_soarece,
    tabla[NUMAR_LINII // 2, NUMAR_COLOANE // 2]
)

droweble_table = []
for line in tabla:
    for hex in line:
        p = [
            (poly_points(hex, r), VERDE_EXTERIOR),
            (poly_points(hex, r * 0.80), VERDE_MIJLOC),
            (poly_points(hex, r * 0.50), VERDE_INTERIOR)
        ]
        droweble_table.append(p)

game_area = [
    tabla[0, 0] + [-5 / 2 * r, -3 / 2 * r],
    tabla[-1, -1] + [-7 / 2 * r, +1 / 2 * r]
]

menu_area = [
    game_area[0] + [game_area[1][0] + GAME_WIDTH / 15, 0],
    (300, game_area[1][1])
]

clock = pygame.time.Clock()
clock.tick(30)

# 33333333333333333333333333333333333333333333333333333333333333333333
# smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
# text = smallfont.render('quit', True, BLACK)


# 333333333333333333333333333333333333333333333333333333333333333333333333333




def draw(screen):
    # Fill the background with white
    screen.fill(WHITE)

    # Deseneaza tabla
    for value in droweble_table:
        for poly, culoare in value:
            pygame.draw.polygon(screen, culoare, poly)

    pygame.draw.rect(screen, BLACK, game_area, 2)
    pygame.draw.rect(screen, BLUE, menu_area, 2)

    pygame.draw.circle(screen, RED, menu_area[0], r * 0.95)

    # Deseneaza soarece
    screen.blit(soarece.img, soarece.get_pos_2_draw())



    # screen.blit(text,  menu_area[0 ])

    pygame.display.flip()
    clock.tick(60)


# Run until the user asks to quit
running = True

p = [NUMAR_LINII // 2, NUMAR_COLOANE // 2]
def game_table_click(tabla, mouse_pozition):
    global r ,p

    poz = get_chenar(tabla, mouse_pozition, r)
    if poz is not None:
        poz = poz[0] * NUMAR_COLOANE + poz[1]

        hexagon = droweble_table[poz][0][0]
        hexagon1 = droweble_table[poz][1][0]
        print(hexagon)
        droweble_table[poz] = [(hexagon, RED), (hexagon1, (255, 165, 0))]

        p = update_pozitie_soarece(p, None)
        soarece.position = tabla[p[0], p[1]]


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pozition = pygame.mouse.get_pos()

            if game_area[0][0] < mouse_pozition[0] < game_area[0][0] + game_area[1][0] \
                    and game_area[0][1] < mouse_pozition[0] < game_area[1][1] + game_area[1][1]:
                game_table_click(tabla, mouse_pozition)




    draw(screen)

# print(pygame.mouse.get_pos())
# time.sleep(SOMN)
# running = False

# Done! Time to quit.
pygame.quit()
