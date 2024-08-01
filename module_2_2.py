# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else"
first, second, third = input('Введите первое число: '), input('Введите второе число: '), input('Введите третье число: ')
if first == second == third:
    print('Обнаружено 3 одинаковых числа')
elif first == second or first == third or second == third:
    print('Обнаружено 2 одинаковых числа')
else:
    print('Не было обнаружено одинаковых чисел')
    