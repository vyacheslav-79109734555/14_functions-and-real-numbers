# Задача 5. Наименьший делитель


def smallest_divisor(numb):
    i = 1
    while i < numb:
        i = i + 1
        if numb % i == 0:
            return i


# обеспечил контроль ввода
while True:
    numb = input('Введите натуральное число n > 1: ')
    if numb.isdigit() and int(numb) > 1:
        numb = int(numb)

        print('Функция найдет наименьший делитель числа:', numb, 'отличный от 1')
        break
    else:
        print('Введите натуральное число n > 1:')

i = smallest_divisor(numb)
print('Наименьший делитель, отличный от единицы =', i)
