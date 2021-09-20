class Bank:

    def deposit(self, value, years, perc):
        for y in range(years):
            new_value = perc * value / 100
            value += new_value

        return value


class Client(Bank):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'Current value {self.value}'

    def set_deposit(self, valueToBank, years, perc):
        self.value -= valueToBank
        self.result = self.deposit(valueToBank, years, perc)

    def get_back(self):
        self.value += self.result

mike = Client(5000)
sue = Client(4000)
print(mike)
mike.set_deposit(3000, 3, 5)
print(mike)
print(mike.result)
mike.get_back()
print(mike)










