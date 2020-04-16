import pygame

_OFFSET = 15

class Bar:
    def __init__(self, speed, dim, image):
        self.speed = speed
        self.image = pygame.transform.scale(image, (80, 10))
        self.rect = self.image.get_rect()
        self.dim = dim
        self.rect.top = dim[1] - _OFFSET
    def move(self, mouseX):
        if mouseX < 0:
            return
        if mouseX > self.dim[0]:
            # print(self.dim[0])
            return
        self.rect.left = mouseX


