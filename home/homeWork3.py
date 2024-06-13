class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount

    def _kill(self):
        self._balance = 0

    def _jackpot(self):
        self._balance *= 10

    def _merge_balance(self, other_balance):
        self._balance += other_balance


client1 = Bank("John", 1000)
client2 = Bank("Alice", 500)

# Вызов методов Bank
client1.moneyX()
print(client1._balance)  # Проверка изменения баланса
client1._kill()  # Обнуление баланса
print(client1._balance)  # Проверка обнуления баланса
client2._jackpot()  # Выигрыш джекпота
print(client2._balance)  # Проверка выигрыша джекпота
client1._merge_balance(client2._balance)  # Объединение баланса
print(client1._balance)  # Проверка объединения баланса


# class Calculator:
#     def __init__(self, value):
#         self.value = value
#
#     def __add__(self, other):
#         return self.value + other.value
#
#     def __sub__(self, other):
#         return self.value - other.value
#
#     def __mul__(self, other):
#         return self.value * other.value
#
#     def __truediv__(self, other):
#         if other.value != 0:
#             return self.value / other.value
#         else:
#             return "Ошибка: деление на ноль"
#
#
# num1 = Calculator(10)
# num2 = Calculator(5)
#
# print(num1 + num2)
# print(num1 - num2)
# print(num1 * num2)
# print(num1 / num2)


