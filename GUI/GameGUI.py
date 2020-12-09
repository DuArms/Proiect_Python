from resurse.utilitare import calc_hex_crd
from GUI.PrimitiveGrafice.Imagine import Imagine
from GUI.PrimitiveGrafice.Button import Button
from resurse.constants import *

import pygame

# Set up the drawing window
screen = pygame.display.set_mode([GAME_WIDTH, GAME_HIGHT])

poza_soarece = pygame.image.load("./resurse/rat.png")
poza_soarece = pygame.transform.scale(poza_soarece, (52, 52))

r = R
p = [250, r]

hex_crd = calc_hex_crd(p, r)

soarece = Imagine(
    poza_soarece,
    hex_crd[NUMAR_LINII // 2, NUMAR_COLOANE // 2]
)

imgs = [soarece]

draweble_table = []

game_area = [
    hex_crd[0, 0] + [-5 / 2 * r, -3 / 2 * r],
    hex_crd[-1, -1] + [-7 / 2 * r, +1 / 2 * r]
]

menu_area = [
    game_area[0] + [game_area[1][0] + GAME_WIDTH / 15, 0],
    (300, game_area[1][1])
]

menu_width = menu_area[1][0]
menu_hight = menu_area[1][1]

button_size = (menu_width * 0.90, menu_hight * (1 / 8))
buttons = []


clock = pygame.time.Clock()


def set_wall(droweble_table, poz):
    poz = poz[0] * NUMAR_COLOANE + poz[1]
    hexagon = droweble_table[poz][0][0]
    hexagon1 = droweble_table[poz][1][0]
    droweble_table[poz] = [(hexagon, RED), (hexagon1, ORENGE)]


def draw(screen, droweble_table, buttons ,imgs):
    # Fill the background with white
    screen.fill(WHITE)

    # Deseneaza tabla
    pygame.draw.rect(screen, BLACK, game_area, 2)

    for value in droweble_table:
        for poly, culoare in value:
            pygame.draw.polygon(screen, culoare, poly)

    # Deseneaza meniu
    # pygame.draw.rect(screen, BLUE, menu_area, 2)

    for bt in buttons:
        bt.draw(screen)

    # Deseneaza soarece
    for img in imgs:
        screen.blit(img.img, img.get_pos_2_draw())

    # screen.blit(text,  menu_area[0 ])

    pygame.display.flip()

    clock.tick(60)
