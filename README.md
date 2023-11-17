# Игра 2048

Это простая версия популярной игры 2048 написанная с использованием графики на Pygame. Цель игры - сдвигать числовые плитки на игровом поле, чтобы объединять их и получить плитку со значением 2048.

## Управление
- Используйте стрелки (вверх, вниз, влево, вправо) для перемещения плиток на поле.
- Нажмите кнопку X в верхнем левом углу окна игры, чтобы закрыть игру.

## Сохранение прогресса
Если вы закроете игру до достижения конца игры (Game Over), ваш прогресс, имя игрока и счет будут сохранены. При следующем открытии игры вы сможете продолжить с того места, где остановились.

## Варианты после Game Over
После достижения Game Over у вас есть три варианта для продолжения игры:

1. Закрыть приложение, нажав на кнопку X, и перезапустить игру.
2. Нажать клавишу Enter, чтобы перейти в меню выбора имени игрока. После ввода имени вы сможете продолжить игру.
3. Нажать клавишу Space, чтобы возобновить игру с тем же именем игрока.

# Перед запуском проекта нужно провести некоторые настройки

### Установка venv
1. Если у вас еще не установлен модуль venv, выполните следующую команду в командной строке, чтобы установить его:
**pip install venv**


### Установка зависимостей
1. Перейдите в корневую папку проекта.

2. Активируйте виртуальное окружение venv следующей командой:
**source venv/bin/activate**

или для Windows:
**venv\Scripts\activate**

3. Установите зависимости, указанные в файле requirements.txt, выполнив следующую команду:
**pip install -r requirements.txt**


### Запуск скрипта

1. В корневой папке проекта выполните команду для перехода в дирректорию с игрой:
**cd 2048**

2. Запускаем саму игру командой:
**python main.py**

---
Приятной игры в 2048!
