# 1 пример
numbers = [1, 2, 3]
print(type(numbers))


class Character():
    def __init__(self, actual_race, damage=10, armor=20): # self это ссылка на экземпляр
        self.race = actual_race # объявление переменной на уровне класса
        self.damage = damage
        self.armor = armor


unit = Character('Elf', 20, 40)
print(unit.race)
print(unit.armor)

# 2 пример (создание статических атрибутов)
class Character():
# на уровне класса объявляем статические атрибуты
    max_speed = 100
    dead_health = 0

    def __init__(self, actual_race, damage=10, armor=20):
        self.race = actual_race
        self.damage = damage
        self.armor = armor
        self.health = 100

    def hit(self, damage):
        self.health -= damage

    def is_dead(self):
        return self.health == Character.dead_health


unit = Character('Ork')
print(unit.race)
print(Character.max_speed)

unit.hit(20)
print(unit.health)
print(unit.is_dead())
unit.hit(80)
print(unit.is_dead())

unit.health = -200
print(unit.health)

# 3 пример (создание защищенных и приватных атрибутов и объявление свойства property,
# который дает доступ к чтению данных атрибутов. Свойство лучше объявлять,
# когда есть сложная логика)

class Character():
    MAX_SPEED = 100

    def __init__(self, actual_race, damage=10):
        self.__race = actual_race # приватный атрибут
        self.damage = damage

        self._health = 100

        self._current_speed = 20

    def hit(self, damage):
        self._health -= damage

    @property
    def health(self):
        return self._health

    @property
    def race(self):
        return self.__race

    @property
    def current_speed(self):
        return self._current_speed

# создание свойства с возможностью записи
    @current_speed.setter
    def current_speed(self, current_speed):
        if current_speed < 0:
            self._current_speed = 0
        elif current_speed > 100:
            self._current_speed =100
        else:
            self._current_speed = current_speed


print(Character.MAX_SPEED)
Character.MAX_SPEED = 10
print(Character.MAX_SPEED)
unit = Character('Elf')
unit._Character__race = 'Ork'
print(unit._Character__race)

unit._health = 0
print(unit._health)

print(unit.health)
print(unit.race)

# не возможно присвоить новое значение
# unit.health = 10
# print(unit.health)

unit.current_speed = 50
print(unit.current_speed)
unit.current_speed = 120
print(unit.current_speed)
unit.current_speed = -30
print(unit.current_speed)


# 4 пример (объявление статических методов)
class StaticTest:
    x = 1


t1 = StaticTest()
print(f'via instance:{t1.x}')
print(f'via class:{StaticTest.x}')
t1.x = 2 # создание нового атрибута внутри класса уровня экземпляра
print(f'via instance:{t1.x}')
print(f'via class:{StaticTest.x}') #
StaticTest.x = 3
print(f'via instance:{t1.x}')
print(f'via class:{StaticTest.x}')


# 5 пример
class Date:
    def __init__(self, month, day, year):
        self.month = month
        self.day = day
        self.year = year

    def display(self):
        return f'{self.month}-{self.day}-{self.year}'

# в классе возможно иметь только один конструктор
# статические методы используют в качестве конструкторов
    # два способа создания статических методов:

    @classmethod
    def millenium_c(cls, month, day): # cls это информация о классе
        return cls(month, day, 2000)

    @staticmethod
    def millenium_s(month, day):
        return Date(month, day, 2000)


d1 = Date.millenium_c(6, 9)
d2 = Date.millenium_s(6, 9)

print(d1.display())
print(d2.display())


class DateTime(Date):
    def display(self): # переопределение метода
        return f'{self.month}-{self.day}-{self.year} - 00:00:00PM'


dt1 = DateTime(10, 10, 1990)
dt2 = DateTime.millenium_c(10, 10)

print(isinstance(dt1, DateTime))
print(isinstance(dt2, DateTime))

print(dt1.display())
print(dt2.display())


# 6 пример
class StrConverter:
    @staticmethod
    def to_str(bytes_or_str):
        if isinstance(bytes_or_str, bytes):
            value = bytes_or_str.decode('utf-8')
        else:
            value = bytes_or_str
        return value

    @staticmethod
    def to_bytes(bytes_or_str):
        if isinstance(bytes_or_str, str):
            value = bytes_or_str.encode('utf-8')
        else:
            value = bytes_or_str
        return value


print(StrConverter.to_str('\c234'))
print(StrConverter.to_str('A'))

print(StrConverter.to_bytes('\c234'))
print(StrConverter.to_bytes('A'))













