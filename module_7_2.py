# Домашнее задание по теме "Позиционирование в файле".

def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding="utf-8")
    strings_positions = {}
    for nl, string in enumerate(strings, start=1):
        byte = file.tell()
        file.write(string + '\n')
        strings_positions[nl, byte] = string
    file.close()
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)




