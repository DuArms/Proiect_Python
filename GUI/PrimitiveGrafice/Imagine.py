from resurse.constants import *

class Imagine:

    def __init__(self , poza , coordonate ):
        self.img = poza
        self.position = coordonate

    def get_pos_2_draw(self):
        x, y = self.position
        x -= R * 0.8
        y -= R

        return (x, y)