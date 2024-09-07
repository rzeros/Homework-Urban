# Домашняя работа по уроку "Атрибуты и методы объекта"

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        new_floor = new_floor
        if 1 <= new_floor <= self.number_of_floors:
            print(new_floor)
        else:
            print('Такого этажа не существует')


house_elb = House('Эльбрус', 25)
house_blz = House('Бальза', 19)

house_blz.go_to(20)
house_elb.go_to(-2)
house_elb.go_to(24)
