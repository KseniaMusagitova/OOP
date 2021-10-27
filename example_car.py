# используем функцию property (1 метод)
class Car:
    def __init__(self, color, type, year):
        self.__color = color
        self.__type = type
        self.__year = year


    def starting(self):
        return 'Автомобиль заведен'

    def turning_off(self):
        return 'Автомобиль заглушен'

    def __getYear_of_issue(self):
        return self.__year

    def __setYear_of_issue(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            raise TypeError('Неправильный тип данных')

    def __delYear_of_issue(self):
        print(f"Атрибут {self.__year} удаляется")
        del self.__year

    def type_of(self):
        return self.__type

    def car_color(self):
        return self.__color

    # используем функцию property (1 метод)
    Year = property(__getYear_of_issue, __setYear_of_issue, __delYear_of_issue)


s = Car('black', 'mazda', 2020)
print(s.starting())
print(s.turning_off())

s.Year = 2018
print(s.Year)
del s.Year

print(s.type_of())
print(s.car_color())

# используем декоратор (2 метод)
class Car:
    def __init__(self, color, type, year):
        self.__color = color
        self.__type = type
        self.__year = year

    def starting(self):
        return 'Автомобиль заведен'

    def turning_off(self):
        return 'Автомобиль заглушен'

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if isinstance(year, int):
            self.__year = year
        else:
            raise TypeError('Неправильный тип данных')

    @year.deleter
    def year(self):
        print(f"Атрибут {self.__year} удаляется")
        del self.__year

    def type_of(self):
        return self.__type

    def car_color(self):
        return self.__color


s = Car('black', 'mazda', 2020)
print(s.starting())
print(s.turning_off())

s.year = 2018
print(s.year)
del s.year

print(s.type_of())
print(s.car_color())

