# Задача 3. Сумма и разность


def summ():
    numb = format(input('Введите одно целое положительное число N: '))
    if numb.isdigit():
        counter(numb)
    else:
        print('Ошибка ввода, введите целое число:')
        summ()


def counter(numb):
    a = int(numb)
    count = 0
    x = 0
    while a > 0:
        count += a % 10
        a //= 10
        x += 1
    print('Сумма цифр:', count)
    print('Кол-во цифр в числе:', x)
    print('Разность суммы и кол-ва цифр:', count - x)


summ()
