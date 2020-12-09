from Game.Rules.GameState import *
from GUI.GameGUI import *

def pvp(game_gui,game_state=GameState(),poz=(-1,-1),tura=1):
    '''
    Functie ce menegenriaza jocul intre 2 utilizatori umani.
    :param game_gui:
    :param game_state:
    :param poz:
    :param tura:
    :return status , tura:
    '''
    x,y = poz
    mouse_moves = game_state.get_mouse_moves()

    if game_state.valid_move(x, y, [GameState.SPATIU, GameState.VIZITAT]):
        if tura == 1:  # joaca soarecele
            if (x, y) in mouse_moves:
                game_state.move_mouse(x, y)
                game_gui.soarece.position = game_gui.hex_crd[poz]
                tura = 1 - tura
        else:  # joaca zidul
            if game_state.build_wall(x, y):
                game_gui.set_wall(poz)
                tura = 1 - tura

    status = game_state.is_game_done(len(mouse_moves))
    return  status , tura