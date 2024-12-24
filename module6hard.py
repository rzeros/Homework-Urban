import math

class Figure:
    sides_count = 0
    def __init__(self, color: list, sides, filled=None):
        self.__sides = sides
        self.__color = color
        self.filled = filled

    def get_color(self):
        return self.__color

    def is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in [r, g, b])

    def set_color(self, r, g, b):
        if self.is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def is_valid_sides(self, *args):
        return all(len(args) == self.sides_count and isinstance(value, int) and 0 <= value for value in args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        if self.sides_count == 1:
            return self.get_sides()[0]
        else:
            return sum(self.get_sides())

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            self.__sides = list(new_sides)



class Circle(Figure):
    sides_count = 1

    def __init__(self, color, sides, filled=None):
        super().__init__(color, [sides], filled)
        self.__radius = self.get_sides()[0] / (2*math.pi)

    def get_square(self):
        return math.pi * self.__radius ** 2


class Triangle(Figure):

    sides_count = 3

    def __init__(self, color, sides, filled):
        super().__init__(color, sides, filled)

    def get_square(self):
        p = 0.5 * (sum(self.get_sides()))
        return math.sqrt(p * (p-self.get_sides()[0]) * (p-self.get_sides()[1]) * (p-self.get_sides()[2]))


class Cube(Figure):

    sides_count = 12

    def __init__(self, color, sides, filled=None):
        super().__init__(color, [sides] * self.sides_count, filled)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())


















