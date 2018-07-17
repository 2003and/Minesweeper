import pygame as pg
import random as rd
from time import sleep


def play(mines):
    global view_field
    global field
    view_field = [[1 for i in range(scale)] for i in range(scale)]
    field = [[0 for i in range(scale)] for i in range(scale)]
    while mines > 0:
        for i in range(scale):
            if mines != 0:
                for j in range(scale):
                    if mines == 0:
                        break
                    else:
                        if rd.randint(0, 10) < 1 and not field[i][j]:
                            field[i][j] = 1
                            mines -= 1
    for i in range(scale):
        for j in range(scale):
            if (count_mines(j, i) > 0) and not (field[i][j] == 1):
                field[i][j] = count_mines(j, i) + 2
    dead = 0
    while not dead:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if not dead:
                        check_for_empty(pg.mouse.get_pos()[1] // tile_size, pg.mouse.get_pos()[0] // tile_size)
                        view_field[pg.mouse.get_pos()[0] // tile_size][pg.mouse.get_pos()[1] // tile_size] = 0
                        if field[pg.mouse.get_pos()[0] // tile_size][pg.mouse.get_pos()[1] // tile_size] == 1:
                            dead = 1
                            for i in range(scale):
                                for j in range(scale):
                                    if field[i][j] == 1:
                                        view_field[i][j] = 0

        for i in range(scale):
            for j in range(scale):
                if view_field[i][j] == 1:
                    screen.blit(tiles[2], [i * tile_size, j * tile_size])
                else:
                    screen.blit(tiles[field[i][j]], [i * tile_size, j * tile_size])
        if dead:
            screen.blit(font.render('You died!', True, (255, 30, 30)),
                        [scale * tile_size // 2 - len('You died!') * 23 // 2, scale * tile_size // 2 - 10])
        pg.display.flip()
        if dead:
            sleep(3)


def setup():
    pg.init()
    global tiles
    global font
    global font2
    global screen
    global scale
    global tile_size
    tiles = []
    tile_size = 30
    scale = 10
    font = pg.font.SysFont(None, 50, True, True)
    font2 = pg.font.SysFont(None, 50, False, False)
    screen = pg.display.set_mode([scale * tile_size, scale * tile_size])
    raw = pg.image.load('tiles.png')
    for i in range(3):
        surf = pg.Surface([10, 10])
        surf.blit(raw, [-i * 10, 0])
        surf = pg.transform.scale(surf, [tile_size, tile_size])
        tiles.append(surf)
    for i in range(3):
        surf = pg.Surface([10, 10])
        surf.blit(raw, [-i * 10, -10])
        surf = pg.transform.scale(surf, [tile_size, tile_size])
        tiles.append(surf)
    for i in range(3):
        surf = pg.Surface([10, 10])
        surf.blit(raw, [-i * 10, -20])
        surf = pg.transform.scale(surf, [tile_size, tile_size])
        tiles.append(surf)
    for i in range(3):
        surf = pg.Surface([10, 10])
        surf.blit(raw, [-i * 10, -30])
        surf = pg.transform.scale(surf, [tile_size, tile_size])
        tiles.append(surf)


def check_for_empty(x, y):
    global view_field
    if y - 1 >= 0:
        if x + 1 < scale:
            if field[y - 1][x + 1] == 0 and not view_field[y - 1][x + 1] == 0:
                view_field[y - 1][x + 1] = 0
                check_for_empty(x + 1, y - 1)
            elif field[y - 1][x + 1] != 1 and not view_field[y - 1][x + 1] == 0:
                view_field[y - 1][x + 1] = 0
    if y - 1 >= 0:
        if field[y - 1][x] == 0 and not view_field[y - 1][x] == 0:
            view_field[y - 1][x] = 0
            check_for_empty(x, y - 1)
        elif field[y - 1][x] != 1 and not view_field[y - 1][x] == 0:
            view_field[y - 1][x] = 0
    if y - 1 >= 0:
        if x - 1 >= 0:
            if field[y - 1][x - 1] == 0 and not view_field[y - 1][x - 1] == 0:
                view_field[y - 1][x - 1] = 0
                check_for_empty(x - 1, y - 1)
            elif field[y - 1][x - 1] != 1 and not view_field[y - 1][x - 1] == 0:
                view_field[y - 1][x - 1] = 0
    if x + 1 < scale:
        if field[y][x + 1] == 0 and not view_field[y][x + 1] == 0:
            view_field[y][x + 1] = 0
            check_for_empty(x + 1, y)
        elif field[y][x + 1] != 1 and not view_field[y][x + 1] == 0:
            view_field[y][x + 1] = 0
    if x - 1 >= 0:
        if field[y][x - 1] == 0 and not view_field[y][x - 1] == 0:
            view_field[y][x - 1] = 0
            check_for_empty(x - 1, y)
        elif field[y][x - 1] != 1 and not view_field[y][x - 1] == 0:
            view_field[y][x - 1] = 0
    if y + 1 < scale:
        if x + 1 < scale:
            if field[y + 1][x + 1] == 0 and not field[y + 1][x + 1] == 0:
                view_field[y + 1][x + 1] = 0
                check_for_empty(x + 1, y + 1)
            elif field[y + 1][x + 1] != 1 and not field[y + 1][x + 1] == 0:
                view_field[y + 1][x + 1] = 0
    if y + 1 < scale:
        if field[y + 1][x] == 0 and not field[y + 1][x] == 0:
            view_field[y + 1][x] = 0
            check_for_empty(x, y + 1)
        elif field[y + 1][x] != 1 and not field[y + 1][x] == 0:
            view_field[y + 1][x] = 0
    if y + 1 < scale:
        if x - 1 >= 0:
            if field[y + 1][x - 1] == 0 and not view_field[y + 1][x - 1] == 0:
                view_field[y + 1][x - 1] = 0
                check_for_empty(x - 1, y + 1)
            elif field[y + 1][x - 1] != 1 and not view_field[y + 1][x - 1] == 0:
                view_field[y + 1][x - 1] = 0


def count_mines(x, y):
    count = 0
    if y - 1 >= 0:
        if x + 1 < scale:
            if field[y - 1][x + 1] == 1:
                count += 1
    if y - 1 >= 0:
        if field[y - 1][x] == 1:
            count += 1
    if y - 1 >= 0:
        if x - 1 >= 0:
            if field[y - 1][x - 1] == 1:
                count += 1
    if y + 1 < scale:
        if x + 1 < scale:
            if field[y + 1][x + 1] == 1:
                count += 1
    if y + 1 < scale:
        if field[y + 1][x] == 1:
            count += 1
    if y + 1 < scale:
        if x - 1 >= 0:
            if field[y + 1][x - 1] == 1:
                count += 1
    if x + 1 < scale:
        if field[y][x + 1] == 1:
            count += 1
    if x - 1 >= 0:
        if field[y][x - 1] == 1:
            count += 1
    return count


setup()

while True:
    screen.fill((0, 0, 0))
    screen.blit(font2.render('PRESS SPACE', False, (255, 255, 255)),
                [scale * tile_size // 2 - len('PRESS SPACE') * 23 // 2, scale * tile_size // 2 - 10])
    for event in pg.event.get():
        if event.type == pg.QUIT:
            quit()
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                play(15)
    pg.display.flip()
