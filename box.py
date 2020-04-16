import pygame

class SingleBox:

    def __init__(self, speed, dim, image, pos):
        self.speed = speed
        self.image = image
        self.rect = self.image.get_rect()
        self.dim = dim
        self.rect.top = pos[1]
        self.rect.left = pos[0]

    def move_down(self):
        self.rect.top += 20

