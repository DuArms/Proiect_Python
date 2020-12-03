import sys

from GameGUI import *
from GameRules.GameState import *
from AiLogic.SelectAI import play_ai

pygame.init()

game_state = GameState()

for poz in np.argwhere(game_state.tabla == GameState.ZID):
    poz = poz[0] * NUMAR_COLOANE + poz[1]

    hexagon = droweble_table[poz][0][0]
    hexagon1 = droweble_table[poz][1][0]
    droweble_table[poz] = [(hexagon, RED), (hexagon1, (255, 165, 0))]


def game_table_click(tabla, mouse_pozition):
    global r

    poz = get_chenar(tabla, mouse_pozition, r)
    if poz is not None:
        x, y = poz
        # aux for debug
        # moves = game_state.get_mouse_moves()
        #
        # for x, y in moves:
        #     poz1 = x * NUMAR_COLOANE + y
        #
        #     hexagon = droweble_table[poz1][0][0]
        #     hexagon1 = droweble_table[poz1][1][0]
        #     droweble_table[poz1] = [(hexagon, BLUE), (hexagon1, (0, 0, 165))]

        if game_state.build_wall(x, y):
            poz = poz[0] * NUMAR_COLOANE + poz[1]

            hexagon = droweble_table[poz][0][0]
            hexagon1 = droweble_table[poz][1][0]
            droweble_table[poz] = [(hexagon, RED), (hexagon1, (255, 165, 0))]

            status = play_ai(game_state, diff_lvl=2)
            if type(status) == str:
                print(status)
                sys.exit(0)

            x, y = status
            soarece.position = tabla[x, y]

            print(game_state.tabla)


# Run until the user asks to quit
running = True

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
