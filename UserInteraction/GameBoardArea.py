import pygame

from resurse.constants import *
from resurse.utilitare import *

from Game.Play.AI import play_ai
from Game.Play.PvP import pvp

from Game.Rules.GameState import GameState
from GUI.GameGUI import *

from UserInteraction.Parametrii import *
import sys


def end_game(status):
    print("end game", status)
    sys.exit(0)


def game_table_click(hex_crd, mouse_pozition):
    global r, tura, draweble_table,oponent_lvl
    poz = get_chenar(hex_crd, mouse_pozition, r)
    if poz is not None:
        x, y = poz

        if oponent_lvl == PVP:
            status = pvp(game_state, poz)
            if status is not None:
                end_game(status)

        else:  # Oponentul este un AI
            if game_state.build_wall(x, y):
                set_wall(draweble_table, poz)
                print(oponent_lvl)
                status = play_ai(game_state, diff_lvl=oponent_lvl)

                if type(status) == str:
                    end_game(status)

                soarece.position = hex_crd[status]


def init_game():
    print("I AM CALLED")
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
