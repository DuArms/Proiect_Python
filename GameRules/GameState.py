from resurse.constants import *

class GameState:
    SOARECE = 1
    SPATIU = 0
    ZID = -1
    VIZITAT = -2

    MSG_LOST = "MOUSE_WIN"
    MSG_WON = "WALL_WIN"

    def __init__(self, crd_soarece=(NUMAR_LINII // 2, NUMAR_COLOANE // 2)):
        self.tabla = np.zeros((NUMAR_LINII, NUMAR_COLOANE))
        self.crd_soarece = np.array(crd_soarece)
        self.tabla[crd_soarece] = GameState.SOARECE

    def valid_move(self, x, y, poz_libere=None):
        if 0 <= x < NUMAR_LINII and 0 <= y < NUMAR_COLOANE and self.tabla[x, y] in poz_libere:
            return True
        return False

    def get_mouse_moves(self,criteriu=None):
        if criteriu is None:
            criteriu = [GameState.SPATIU, GameState.VIZITAT]

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

    def move_mouse(self, x, y):
        if self.valid_move(x, y , [GameState.SPATIU, GameState.VIZITAT]):
            self.tabla[self.crd_soarece[0], self.crd_soarece[1]] = GameState.VIZITAT
            self.crd_soarece = np.asarray((x, y))
            self.tabla[x, y] = GameState.SOARECE

            return True
        return False

    def build_wall(self, x, y):
        if self.valid_move(x, y, [GameState.VIZITAT, GameState.SPATIU]):
            self.tabla[x, y] = GameState.ZID
            return True
        return False

    def is_game_done(self, numar_mutari):
        if self.crd_soarece[0] in [0, NUMAR_LINII - 1] or self.crd_soarece[1] in [0, NUMAR_COLOANE - 1]:
            return GameState.MSG_LOST
        if numar_mutari == 0:
            return GameState.MSG_WON

        return None




if __name__ == "__main__":
    x = GameState()
    a = x.get_mouse_moves()
    print(a)
