import numpy as np

# Culori
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
ORENGE = (255, 165, 0)

VERDE_EXTERIOR = (9, 74, 24)
VERDE_MIJLOC = (105, 189, 21)
VERDE_INTERIOR = (4, 212, 60)

# Constatne tabla
GAME_WIDTH = 1366
GAME_HIGHT = 720

NUMAR_LINII = 11
NUMAR_COLOANE = 11

R = 30
# Matematice
PI = np.math.pi
UNGHI_HEXAGON = 1.0471975512
# Constante de debug

SOMN = 15
#Constante de joc

HARD_AI = 3
MEDIUM_AI = 2
EASY_AI = 1
PVP = 0
RESET = -1

ZONE_ADIACENTE = list(zip(
    [-1, -1, -1, 0, 0, 1, 1, 1],
    [-1, 0, 1, -1, 1, -1, 0, 1]
))
