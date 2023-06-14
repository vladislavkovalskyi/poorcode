# 🏠 • Домашнее задание (дедлайн 14.06):
# • Написать достаточно сложный декоратор, который позволит красиво писать функцию, в аргументы которой ты будешь передавать код,
# а декоратор будет рисовать в консоле красивую таблицу.
# Условие: Функция принимает только список с словарями

VERTICALLY = "┃"
VERTICALLY_RIGHT = "┣"
VERTICALLY_LEFT = "┫"

HORIZONTALLY = "━"
HORIZONTALLY_BOTTOM = "┳"
HORIZONTALLY_TOP = "┻"

BOTTOM_RIGHT = "┏"
BOTTOM_LEFT = "┓"

TOP_RIGHT = "┗"
TOP_LEFT = "┛"

CROSS = "╋"


def framer(func):
    def wrapper(data=[], title_spaces = 3):
        if not data:
            print("Произошла ошибка. Передайте список со словарём.")
            return
        func(data, title_spaces)
        spaces = " " * title_spaces
        # Здесь у нас хранятся список всех ключей словаря
        keys = list(data[0].keys())
        for i in range(len(keys)):
            keys[i] = f"{spaces}{keys[i]}{spaces}"
        # Здесь мы создали f-string для того, чтобы там сохранялись все наши ключи через вертикальную палочку
        # Она нам понадобиться позже для того, чтобы нарисовать ровную линию, такой же длины
        row = f"{VERTICALLY} {(' ' + VERTICALLY + ' ').join(keys)} {VERTICALLY}"

        print(BOTTOM_RIGHT,  HORIZONTALLY * (len(row) - 2), BOTTOM_LEFT, sep="")
        print(row)
        crosses_range = []
        for i, key in enumerate(keys):
            if i != len(keys) - 1:
                crosses_range.append(len(key) + 3)
        print(VERTICALLY_RIGHT, end="")
        total_row = ""
        for length in crosses_range:
            cross_row = f"{HORIZONTALLY * (length - 1)}{CROSS}"
            total_row += cross_row
            print(cross_row, end="")
        print(HORIZONTALLY * (len(row) - len(total_row) - 2), end=VERTICALLY_LEFT + "\n")

        for element in data:
            print(VERTICALLY, end=" ")
            for key in keys:
                print(element[key.replace(" ", "")], end=(" " * (len(key) - len(str(element[key.replace(" ", "")])) + 1) + VERTICALLY + " "))
            print()

        print(TOP_RIGHT, HORIZONTALLY * (len(row) - 2), TOP_LEFT, sep="")
    return wrapper


@framer
def draw_frame(data=[], title_spaces = 3):
    print("Вот твоя красивая таблица:")


data = [
    {"username": "Ярослав", "surname": "Жук", "password": "yar111", "balance": 1522525},
    {"username": "Адам", "surname": "Кацапов", "password": "adam222", "balance": 1000},
    {"username": "Владислав", "surname": "Пингвин", "password": "vlad222", "balance": 1000000},
    {"username": "Михаил", "surname": "Круг", "password": "mishafff", "balance": 124442}
]

draw_frame(data, 5)
