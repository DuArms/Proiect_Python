from utilitare import *
from Imagine import Imagine

import pygame



# Set up the drawing window
screen = pygame.display.set_mode([GAME_WIDTH, GAME_HIGHT])

poza_soarece = pygame.image.load("resurse/rat.png")
poza_soarece = pygame.transform.scale(poza_soarece, (52, 52))

r = R
p = [250, r]

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

def draw(screen):
    # Fill the background with white
    screen.fill(WHITE)

    # Deseneaza tabla
    pygame.draw.rect(screen, BLACK, game_area, 2)

    for value in droweble_table:
        for poly, culoare in value:
            pygame.draw.polygon(screen, culoare, poly)

    #Deseneaza meniu
    pygame.draw.rect(screen, BLUE, menu_area, 2)

    pygame.draw.circle(screen, RED, menu_area[0], r * 0.95)

    # Deseneaza soarece
    screen.blit(soarece.img, soarece.get_pos_2_draw())

    # screen.blit(text,  menu_area[0 ])

    pygame.display.flip()
    clock.tick(60)