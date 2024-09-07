# Домашняя работа по уроку "Специальные методы классов"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название {self.name}, кол-во этажей: {self.number_of_floors}'

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print('Такого этажа не существует')


house_elb = House('Эльбрус', 25)
house_blz = House('Бальза', 19)

print(str(house_elb))
print(str(house_blz))
print(len(house_elb))
print(len(house_blz))
