import unittest

from logics import *


class Test2048(unittest.TestCase):
    #тесты для функции перевода позиции числа в массивк в порядковый номер
    def test_1(self):
        self.assertEqual(get_number_from_index(1, 2), 7)

    def test_2(self):
        self.assertEqual(get_number_from_index(3, 3), 16)

    #тесты для функции получения порядкового номера только 0-х элементов
    def test_3(self):
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        game_table = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(game_table), arr)

    def test_4(self):
        arr = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
        game_table = [
            [2, 2, 2, 2],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(get_empty_list(game_table), arr)

    def test_5(self):
        arr = [5, 7, 8, 9, 10, 12, 13, 14, 15]
        game_table = [
            [2, 2, 2, 2],
            [0, 2, 0, 0],
            [0, 0, 4, 0],
            [0, 0, 0, 4]
        ]
        self.assertEqual(get_empty_list(game_table), arr)

    def test_6(self):
        arr = []
        game_table = [
            [2, 2, 2, 2],
            [4, 2, 8, 2],
            [2, 2, 4, 8],
            [2, 8, 4, 4]
        ]
        self.assertEqual(get_empty_list(game_table), arr)

    def test_7(self):
        arr = [1, 8, 11]
        game_table = [
            [0, 2, 2, 2],
            [4, 2, 8, 0],
            [2, 2, 0, 8],
            [2, 8, 4, 4]
        ]
        self.assertEqual(get_empty_list(game_table), arr)

    #тесты для функции получения позиции числа из порядкового номера
    def test_8(self):
        self.assertEqual(get_index_from_number(7), (1, 2))

    def test_9(self):
        self.assertEqual(get_index_from_number(3), (0, 2))

    def test_10(self):
        self.assertEqual(get_index_from_number(16), (3, 3))

    def test_11(self):
        self.assertEqual(get_index_from_number(1), (0, 0))

    #тесты для функции проверки что есть ещё нулевые елементы в массиве
    def test_12(self):
        game_table = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self.assertEqual(is_zero_in_array(game_table), False)

    def test_13(self):
        game_table = [
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 0]
        ]
        self.assertEqual(is_zero_in_array(game_table), True)

    def test_14(self):
        game_table = [
            [0, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2],
            [2, 2, 2, 2]
        ]
        self.assertEqual(is_zero_in_array(game_table), True)

    #тесты для функции сдвиг чисел влево и схлопывание одинаковых рядом стоящих
    def test_15(self):
        game_table = [
            [2, 2, 0, 0],
            [0, 4, 4, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        result = [
            [4, 0, 0, 0],
            [8, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_left(game_table), (result, 12))

    def test_16(self):
        game_table = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [0, 0, 0, 0],
            [8, 8, 4, 4]
        ]
        result = [
            [2, 8, 2, 0],
            [4, 2, 0, 0],
            [0, 0, 0, 0],
            [16, 8, 0, 0]
        ]
        self.assertEqual(move_left(game_table), (result, 32))

    #тесты для функции сдвиг чисел вправо и схлопывание одинаковых рядом стоящих
    def test_17(self):
        game_table = [
            [2, 4, 4, 2],
            [4, 0, 0, 2],
            [2, 0, 2, 0],
            [8, 8, 4, 4]
        ]
        result = [
            [0, 2, 8, 2],
            [0, 0, 4, 2],
            [0, 0, 0, 4],
            [0, 0, 16, 8]
        ]
        self.assertEqual(move_right(game_table), (result, 36))

    # тесты для функции сдвиг чисел вверх и схлопывание одинаковых рядом стоящих
    def test_18(self):
        game_table = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        result = [
            [4, 8, 4, 2],
            [8, 0, 0, 4],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.assertEqual(move_up(game_table), (result, 24))

    # тесты для функции сдвиг чисел вниз и схлопывание одинаковых рядом стоящих
    def test_19(self):
        game_table = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        result = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [4, 0, 0, 2],
            [8, 8, 4, 4]
        ]
        self.assertEqual(move_down(game_table), (result, 24))

    #тесты для проверки функции на возможность схлопывания при перемещении в одну из сторон
    def test_20(self):
        game_table = [
            [2, 4, 0, 2],
            [2, 0, 2, 0],
            [4, 0, 2, 4],
            [4, 4, 0, 0]
        ]
        self.assertEqual(is_can_move(game_table), True)

    def test_21(self):
        game_table = [
            [2, 4, 8, 16],
            [128, 32, 512, 8],
            [4, 16, 256, 32],
            [32, 128, 4, 2]
        ]
        self.assertEqual(is_can_move(game_table), False)


if __name__ == "__main__":
    unittest.main()
