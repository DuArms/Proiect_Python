from constants import *


def update_pozitie_soarece( pozitie_curenta,tabla_de_joc):

   #Random for test
    if np.random.randint(0,2):
        pozitie_curenta[0] += 1
        if pozitie_curenta[0] == NUMAR_COLOANE:
            pozitie_curenta[0] = 0
    else:
        pozitie_curenta[1] += 1
        if pozitie_curenta[1] == NUMAR_LINII:
            pozitie_curenta[1] = 0
    return  pozitie_curenta