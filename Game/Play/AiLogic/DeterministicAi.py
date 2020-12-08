from Game.Rules.GameState import *


def deterministic_logic(game_state=GameState(), mutari_posibile=None, nr_mutari=None):
    saved_game_table = game_state.tabla.copy()
    saved_moves = mutari_posibile

    maze = game_state.tabla.copy()
    maze = np.where(maze == GameState.ZID, 1000, maze)
    maze = np.where(maze == GameState.VIZITAT, GameState.SPATIU, maze)

    sx, sy = game_state.crd_soarece
    maze[sx, sy] = -10

    mutari_posibile = [
        (m[0], m[1], 1) for m in mutari_posibile
    ]

    for x, y, d in mutari_posibile:
        if maze[x, y] == GameState.SPATIU:
            maze[x, y] = d

        maze[x, y] = min(d, maze[x, y])
        game_state.move_mouse(x, y)

        for move in game_state.get_mouse_moves([GameState.SPATIU, GameState.VIZITAT]):
            if maze[move[0], move[1]] == GameState.SPATIU:
                mutari_posibile.append((move[0], move[1], d + 1))

    #print(maze)
    maze = np.where(maze == GameState.SPATIU, 1000, maze)

    busola = {
        "south": (0, np.argmin(maze[0, :])),
        "north": (NUMAR_LINII - 1, np.argmin(maze[-1, :])),
        "east": (np.argmin(maze[:, 0]), 0),
        "west": (np.argmin(maze[:, -1]), NUMAR_COLOANE - 1)
    }

    closest_exit = busola["south"]
    for value in busola.values():
        if maze[value] < maze[closest_exit]:
            closest_exit = value
        elif maze[value] == maze[closest_exit] and np.random.randint(100) < 66:
            closest_exit = value

    #print(maze)

    rez = closest_exit
    #print(rez, maze[rez])

    if maze[closest_exit] == 1000:
        rez = saved_moves[np.random.randint(0, len(saved_moves))]
    else:
        while rez not in saved_moves:
            for x, y in ZONE_ADIACENTE:
                x, y = x + rez[0], y + rez[1]
                if game_state.valid_move(x, y, [GameState.SPATIU, GameState.VIZITAT]):
                    if 0 < maze[x, y]+1 == maze[rez]:
                        rez = (x, y)

    #print(rez)
    game_state.move_mouse(sx, sy)
    game_state.tabla = saved_game_table

    return rez


if __name__ == "__main__":
    gs = GameState()
    pm = gs.get_mouse_moves()
    deterministic_logic(gs, pm, len(pm))
