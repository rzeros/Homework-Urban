# Домашняя работа по уроку "Цикл for. Элементы списка. Полезные функции в цикле"
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
prime = []
not_prime = []
for i in range(len(numbers)):
    if numbers[i] == 1:
        continue
    is_prime = True  # Флаг
    for j in range(2, numbers[i]):
        if numbers[i] % j == 0:
            is_prime = False
            break
    if is_prime:
        prime.append(numbers[i])
    else:
        not_prime.append(numbers[i])
print("Primes:", prime)
print("Not Primes:", not_prime)
