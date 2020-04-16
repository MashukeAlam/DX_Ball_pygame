import pygame

class Ball:
    def __init__(self, speed, dim, image):
        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load('_ball.png'), (20, 20))
        self.rect = self.image.get_rect()
        self.dim = dim
        self.rect.top = dim[1] // 2

    def move(self):
        self.rect = self.rect.move(self.speed)
        if self.rect.left < 0 or self.rect.right > self.dim[0]:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom > self.dim[1]:
            return "GAME_OVER"

    def has_collided_with(self, obj_rect):
        return self.rect.colliderect(obj_rect)

    def flip_horizontal_dir(self):
        #if self.rect.left < 0 or self.rect.right > self.dim[0]:
        self.speed[1] = -self.speed[1]

    def flip_vertical_dir(self):
        #if self.rect.left < 0 or self.rect.right > self.dim[0]:
        self.speed[1] = -self.speed[1]
