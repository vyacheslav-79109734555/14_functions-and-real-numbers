# Задача 4. Число наоборот 3
# flag - флаг
# a - целая часть числа
# b - значение после запятой
# symbol - символ
# result - результат вычисления функции
# x - результат вычислений № 1
# y - результат вычислений № 2
# w - переменная функции
# Ввод: первое число: 123.45
# Ввод: второе число: 456.78

def revers(w):
    flag = True
    a = ''
    b = ''
    i = len(w)
    for symbol in reversed(w):
        if symbol == '.':
            flag = False
        elif flag:
            a = a + symbol
        else:
            b = b + symbol

    result = float(b + '.' + a)
    if result < 1:
        result *= 10 ** i

    return result


while True:
    numb_1 = input('Введите первое число: ')
    numb_2 = input('Введите второе число: ')
    if (len(numb_2) != 0 or len(numb_1) != 0) and (float(numb_1) > 0 and float(numb_2) > 0):
        print('ok')
        break
    print('что то пошло не так, попробуй еще раз: ')

x = revers(numb_1)
y = revers(numb_2)
print(f'\nПервое число наоборот:{x}')
print(f'\nВторое число наоборот:{y}')
print(f'\nСумма:{x + y}')
