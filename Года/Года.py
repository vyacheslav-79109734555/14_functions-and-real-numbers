# Задача 7. Года

def special_years(year_start, year_stop):
    x = int(year_start)
    y = int(year_stop)
    i = 0
    for year in range(x, y + 1):
        i = year
        n_1 = i % 10
        i //= 10
        n_2 = i % 10
        i //= 10
        n_3 = i % 10
        i //= 10
        n_4 = i % 10
        i //= 10
        if (n_1 == n_2 == n_3) or (n_1 == n_2 == n_4) or (n_2 == n_3 == n_4) or (n_3 == n_4 == n_1):
            print(year)


while True:
    year_start = input('Введите первый год: ')
    year_stop = input('Введите второй год: ')
    if len(year_start) == 4 and len(year_stop) == 4 and int(year_start) < int(year_stop):
        print('ok: ')
        break
    print('что то пошло не так, попробуй еще раз: ')
special_years(year_start, year_stop)
