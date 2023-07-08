import random
import copy

#функция отображения
def pretty_print(arr):
    print('-' * 10)
    for row in arr:
        print(*row)
    print('-' * 10)


#функция которая возвращает список из пустых элементов
def get_empty_list(arr):
    empty = []
    for i in range(4):
        for j in range(4):
            if arr[i][j] == 0:
                num = get_number_from_index(i, j)
                empty.append(num)
    return empty


#функция присваивающая элементам массива порядковые номера начиная с 1
def get_number_from_index(i, j):
    return i * 4 + j + 1


#функция переводит порядковый номер в координаты массива
def get_index_from_number(num):
    num -= 1
    x, y = num // 4, num % 4
    return x, y


#функция рандомно заносит 2 или 4 в массив
def insert_2_or_4(arr, x, y):
    if random.random() <= 0.75:
        arr[x][y] = 2
    else:
        arr[x][y] = 4
    return arr


#функция проверяет на наличие незанятых полей, т.е. 0-х элементов
def is_zero_in_array(arr):
    for row in arr:
        if 0 in row:
            return True
    return False


#функция сдвига чисел влево
def move_left(arr):
    origin = copy.deepcopy(arr)
    delta = 0  # изменение счета врезультате схлопывания
    #перемещения чисел из правой части влевую
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.append(0)
    #схлопывания одинаковых рядом стоящих цифр
    for row in range(4):
        for col in range(3):
            if arr[row][col] == arr[row][col+1] and arr[row][col] != 0:
                 arr[row][col] *= 2
                 delta += arr[row][col]
                 arr[row].pop(col+1)
                 arr[row].append(0)
    return arr, delta, not origin == arr


#функция сдвига чисел вправо
def move_right(arr: list):
    origin = copy.deepcopy(arr)
    delta = 0
    #перемещения цифр из левой части вправую
    for row in arr:
        while 0 in row:
            row.remove(0)
        while len(row) != 4:
            row.insert(0, 0)
    #схлопывания одинаковых рядом стоящих цифр
    for row in range(4):
        for col in range(3, 0, -1):
            if arr[row][col] == arr[row][col-1] and arr[row][col] != 0:
                 arr[row][col] *= 2
                 delta += arr[row][col]
                 arr[row].pop(col-1)
                 arr[row].insert(0, 0)
    return arr, delta, not origin == arr


#функция сдвига чисел вверх
def move_up(arr):
    origin = copy.deepcopy(arr)
    delta = 0
    for col in range(4):
        #собираем столбик в отдельный массив
        column = []
        for row in range(4):
            if arr[row][col] != 0:
                column.append(arr[row][col])
        while len(column) != 4:
            column.append(0)
        #схлопываем одинаковые соседние числа
        for i in range(3):
            if column[i] == column[i+1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i+1)
                column.append(0)
        #перезаписываем столбик первоначального массива
        for row in range(4):
            arr[row][col] = column[row]
    return arr, delta, not origin == arr


#функция сдвига чисел вниз
def move_down(arr):
    origin = copy.deepcopy(arr)
    delta = 0
    for col in range(4):
        #собираем столбик в отдельный массив
        column = []
        for row in range(4):
            if arr[row][col] != 0:
                column.append(arr[row][col])
        while len(column) != 4:
            column.insert(0, 0)
        #схлопываем одинаковые соседние числа справа налево
        for i in range(3, 0, -1):
            if column[i] == column[i-1] and column[i] != 0:
                column[i] *= 2
                delta += column[i]
                column.pop(i-1)
                column.insert(0, 0)
        #перезаписываем столбик первоначального массива
        for row in range(4):
            arr[row][col] = column[row]
    return arr, delta, not origin == arr


def is_can_move(arr):
    for row in range(3):
        for col in range(3):
            if arr[row][col] == arr[row][col+1] or arr[row][col] == arr[row+1][col]:
                return True
    for row in range(1, 4):
        for col in range(1, 4):
            if arr[row][col] == arr[row-1][col] or arr[row][col] == arr[row][col-1]:
                return True
    return False
