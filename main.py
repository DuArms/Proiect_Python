from constants import *
from utilitare import *
import time
# Import and initialize the pygame library
import pygame

pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([GAME_WIDTH, GAME_HIGHT])

r = 30
p = (250, r)

tabla = generate_table(p, r)
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


# 33333333333333333333333333333333333333333333333333333333333333333333
# smallfont = pygame.font.SysFont('Corbel', 35)

# rendering a text written in
# this font
# text = smallfont.render('quit', True, BLACK)


# 333333333333333333333333333333333333333333333333333333333333333333333333333


def draw(screen):
    # Fill the background with white
    screen.fill(WHITE)
    # Draw a solid blue circle in the center
    # pygame.draw.circle(screen, BLUE, circle_center , 75)

    for value in droweble_table:
        for poly, culoare in value:
            pygame.draw.polygon(screen, culoare, poly)

    pygame.draw.rect(screen, BLACK, game_area, 2)
    pygame.draw.rect(screen, BLUE, menu_area, 2)

    pygame.draw.circle(screen, RED, menu_area[0], r * 0.95)

    # screen.blit(text,  menu_area[0 ])

    pygame.display.flip()


# Run until the user asks to quit
running = True

def game_table_click(tabla  ,mouse_pozition):
    global  r

    poz = get_chenar(tabla, mouse_pozition, r)
    if poz is not None:
        poz = poz[0] * NUMAR_COLOANE + poz[1]

        hexagon = droweble_table[poz][0][0]
        hexagon1 = droweble_table[poz][1][0]
        print(hexagon)
        droweble_table[poz] = [(hexagon, RED) , (hexagon1,(255,165,0) )]


while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_pozition = pygame.mouse.get_pos()

            if game_area[0][0] < mouse_pozition[0] < game_area[0][0] + game_area[1][0] \
                    and game_area[0][1] < mouse_pozition[0] < game_area[1][1]+ game_area[1][1]:
                    game_table_click(tabla , mouse_pozition)




        draw(screen)

# print(pygame.mouse.get_pos())
# time.sleep(SOMN)
# running = False

# Done! Time to quit.
pygame.quit()
