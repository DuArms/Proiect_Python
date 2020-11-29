import numpy as np
from constants import *

cos = np.math.cos
sin = np.math.sin


def poly_points(point=(0, 0), raza=100, n=6):
    corners = []
    starting_angle = 2 * PI / n
    for i in range(n):
        alpha = (i) * starting_angle + PI / 2
        new_point = (point[0] + raza * cos(alpha), point[1] + raza * sin(alpha))
        corners.append(new_point)

    return corners


def generate_table(staring_point=(0, 0), raza=25):
    tabla = []
    coordonate_centru_tabla = []
    l_adjust = raza * cos(UNGHI_HEXAGON)
    c_adjust = raza * sin(UNGHI_HEXAGON)

    line_start = staring_point[0], staring_point[1]

    for i in range(NUMAR_LINII):
        displacement = 2.0 * raza   - l_adjust
        line_start = line_start[0], line_start[1] + displacement

        tabla.append([])

        for j in range(NUMAR_COLOANE):
            displacement = 2.0 * c_adjust * j - c_adjust * (i % 2)

            hex_curent = line_start[0] + displacement, line_start[1] #- l_adjust * (i % 2)

            tabla[-1].append(hex_curent)

    tabla =  np.array(tabla)

    return tabla


p = (300, 100)
r = 25

tabla = generate_table(p, r)
print(tabla)
