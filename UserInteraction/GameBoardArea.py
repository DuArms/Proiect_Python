from resurse.utilitare import *

from Game.Play.AI import play_ai
from Game.Play.PvP import pvp

from Game.Rules.GameState import GameState
from GUI.GameGUI import *

import time

opponent_lvl = HARD_AI
tura = 1


def end_game(status):
    '''
    Functie ce se apeleaza cand s-a terminat un joc
    :param status:
    :return:
    '''
    global game_gui
    print("end game", status)
    game_gui.buttons.append(Button( game_gui.hex_crd[NUMAR_LINII // 2 -2, NUMAR_COLOANE // 2-2],
                                    (45, 34, 104), status, game_gui.button_size, None))
    game_gui.draw()
    game_gui.buttons = game_gui.buttons[:-1]
    time.sleep(3)
    game_gui = init_game()


def game_table_click(game_gui, mouse_pozition, opponent_lvl):
    '''
    Functie principala ce menegeriaza interactiunea
    dintre jucator si reprezentarea jocului.
    :param game_gui:
    :param mouse_pozition:
    :param opponent_lvl:
    :return:
    '''
    global tura
    poz = get_chenar(game_gui.hex_crd, mouse_pozition, GameGUI.r)

    if poz is not None:
        x, y = poz

        if opponent_lvl == PVP:
            status, tura = pvp(game_gui ,game_state, poz, tura)
            if status is not None:
                end_game(status)
                return

        else:  # Oponentul este un AI
            if game_state.build_wall(x, y):
                game_gui.set_wall(poz)

                status = play_ai(game_state, diff_lvl=opponent_lvl)

                if type(status) == str:
                    end_game(status)
                    return

                game_gui.soarece.position = game_gui.hex_crd[status]


def init_game():
    '''
    Functie de initializare pentru un joc nou.
    :return:
    '''
    pygame.init()

    global game_state
    global game_gui

    game_gui.soarece.position = game_gui.hex_crd[NUMAR_LINII // 2, NUMAR_COLOANE // 2]

    game_gui.draweble_table = []
    for line in game_gui.hex_crd:
        for hex in line:
            p = [
                (poly_points(hex, GameGUI.r), VERDE_EXTERIOR),
                (poly_points(hex, GameGUI.r * 0.80), VERDE_MIJLOC),
                (poly_points(hex, GameGUI.r * 0.50), VERDE_INTERIOR)
            ]
            game_gui.draweble_table.append(p)

    game_state = GameState()

    for poz in np.argwhere(game_state.tabla == GameState.ZID):
        game_gui.set_wall(poz)

    return game_gui
