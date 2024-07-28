# Практическое задание по теме: "Словари и множества"

my_dict = {'Ruslan': 2002, 'Maksim': 1999, 'Ildar': 2001, 'Maria': 1999}
print(my_dict, my_dict['Ruslan'], my_dict.get('Ivan', 'Значение по заданному ключу не найдено'),  sep='\n')
my_dict.update({'Sergey': 1987, 'Vasilisa': 2000})
entry_from_dict = my_dict.pop('Maksim')
print(entry_from_dict)
print(my_dict, end='\n\n')

my_set = {65, False, 'Sunset', 65, True, False, 24, 'Sunrise'}
print(my_set)
my_set |= {10101, 'Moon'}
my_set.discard(False)
print(my_set)
