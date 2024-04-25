# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
#
#     def deposit(self, money):
#         self.__balance += money
#
#     def withdraw(self, money):
#         if self.__balance >= money:
#             self.__balance -= money
#         else:
#             print('Недостаточно средств')
#
#     def get_balance(self):
#         print('Баланс:', self.__balance)
#
#
# account = BankAccount()
#
# account.deposit(200)
# account.get_balance()
# account.withdraw(300)
# account.get_balance()


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def make_sound(self):
#         pass
#
#     def display_info(self):
#         print(f'Имя: {self.name}')
#
# class Dog(Animal):
#
#     def __init__(self, name, breed):
#         super().__init__(name)
#         self.breed = breed
#
#     def display_info(self):
#         super().display_info()
#         print(f'Порода: {self.breed}')
#
#     def make_sound(self):
#         print('Истошный лай:', 'Woof!')
#
#
# d1 = Dog('Bim', 'Корги')
#
# d1.display_info()
# d1.make_sound()





