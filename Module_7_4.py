# Домашнее задание по теме "Форматирование строк".

team1_num = 25
team2_num = 27
score_1 = 13
score_2 = 14
team1_time = 10521
team2_time = 10603
if score_1 > score_2:
    challenge_result = "победа команды Мастера кода!"
elif score_1 == score_2:
    challenge_result = "ничья!"
else:
    challenge_result = "победа команды Волшебники Данных!"
tasks_total = score_1 + score_2
time_avg = round((team1_time + team2_time) / (score_1 + score_2),1)

# Использование %:
print("В команде Мастера кода участников: %s!" % team1_num)
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))
print("Итого сегодня в командах участников: %s и %s!" % (team1_num, team2_num))

# Использование format():
print("Команда Волшебники данных решила задач: {}!".format(score_2))
print("Волшебники данных решили задачи за {} с!".format(team2_time))

# Использование f-строк:
print(f"Команды решили {score_1} и {score_2} задач.")
print(f"Результат битвы: {challenge_result}")
print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")


