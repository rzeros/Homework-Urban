# Домашняя работа по уроку "Стиль кода часть II. Цикл While.
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
while len(my_list) > index:
    if my_list[index] < 0:
        break
    elif my_list[index] == 0:
        index += 1
        continue
    print(my_list[index])
    index += 1
