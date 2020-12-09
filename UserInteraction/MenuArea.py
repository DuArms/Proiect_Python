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

pos = game_gui.menu_area[0]
for text, cbf in zip(text, functii):
    game_gui.buttons.append(Button(pos, (45,34,104), text,  game_gui.button_size, cbf))
    pos = pos + [0,  game_gui.button_size[1] + 10]


def menu_click(mouse_pozition, game_gui):
    '''
    Functie ce menegeriaza interactiunea cu meniul
    :param mouse_pozition:
    :param game_gui:
    :return:
    '''
    global  opponent_lvl
    for bt in game_gui.buttons:
        if bt.check_if_clicked(mouse_pozition):
            if bt.call_fn is not None:
                result = bt.call_fn()
                if "RESET" == result:
                    game_gui.imgs[0].position = game_gui.hex_crd[NUMAR_LINII // 2, NUMAR_COLOANE // 2]
                    game_gui = init_game()
                elif type(result) == int:
                    opponent_lvl = result


    return game_gui ,opponent_lvl
