import pygame

class Tile_Wall(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.image.load('images/tile/IMG_0531.PNG')
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, x_shift):
        self.rect.x += x_shift