# Задача 6. Монетка 2
# Теорема Пифагора...
# Расстояние до точки = гипотенуза треугольника со сторонами (x, y)

import math


def find_monetka():
    x = float(input('По горизонтали: '))
    y = float(input('По вертикали: '))
    r = int(input('Введите радиус: '))
    # if -1 > x_point or x_point > 1 or -1 > y_point or y_point > 1:
    if math.sqrt(x ** 2 + y ** 2) >= r:

        print('Монетки в области нет')
        find_monetka()
    else:
        print('Монетка где-то рядом')
        find_monetka()


find_monetka()
