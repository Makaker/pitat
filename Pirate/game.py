# 1
# 1 - дисплей
# 2 - подгружается класс Level с изображением карты  на экран
# 3 - бесконечный цикл и услевие для  отслеживания кнопки выхода
# 4 - в цикле есть заливка экрана
# 5 - в цикле есть класс Level с методом run - в нём есть прорисовка героя и его обновления для движения и так же сплитки
# 6 - в цикле обновление дисплея и время
import pygame, sys
from Settings import *
from Level import Level  # импортировали класс Level из файла Level

pygame.init()  # с этой иницилизации начинается код в пайгейме

screen = pygame.display.set_mode((screen_width, screen_height))  # задали размеры дисплея
clock = pygame.time.Clock()  # подключили время
level = Level(level_map, screen)  # переменная level - импортированый класс Level с переменными уровень и экран

while True:
    for event in pygame.event.get():  # условие для остлеживания событей
        if event.type == pygame.QUIT:  # отслеживаем нажатие кнопки закрыть
            pygame.quit()
            sys.exit()  # выходим из игры

    screen.fill((145, 137, 137))  # заливка основного экрана
    level.run()  # в цикл засунули функцию (метод) запуска уровня(обновление и проросовка спрайтов)

    pygame.display.update()  # обновление дисплея, для анимации
    clock.tick(60)  # fps
