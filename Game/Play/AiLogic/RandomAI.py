from Game.Rules.GameState import  *


def random_logic(game_state, mutari_posibile, nr_mutari):
    '''
    Alege aleatoriu o mutare valida
    :param game_state:
    :param mutari_posibile:
    :param nr_mutari:
    :return mutare:
    '''
    for x, y in mutari_posibile:
        if x in [0, NUMAR_LINII - 1] or y in [0, NUMAR_COLOANE - 1]:
            return (x, y)

    better_moves = game_state.get_mouse_moves([GameState.SPATIU])
    if len(better_moves) > 0:
        nr_mutari = len(better_moves)
        mutari_posibile = better_moves

    mutare_id = np.random.randint(0, nr_mutari)
    mutare = mutari_posibile[mutare_id]

    return mutare