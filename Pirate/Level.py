# 4 класс уровня игры
# я так понимаю что все спрайты создаются в этом классе - уровень
import pygame
from tile import Tile
# from tile_wall import Tile_Wall
from Settings import tile_size, screen_width, screen_height
from player import Player


class Level:
    # ____Init____ функция дает классу две переменных, первая - данные уровня, 2 - поверхность
    # В нашем случае это - списко с картой и наш экран
    def __init__(self, level_data, serface):

        # Переменные класса = 3 штуки, одна из наих постоянная = 0

        # level setap  - настройка уровня
        self.display_surface = serface  # переменная в класс - которая в нашем случае равна экрану creen
        self.setup_level(
            level_data)  # - функция setup_level которая выстраивает плитку принимает параметры(level_data - это список карты)
        self.world_shift_x = 0  # скорость передвежения карты
        self.world_shift_y = 0
        self.current_x = 0

    # функция, класса -  которая циклически проходит через весь список карты (level_map) и размещает плитку везде, где мы находим Х
    def setup_level(self, layout):  # принимает переменную layout - макет (принимает -список level_map )
        self.tiles = pygame.sprite.Group()  # создание группы спрайтов
        self.player = pygame.sprite.GroupSingle()  # создаем спрайт для персонажа
        # self.tiles_wall = pygame.sprite.Group()

        # цикл для получения строки и столбца для каждого Х
        for row_index, row in enumerate(
                layout):  # цикл с переменой row - ряд из переменой - layout, функции - setup_level
            for col_index, cell in enumerate(row):  # цикл для получения индекса столбца
                x = col_index * tile_size  # таким образом прорисовываем все Х, P
                y = row_index * tile_size

                if cell == 'X':  # условие - если ячейка == Х, ячейку мі получили с цикла
                    tile = Tile((x, y), tile_size)  # вызываем класс Tile с координатами и размером
                    self.tiles.add(tile)  # добовляем плитку
                elif cell == 'P':  # условие - если ячейка == Р, ячейку мі получили с цикла
                    player_sprite = Player((x, y))  # вызываем класс Player с координатами
                    self.player.add(player_sprite)
                # elif cell == 'W':
                #     tile_wall = Tile_Wall((x, y), tile_size)
                #     self.tiles_wall.add(tile_wall)

            #     print(f'{row_index},{col_index}:{cell}')    # прослеживать координаты Х
            # print(row_index)
            # print(row)

    # функция или метод для прокрутки экрана по оси Х
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < int(screen_height / 2) and direction_y < 0:
            self.world_shift_y = 8
        elif player_y > screen_height - (screen_height / 2) and direction_y > 0:
            self.world_shift_y = -8
        else:
            self.world_shift_y = 0
            player.speed = 8

        if player_x < int(screen_width / 4) and direction_x < 0:
            self.world_shift_x = 8
            player.speed = 0
        elif player_x > screen_width - (screen_width / 4) and direction_x > 0:
            self.world_shift_x = -8
            player.speed = 0
        else:
            self.world_shift_x = 0
            player.speed = 8

    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed  # прорисовка движения игрока

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                    self.current_x = player.rect.left
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
                    self.current_x = player.rect.right

        if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
            player.on_left = False
        if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
            player.on_right = False

    # for sprite in self.tiles_wall.sprites():
    #     if sprite.rect.colliderect(player.rect):
    #         if player.direction.x < 0:
    #             player.rect.left = sprite.rect.right
    #         elif player.direction.x > 0:
    #             player.rect.right = sprite.rect.left

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ceiling = True

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False

    # функция запуска уровня, прорисовка старта уровня (обновление и прорисовка)
    def run(self):

        # level tiles
        self.tiles.update(self.world_shift_x,
                          self.world_shift_y)  # обновление плитки для прокрутки карты со скоростью (аргумент) world_shift
        self.tiles.draw(
            self.display_surface)  # прорисовка плитки с параметром display_surface(координаты) - который является переменной serface этого класса
        # self.tiles_wall.update(self.world_shift)
        # self.tiles_wall.draw(self.display_surface)
        self.scroll_x()
        # player
        self.player.update()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(
            self.display_surface)  # прорисовка плитки с параметром display_surface(координаты) - который является переменной serface этого класса
