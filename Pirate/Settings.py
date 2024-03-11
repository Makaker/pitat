#2
level_map = [
'XXXXXX                                                          X',
'XXXXXX                                                   XXXXXX X',
'XXXXXX                                              XXXXXXXXXXX X',
'XXXXXX                                                          X',
'XXXXXX                                                          X',
'XXXXXX                   XXX                     XX             X',
'XXXXXX                                                          X',
'XXXXXX                                                          X',
'XXXXXX              XXXXXXX   XXXXXX   X  X  XXXXXXXXX    XXXXXXX',
'XXXXXX  P    XXXXXXXXXXXXXX   XXXXXX         XXXXXXXXX    XXXXXXX',
'XXXXXXXXXXXXXXXXXXXXXXXXXXX   XXXXXX         XXXXXXXXX    XXXXXXX',
'XXXXXX                     XXX      XXXXXXXXXX                  X',
'XXXXXX                                                          X',
'XXXXXX                                                  XX      X',
'XXXXXX                                              XXX        X',
'XXXXXX                                           XXX            X',
'XXXXXX                                      XXX                 X',
'XXXXXX                                                          X',
'XXXXXX                                                          X',
'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX']    # создали уровень (карту) в виде списка со строками

tile_size = 64        # размер плитки в пикселях - на карте это один Х
screen_width = 1370   # ширена экрана в пикселях
screen_height = 700
# screen_height = len(level_map) * tile_size  # высота экрана - длина списка level_map на размер плитки, таким
# образом мы привезали высоту экрана к размеру плитки
print(len(level_map)) # - длина списка
print(len(level_map) * tile_size) # - ширина экранана в пикселях


