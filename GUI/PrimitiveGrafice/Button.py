import numpy as np
import pygame
from resurse.constants import *
pygame.init()
font = pygame.font.Font('freesansbold.ttf', 25)


class Button:

    def __init__(self, pos, cul, text, size, call_fn):
        self.pos = np.array(pos)
        self.cul = cul
        self.text = text
        self.size = np.array(size)
        self.call_fn = call_fn

    def get_rect(self):
        return [self.pos, self.size]

    def draw(self, screen):
        '''
        Deseneaza butonul pe ecran
        :param screen:
        :return:
        '''
        pygame.draw.rect(screen, self.cul, self.get_rect())
        txt = font.render(self.text, True,WHITE, self.cul)
        screen.blit(txt, self.pos + self.size * [0.2, 0.35])

    def check_if_clicked(self, click_poz):
        '''
        Verifica daca butonul a fost apasat
        :param click_poz:
        :return:
        '''
        x, y = click_poz
        sx, sy = self.pos
        return sx <= x <= sx + self.size[0] and sy <= y <= sy + self.size[1]
