import numpy as np
from resurse.constants import *

cos = np.math.cos
sin = np.math.sin

def poly_points(point=(0, 0), raza=100, n=6):
    '''
    Genereaza coordonatele colturilor unui poligon
    :param point:
    :param raza:
    :param n:
    :return:
    '''
    corners = []
    starting_angle = 2 * PI / n
    for i in range(n):
        alpha = (i) * starting_angle + PI / 2
        new_point = (point[0] + raza * cos(alpha), point[1] + raza * sin(alpha))
        corners.append(new_point)

    return corners


def calc_hex_crd(staring_point=(0, 0), raza=25):
    '''
    Calculeaza coordonatele colturilor unui hexagon pentru a
    fi desenabil pe ecran
    :param staring_point:
    :param raza:
    :return:
    '''
    tabla = []
    coordonate_centru_tabla = []
    l_adjust = raza * cos(UNGHI_HEXAGON)
    c_adjust = raza * sin(UNGHI_HEXAGON)

    line_start = staring_point[0], staring_point[1]

    for i in range(NUMAR_LINII):
        displacement = 2.0 * raza - l_adjust
        line_start = line_start[0], line_start[1] + displacement

        tabla.append([])

        for j in range(NUMAR_COLOANE):
            displacement = 2.0 * c_adjust * j - c_adjust * (i % 2)

            hex_curent = line_start[0] + displacement, line_start[1]  # - l_adjust * (i % 2)

            tabla[-1].append(hex_curent)

    tabla = np.array(tabla)

    return tabla


def find_point(vector, raza, valoare, size):
    '''
    Functie auxiliara pentru gasirea hexagonului pe care
    a fost dat click.
    :param vector:
    :param raza:
    :param valoare:
    :param size:
    :return:
    '''
    m = size // 2
    st = 0
    dr = size - 1

    while st <= m <= dr and np.abs(vector[m] - valoare) > raza:
        if vector[m] < valoare:
            st = m + 1
        elif valoare < vector[m]:
            dr = m - 1
        m = (st + dr) // 2

    if np.abs(vector[m] - valoare) < raza:
        return m

    return None


def get_chenar(tabla, coordonate_mouse, r):
    '''
    Functie ce retuneaza indexii hexagonului pe care
    a fost dat click
    :param tabla:
    :param coordonate_mouse:
    :param r:
    :return:
    '''
    r *= 0.90
    table_y = [int(linie[0][1]) for linie in tabla]

    index_linie = find_point(table_y, r, coordonate_mouse[1], NUMAR_LINII)

    if index_linie is None:
        return None

    table_x = [int(valoare[0]) for valoare in tabla[index_linie]]
    index_coloana = find_point(table_x, r, coordonate_mouse[0], NUMAR_COLOANE)

    if index_coloana is None:
        return None

    return (index_linie, index_coloana)


def in_pyrect(area, mouse_pozition):
    '''
    Verifica daca clickul a fost dat intr-un chenar
    :param area:
    :param mouse_pozition:
    :return:
    '''
    return area[0][0] < mouse_pozition[0] < area[0][0] + area[1][0] \
           and area[0][1] < mouse_pozition[1] < area[1][1] + area[1][1]
