# Самостоятельная работа по уроку "Распаковка позиционных параметров"
def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])
values_list = [False, 2.3, 8]
values_dict = {'a': 23, 'b': True, 'c': 'Str'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = ('SB', 25)
print_params(*values_list_2, 42)
