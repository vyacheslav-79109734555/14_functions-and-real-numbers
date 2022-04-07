#
# www_n_1(N) - название функции
# x - счетчик
# reverse_n_1
# remainder_of_number_1 --- остаток от числа
# remainder_of_number_2 --- остаток от числа
# count - переменная
#
# www - вызов функции разворота числа

#
#
def www_n_1(N):
    x = 0
    remainder_of_number_1 = round(N, 1) // 1
    print(remainder_of_number_1)
    while remainder_of_number_1 > 0:
        count = remainder_of_number_1 % 10
        remainder_of_number_1 = remainder_of_number_1 // 10
        x = x * 10
        x = x + count
        print(x)
        return x


while True:
    n_1 = input('Введите первое число: ')
    # n_2 = input('Введите второе число: ')
    if n_1.isdigit() or len(n_1) > 0:
        print('ok')
        break
    else:
        print('что то пошло не так, попробуй еще раз: ')

reverse_n_1 = www_n_1(n_1)
print("1ое число наоборот: ", reverse_n_1)

# if n_1.isdigit() and n_2.isdigit() or len(n_1) > 0 and len(n_2) > 0:
