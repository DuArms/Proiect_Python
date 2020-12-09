from resurse.utilitare import calc_hex_crd
from GUI.PrimitiveGrafice.Imagine import Imagine
from GUI.PrimitiveGrafice.Button import Button
from resurse.constants import *

import pygame


# Set up the drawing window
class GameGUI:
    poza_soarece = pygame.image.load("./resurse/rat.png")
    poza_soarece = pygame.transform.scale(poza_soarece, (52, 52))
    r = R
    p = [250, r]
    def __init__(self):
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode([GAME_WIDTH, GAME_HIGHT])

        self.hex_crd = calc_hex_crd(GameGUI.p, GameGUI.r)

        self.soarece = Imagine(
            GameGUI.poza_soarece,
            self.hex_crd[NUMAR_LINII // 2, NUMAR_COLOANE // 2]
        )

        self.imgs = [self.soarece]

        self.draweble_table = []

        self.game_area = [
            self.hex_crd[0, 0] + [-5 / 2 * GameGUI.r, -3 / 2 * GameGUI.r],
            self.hex_crd[-1, -1] + [-7 / 2 * GameGUI.r, +1 / 2 * GameGUI.r]
        ]

        self.menu_area = [
            self.game_area[0] + [self.game_area[1][0] + GAME_WIDTH / 15, 0],
            (300, self.game_area[1][1])
        ]

        self.menu_width = self.menu_area[1][0]
        self.menu_hight = self.menu_area[1][1]

        self.button_size = (self.menu_width * 0.90, self.menu_hight * (1 / 8))
        self.buttons = []

        pass

    def draw(self):
        '''
        Deseneaza elementele grafice pe ecran.
        :return:
        '''
        # Fill the background with white
        self.screen.fill(WHITE)

        # Deseneaza tabla
        pygame.draw.rect(self.screen, BLACK, self.game_area, 2)

        for value in self.draweble_table:
            for poly, culoare in value:
                pygame.draw.polygon(self.screen, culoare, poly)

        # Deseneaza meniu
        for bt in self.buttons:
            bt.draw(self.screen)

        # Deseneaza soarece
        for img in self.imgs:
            self.screen.blit(img.img, img.get_pos_2_draw())

        pygame.display.flip()

        self.clock.tick(60)

    def set_wall(self, poz):
        '''
        Coloreaza un zid
        :param poz:
        :return:
        '''
        poz = poz[0] * NUMAR_COLOANE + poz[1]
        hexagon = self.draweble_table[poz][0][0]
        hexagon1 = self.draweble_table[poz][1][0]
        self.draweble_table[poz] = [(hexagon, RED), (hexagon1, ORENGE)]


game_gui = GameGUI()
