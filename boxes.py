import pygame
import random
from box import SingleBox
_IMG_HEIGHT = 20

class Boxes:
    def __init__(self, dim, images):
        self.dim = dim
        self.images = images
        self.img_res = [(200, _IMG_HEIGHT), (180, _IMG_HEIGHT), (160, _IMG_HEIGHT)]
        self.box_arr = []

    def build_full_panel(self):
        total = int(self.dim[1] / _IMG_HEIGHT)

        for i in range(0, total):
            curr_width = 0
            while curr_width < self.dim[0]:
                img_select = random.randint(0, 1)
                res_select = random.randint(0, 2)
                print(img_select, res_select)
                curr = self.images[img_select]
                curr = pygame.transform.scale(curr, self.img_res[res_select])
                self.box_arr.append(SingleBox(curr, i))
                curr_width += self.img_res[res_select][0]

