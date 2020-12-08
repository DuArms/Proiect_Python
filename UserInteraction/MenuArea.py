from UserInteraction.Parametrii import *
from GUI.GameGUI import *
from UserInteraction.GameBoardArea import *


def chenge_to_pvp():
    global oponent_lvl
    global external_function_call
    oponent_lvl = PVP
    return "RESET"


def chenge_to_hard_ai():
    global oponent_lvl
    oponent_lvl = HARD_AI



def chenge_to_medium_ai():
    global oponent_lvl
    oponent_lvl = MEDIUM_AI


def chenge_to_easy_ai():
    global oponent_lvl
    oponent_lvl = EASY_AI


def reset():
    global init_game
    global external_function_call
    return "RESET"


text = ["P Vs P ", "P Vs EASY AI", "P Vs MEDIUM AI", "P Vs HARD AI", "RESET"]
functii = [chenge_to_pvp, chenge_to_easy_ai, chenge_to_medium_ai, chenge_to_hard_ai, reset]

pos = menu_area[0]
for text, cbf in zip(text, functii):
    buttons.append(Button(pos, BLUE, text, button_size, cbf))
    pos = pos + [0, button_size[1] + 10]


def menu_click(mouse_pozition, buttons, draweble_table):
    global  imgs , oponent_lvl
    for bt in buttons:
        if bt.check_if_clicked(mouse_pozition):
            print(bt.text)
            if "RESET" == bt.call_fn():
                imgs[0].position = hex_crd[NUMAR_LINII // 2, NUMAR_COLOANE // 2]
                draweble_table = init_game()


            print(oponent_lvl)

    return draweble_table
