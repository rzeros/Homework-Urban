# Дополнительное практическое задание по модулю: "Подробнее о функциях"
def calculate_structure_sum(info):
    sum_ = 0
    if isinstance(info, int):
        sum_ += info
    elif isinstance(info, str):
        sum_ += len(info)
    elif isinstance(info, (list, tuple, set)):
        for i in info:
            sum_ += calculate_structure_sum(i)
    elif isinstance(info, dict):
        for key, value in info.items():
            sum_ += calculate_structure_sum(key) + calculate_structure_sum(value)
    return sum_


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)




