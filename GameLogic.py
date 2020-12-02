from constants import *


class GameLogic:
    SOARECE = 1
    SPATIU = 0
    ZID = -1
    VIZITAT = -2

    MSG_LOST = "MOUSE_WIN"
    MSG_WON = "WALL_WIN"

    def __init__(self, crd_soarece=(NUMAR_LINII // 2, NUMAR_COLOANE // 2)):
        self.tabla = np.zeros((NUMAR_LINII, NUMAR_COLOANE))
        self.crd_soarece = np.array(crd_soarece)
        self.tabla[crd_soarece] = GameLogic.SOARECE
        print(self.tabla)

    def get_mouse_moves(self,criteriu=None):
        if criteriu is None:
            criteriu = [GameLogic.SPATIU,GameLogic.VIZITAT]

        if self.crd_soarece[0] % 2 == 1:
            move_x = [-1, -1, 0, 0, 1, 1]
            move_y = [-1, 0, -1, 1, -1, 0]
        else:
            move_x = [-1, -1, 0, 0, 1, 1]
            move_y = [0, 1, -1, 1, 0, 1]

        valid_move = []
        for x, y in zip(move_x, move_y):
            x, y = self.crd_soarece + np.asarray([x, y])

            if self.valid_move(x, y, criteriu):
                valid_move.append((x, y))

        return valid_move

    def valid_move(self, x, y, poz_libere=None):
        if 0 <= x < NUMAR_LINII and 0 <= y < NUMAR_COLOANE and self.tabla[x, y] in poz_libere:
            return True
        return False

    def move_mouse(self, x, y):
        if self.valid_move(x, y ,[GameLogic.SPATIU,GameLogic.VIZITAT]):
            self.tabla[self.crd_soarece[0], self.crd_soarece[1]] = GameLogic.VIZITAT
            self.crd_soarece = np.asarray((x, y))
            self.tabla[x, y] = GameLogic.SOARECE

            return True
        return False

    def build_wall(self, x, y):
        if self.valid_move(x, y, [GameLogic.VIZITAT, GameLogic.SPATIU]):
            self.tabla[x, y] = GameLogic.ZID
            return True
        return False

    def is_game_done(self, numar_mutari):
        if self.crd_soarece[0] in [0, NUMAR_LINII - 1] or self.crd_soarece[1] in [0, NUMAR_COLOANE - 1]:
            return GameLogic.MSG_LOST
        if numar_mutari == 0:
            return GameLogic.MSG_WON

        return None

    def random_logic(self, mutari_posibile, nr_mutari):
        better_moves = self.get_mouse_moves([GameLogic.SPATIU])
        if len(better_moves) > 0 :
            nr_mutari = len(better_moves)
            mutari_posibile = better_moves

        mutare_id = np.random.randint(0, nr_mutari)
        mutare = mutari_posibile[mutare_id]

        return mutare


def play_ai(game_state=GameLogic(), diff_lvl=1):
    moves = game_state.get_mouse_moves()
    nr_mutari = len(moves)

    game_done = game_state.is_game_done(nr_mutari)

    if game_done is not None:
        return game_done

    if diff_lvl == 1:
        x, y = game_state.random_logic(moves, nr_mutari)
        game_state.move_mouse(x, y)

    return x, y


if __name__ == "__main__":
    x = GameLogic()
    a = x.get_mouse_moves()
    print(a)
