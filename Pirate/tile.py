#3
# Класс плитки
import pygame

# клас плитки
class Tile(pygame.sprite.Sprite):  # этот класс наследуется от pygame.sprite.Sprite - т.е. спрайт и расширяет свою функциональность (в скобках класса пишется от кого наследуется)
    def __init__(self, pos, size):  # функция принимает позицию и размер плитки
        super().__init__()
        self.image = pygame.image.load('images/tile/IMG_0530.PNG')   # создали  поверхность, с размером задаваемыми в классе
        # self.image.fill('grey')    # заливка  повекрхности, плитки
        self.rect = self.image.get_rect(topleft = pos)
    def update(self, x_shift, y_shift):   # переменная сдвиг х
        self.rect.x += x_shift
        self.rect.y += y_shift

