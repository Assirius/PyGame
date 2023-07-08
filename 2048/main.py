import sys
import os
import json

import pygame

from logics import *
from database import get_best, insert_result


#3 лучших результата из БД где хранятся все результаты
PLAYERS_DB = get_best()

#инициализация игрового поля
def init_game():
    global game_table, score

    game_table = [[0] * BLOCKS for _ in range(BLOCKS)]
    score = 0

    empty = get_empty_list(game_table)
    random.shuffle(empty)
    random_num1 = empty.pop()
    random_num2 = empty.pop()
    x1, y1 = get_index_from_number(random_num1)
    x2, y2 = get_index_from_number(random_num2)
    game_table = insert_2_or_4(game_table, x1, y1)
    game_table = insert_2_or_4(game_table, x2, y2)


#стартовый экран приветстивия
def draw_intro():
    img2048 = pygame.image.load("logo2048.png")
    font = pygame.font.SysFont("comicsansms", 55)
    text_welcome = font.render("Welcome!", True, WHITE)
    name = "Введите имя"
    is_find_name = False

    while not is_find_name:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            elif event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    if name == "Введите имя":
                        name = event.unicode
                        continue
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN and name != "Введите имя":
                    if len(name) > 2:
                        global username
                        username = name
                        is_find_name = True
                        break

        screen.fill(BLACK)
        text_name = font.render(f"{name}", True, WHITE)
        name_coords = text_name.get_rect()
        name_coords.center = screen.get_rect().center

        screen.blit(pygame.transform.scale(img2048, (200, 200)), (10, 10))
        screen.blit(text_welcome, (230, 80))
        screen.blit(text_name, name_coords)

        pygame.display.update()

    screen.fill(BLACK)


#функция отрисовки списка топ игроков
def draw_top_players():
    font_head = pygame.font.SysFont("comicsansms", 25)
    font_player = pygame.font.SysFont("comicsansms", 20)
    text_head = font_head.render("Best tries: ", True, COLOR_TEXT)
    screen.blit(text_head, (320, 5))

    for index, (name, score) in enumerate(PLAYERS_DB):
        data = f"{index+1}. {name} - {score}"
        text_player = font_player.render(f"{data}", True, COLOR_TEXT)
        screen.blit(text_player, (320, 35 + 24 * index))


#функция отрисовки интерфейса игры
def draw_interface(score, delta=0):
    # рисуем блоки
    pygame.draw.rect(screen, WHITE, TITLE_REC)
    font_cell = pygame.font.SysFont("comicsansms", 70)
    font_score = pygame.font.SysFont("comicsansms", 48)
    font_delta = pygame.font.SysFont("comicsansms", 32)
    text_score = font_score.render("Score: ", True, COLOR_TEXT)
    text_score_value = font_score.render(f"{score}", True, COLOR_TEXT)
    screen.blit(text_score, (20, 35))
    screen.blit(text_score_value, (150, 35))
    if delta > 0:
        text_delta = font_delta.render(f"+{delta}", True, COLOR_TEXT)
        screen.blit(text_delta, (145, 65))
    pretty_print(game_table)

    draw_top_players()

    for row in range(BLOCKS):
        for col in range(BLOCKS):
            value = game_table[row][col]
            text_cell = font_cell.render(f"{value}", True, BLACK)

            w = col * SIZE_BLOCK + (col + 1) * MARGIN
            h = row * SIZE_BLOCK + (row + 1) * MARGIN + TITLE_HEIGHT_BLOCK
            pygame.draw.rect(screen, COLORS[value], (w, h, SIZE_BLOCK, SIZE_BLOCK))

            if value != 0:
                font_w, font_h = text_cell.get_size()
                text_x = w + (SIZE_BLOCK - font_w) // 2
                text_y = h + (SIZE_BLOCK - font_h) // 2
                screen.blit(text_cell, (text_x, text_y))


#функция отрисовки завешения игры
def draw_game_over():
    global username, PLAYERS_DB

    img2048 = pygame.image.load("logo2048.png")
    font = pygame.font.SysFont("comicsansms", 65)
    text_game_over = font.render("Game over!", True, WHITE)
    text_score = font.render(f"Вы набрали {score}", True, WHITE)

    best_score = PLAYERS_DB[0][1] if len(PLAYERS_DB) > 0 else 0
    if score > best_score:
        text = "Рекорд побит!"
    else:
        text = f"Рекорд {best_score}"
    text_record = font.render(f"{text}", True, WHITE)
    insert_result(name=username, score=score)

    PLAYERS_DB = get_best()
    is_decision = False
    while not is_decision:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                #перезапуск игры с тем же именем
                if event.key == pygame.K_SPACE:
                    init_game()
                    is_decision = True
                #перезапуск игры со сменой имени
                elif event.key == pygame.K_RETURN:
                    init_game()
                    username = None
                    is_decision = True

        screen.fill(BLACK)
        screen.blit(text_game_over, (220, 80))
        screen.blit(text_score, (30, 250))
        screen.blit(text_record, (30, 300))
        screen.blit(pygame.transform.scale(img2048, (200, 200)), (10, 10))
        pygame.display.update()
    screen.fill(BLACK)


#Сохранение преждевременного завершения игры
def save_game():
    data = {
        "username": username,
        "score": score,
        "game_table": game_table
    }

    with open("data.json", mode="w", encoding="utf-8") as outfile:
        json.dump(data, outfile)
        

#главный игровой цикл
def game_loop():
    global score, game_table

    # Прорисовка интерфейса игры
    draw_interface(score)
    pygame.display.update()

    # Запуск игровых событий
    while is_zero_in_array(game_table) or is_can_move(game_table):
        is_arr_move = False
        for event in pygame.event.get():
            # exit
            if event.type == pygame.QUIT:
                save_game()
                pygame.quit()
                sys.exit(0)
            # нажатия кнопок на клавиатуре
            elif event.type == pygame.KEYDOWN:
                delta = 0
                if event.key == pygame.K_LEFT:
                    game_table, delta, is_arr_move = move_left(game_table)
                elif event.key == pygame.K_RIGHT:
                    game_table, delta, is_arr_move = move_right(game_table)
                elif event.key == pygame.K_UP:
                    game_table, delta, is_arr_move = move_up(game_table)
                elif event.key == pygame.K_DOWN:
                    game_table, delta, is_arr_move = move_down(game_table)

                score += delta
                if is_zero_in_array(game_table) and is_arr_move:
                    empty = get_empty_list(game_table)
                    random.shuffle(empty)
                    random_num = empty.pop()
                    x, y = get_index_from_number(random_num)
                    game_table = insert_2_or_4(game_table, x, y)
                    print(f"Мы заполнили элемент под номером {random_num}")

                draw_interface(score, delta)
                pygame.display.update()


# Настройки параметров игрового дисплея
COLOR_TEXT = (255, 127, 0)
COLORS = {
    0: (130, 130, 130),
    2: (255, 255, 255),
    4: (255, 255, 128),
    8: (255, 255, 64),
    16: (255, 255, 32),
    32: (255, 255, 16),
    64: (255, 255, 8),
    128: (255, 255, 4),
    256: (255, 255, 2),
    512: (255, 255, 0),
    1024: (255, 255, 255)
}

WHITE = (255, 255, 255)
GRAY = (130, 130, 130)
BLACK = (0, 0, 0)

BLOCKS = 4
SIZE_BLOCK = 110
TITLE_HEIGHT_BLOCK = 110
MARGIN = 10
WIDTH = BLOCKS * SIZE_BLOCK + (BLOCKS+1) * MARGIN
HEIGHT = WIDTH + TITLE_HEIGHT_BLOCK
TITLE_REC = pygame.Rect(MARGIN, MARGIN, WIDTH - 2 * MARGIN, TITLE_HEIGHT_BLOCK - MARGIN)



#Инициализация
username = None
game_table = None
score = None
path_project = os.getcwd()
if "data.json" in os.listdir():
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        username = data.get("username")
        game_table = data.get("game_table")
        score = data.get("score")
    full_path = os.path.join(path_project, "data.json")
    os.remove(full_path)
else:
    init_game()

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2048")

#-------------------------------------------------------------------------------------------------------------

while True:
    if username is None:
        #Экран приветствия
        draw_intro()
    #игровой цикл
    game_loop()
    #Финальный экран - конца игры
    draw_game_over()
