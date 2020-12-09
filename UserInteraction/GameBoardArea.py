from resurse.utilitare import *

from Game.Play.AI import play_ai
from Game.Play.PvP import pvp

from Game.Rules.GameState import GameState
from GUI.GameGUI import *


import sys

opponent_lvl = MEDIUM_AI
tura = 1

def end_game(status):
    print("end game", status)
    sys.exit(0)


def game_table_click(hex_crd, mouse_pozition,opponent_lvl):
    global r, tura, draweble_table
    poz = get_chenar(hex_crd, mouse_pozition, r)

    if poz is not None:
        x, y = poz

        if opponent_lvl == PVP:
            status,tura = pvp(game_state, poz,tura)
            if status is not None:
                end_game(status)

        else:  # Oponentul este un AI
            if game_state.build_wall(x, y):
                set_wall(draweble_table, poz)

                status = play_ai(game_state, diff_lvl=opponent_lvl)

                if type(status) == str:
                    end_game(status)

                soarece.position = hex_crd[status]


def init_game():
    pygame.init()

    global game_state
    global draweble_table
    global hex_crd
    global  imgs

    draweble_table = []
    for line in hex_crd:
        for hex in line:
            p = [
                (poly_points(hex, r), VERDE_EXTERIOR),
                (poly_points(hex, r * 0.80), VERDE_MIJLOC),
                (poly_points(hex, r * 0.50), VERDE_INTERIOR)
            ]
            draweble_table.append(p)

    game_state = GameState()

    for poz in np.argwhere(game_state.tabla == GameState.ZID):
        set_wall(draweble_table, poz)

    return draweble_table
