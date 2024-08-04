# Дополнительное практическое задание по модулю: "Основные операторы"
number = int(input('Введите число из первого поля (от 3 до 20): '))
code = ''
for i in range(1, 20):
     for n in range (1, 20):
         if number % (i + n) != 0:
             continue
         elif n > i:
             code += str(i) + str(n)
print('Число для второго поля:', code)
