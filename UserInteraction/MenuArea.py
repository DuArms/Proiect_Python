from UserInteraction.GameBoardArea import *


def chenge_to_pvp():
    global opponent_lvl
    global external_function_call
    opponent_lvl = PVP
    return "RESET"


def chenge_to_hard_ai():
    return HARD_AI



def chenge_to_medium_ai():
    return MEDIUM_AI


def chenge_to_easy_ai():
   return EASY_AI


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
    global  imgs , opponent_lvl
    for bt in buttons:
        if bt.check_if_clicked(mouse_pozition):
            result = bt.call_fn()
            if "RESET" == result:
                imgs[0].position = hex_crd[NUMAR_LINII // 2, NUMAR_COLOANE // 2]
                draweble_table = init_game()
            elif type(result) == int:
                opponent_lvl = result


    return draweble_table ,opponent_lvl
