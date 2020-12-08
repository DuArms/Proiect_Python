from GameRules.GameState import *
from AiLogic.RandomAI import random_logic
from AiLogic.DeterministicAi import deterministic_logic


def play_ai(game_state=GameState(), diff_lvl=1):
    moves = game_state.get_mouse_moves()
    nr_mutari = len(moves)

    game_done = game_state.is_game_done(nr_mutari)

    if game_done is not None:
        return game_done

    decision_making = None

    if diff_lvl == 1:
        decision_making = random_logic
    elif diff_lvl ==2:
        if np.random.random() < 0.5:
            decision_making = deterministic_logic
        else:
            decision_making = random_logic
    elif diff_lvl == 3:
        decision_making = deterministic_logic

    x, y = decision_making(game_state, moves, nr_mutari)
    game_state.move_mouse(x, y)

    return x, y
