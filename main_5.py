# def hello():
#     print('hello world')
#
# hello()


# def hello(name):
#     print(f'Hello, {name} {surname}')
#
# hello('Alex', 'Walker')


# def sum(a, b):
#     return a+b
# result = sum(10, 56)
# print(result)


# def hello(a):
#
#     k = 0
#     for i in range(2, a // 2 + 1):
#         if a % i == 0:
#             k = k + 1
#     if k <= 0:
#         print("Число простое")
#     else:
#         print("Число не является простым")
#
#
# a = int(input("Введите число: "))
#
# hello(a)
#
# l_t = [1, 1, 1, 2, 5, 7, 7, 8]
#
# def newlist(l_t):
#     unique_list = list(set(l_t))
#     print (unique_list)
#
# newlist(l_t)


# sum = lambda a, b: a + b
# print(sum(4, 5))
#
#
# sum = lambda x: [i*2 for i in x]
# print(sum([1, 2, 3, 4]))
#
# str = 'wwfwwfwf'
# sum = lambda str: str.upper()
# print(sum(str))
#
#
# sum = lambda x: x % 2 == 0
# print(sum(5))



# str = int(input('Сколько Вам лет: '))
# if str < 18:
#     print('Вы не совершеннолетний')
#
# elif 18 <= str < 65:
#     print('Вы взрослый')
#
# else:
#     print('Вы пенсионер')
#
#
#
# a = int(input('Введите число: '))
# c = 0
# while a >= 0:
#     c += a
#     a = int(input('Введите число: '))
#     if a < 0:
#         break
# print(f'вы ввели отрицательное число. Ваш результат: {c}')
#
#
#
# str = input('Введите слово: ')
# rev_str = str[::-1]
# print('-'.join(rev_str))
#
#
#
# text = input('Введите слова: ')
# l_text = text.lower().split(' ')
#
# empty_list = []
# for i in l_text:
#     if i not in empty_list:
#         empty_list.append(i)
#
# print(sorted(empty_list))
#
#
# str1 = input('Введите слово: ')
# str2 = input('Введите букву: ')
#
# def f_n(str1, str2):
#     lst1 = str1.split(' ')
#     lst2 = str2.split(' ')
#     lst3 = []
#     for i in lst1:
#         if i.lower()[0] in lst2:
#             lst3.append(i)
#     print(lst3)
#
# f_n(str1, str2)

# class Person():
#     def __init__(self, name, surname, age, weight, height):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.weight = weight
#         self.height = height
#
#     def info(self):
#         print(f'Привет, {self.name}')
#
#
# ivan = Person('Ivan', 'Vasiliev', 25, 75, 170)
#
#
# # print(ivan.name)
# ivan.info()


# class Square():
#     def __init__(self, side):
#         self.side = side
#
#     def calculate_square(self):
#         print(self.side**2)
#
# square1 = Square(5)
# square1.calculate_square()

# class Rectangle():
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def input_data(self):
#         self.length = int(input('Сторона а'))
#         self.width = int(input('Сторона b'))
#
#     def perimeter(self):
#         return 2*(self.width + self.length)
#
#     def area(self):
#         return self.width * self.length
#
# # rect = Rectangle(5, 4)
# print(rect.perimeter())
# rect = Rectangle('', '')
#
# rect.input_data()
#
# print(rect.area())


# class Person():
#     def __init__(self, name, surname, date_of_birth, phone_number, city, country, adress):
#         self.name = name
#         self.surname = surname
#         self.date_of_birth = date_of_birth
#         self.phone_number = phone_number
#         self.city = city
#         self.country = country
#         self.adress = adress
#
#     def input_data(self):
#         self.name = input('Введите имя')
#         self.surname = input('Введите фамилию')
#         self.date_of_birth = input('Введите дату рождения')
#         self.phone_number = input('Введите номер телефона')
#         self.city = input('Введите город проживания')
#         self.country = input('Введите страну проживания')
#         self.adress = input('Введите адрес проживания')
#
#
#     def info(self):
#         print(f'{self.name}, {self.surname}, {self.date_of_birth}, {self.phone_number},'
#               f' {self.city}, {self.country}, {self.adress}')
#
#     def name_surname(self):
#         print(f'{self.name}, {self.surname}')
#
#     def country_city(self):
#         print(f'{self.country}, {self.city}')
#
# ivan = Person('Ivan', 'Vasiliev', '05.01.1986', '+79996385766', 'Ekaterinburg', 'Russia', 'Frunse, 57')
#
#
# # print(ivan.name)
# # ivan.info()
# ivan.name_surname()
# ivan.country_city()



# class City():
#     def __init__(self, city_name, region, country, population, zipcode, phone_code):
#         self.city_name = city_name
#         self.region = region
#         self.country = country
#         self.population = population
#         self.zipcode = zipcode
#         self.phone_code = phone_code
#
#     def input_data(self):
#         self.city_name = input('Введите наименование города: ')
#         self.region = input('Введите регион: ')
#         self.country = input('Введите страну: ')
#         self.population = input('Население города: ')
#         self.zipcode = input('Почтовый код города: ')
#         self.phone_code = input('Телефонный код города: ')
#
#     def info(self):
#         print(f'{self.city_name}, {self.region}, {self.country}, {self.population},'
#               f' {self.zipcode}, {self.phone_code}')
#
#     def country_and_city(self):
#         return f'{self.country}, {self.city_name}'
#
#     def population_of_city(self):
#         return f'{self.population}'
#
#     def zipcode_and_phone_code(self):
#         return f'{self.zipcode}, {self.phone_code}'
#
#
# city1 = City('', '', '', '', '', '')
#
# city1.input_data()
# city1.info()
# city1.country_and_city()

# class Country():
#     def __init__(self, country_name, continent, population, phone_code, name_of_capital, cities_name):
#         self.country_name = country_name
#         self.continent = continent
#         self.population = population
#         self.phone_code = phone_code
#         self.name_of_capital = name_of_capital
#         self.cities_name = cities_name
#
#     def input_data(self):
#         self.country_name = input('Введите наименование страны: ')
#         self.continent = input('Введите континент: ')
#         self.population = input('Население страны: ')
#         self.phone_code = input('Телефонный код страны: ')
#         self.name_of_capital = input('Название столицы: ')
#         self.cities_name = input('Названия городов: ')
#
#     def info(self):
#         print(f'{self.country_name}, {self.continent}, {self.population}, {self.phone_code},'
#               f' {self.name_of_capital}, {self.cities_name}')
#
#     def country_and_capital(self):
#         print(f'{self.country_name}, {self.name_of_capital}')
#
#     def population_of_country(self):
#         print(f'{self.population}')
#
#     def name_of_cities(self):
#         print(f'{self.cities_name}')
#
#
# country1 = Country('', '', '', '', '', '')
#
# country1.input_data()
# country1.info()
# country1.country_and_capital()

# class Fraction():
#     def __init__(self, number, divider):
#         self.number = number
#         self.divider = divider
#
#     def input_data(self):
#         self.number = float(input('Введите числитель: '))
#         self.divider = float(input('Введите знаменатель: '))
#
#     def info(self):
#         print(f'Числитель: {self.number}, знаменатель: {self.divider}')
#
#     def multi(self, fraction1, fraction2):
#         return (fraction1.number + fraction2.number, fraction1.divider + fraction2.divider)
#
#     # def residual(self):
#     #     print(f'{self.population}')
#
#     # def name_of_cities(self):
#     #     return self.number + self.divider
#
#
# fraction1 = Fraction('', '')
# fraction2 = Fraction('', '')
#
#
# fraction1.input_data()
# fraction2.input_data()
#
# Fraction.multi()


# country1.input_data()
# print(country1.info())
# print(country1.country_and_capital())


# class MyClass():
#     @staticmethod
#     def static_method():
#         print('Hello')
#
# MyClass.static_method()


# class Calculator():
#     @staticmethod
#     def square(n):
#         return n*n
#
#
# print(Calculator.square(5))

# class Person():
#     j = 0
#
#     def __init__(self, name, surname, date_of_birth, phone_number, city, country, adress):
#         self.name = name
#         self.surname = surname
#         self.date_of_birth = date_of_birth
#         self.phone_number = phone_number
#         self.city = city
#         self.country = country
#         self.adress = adress
#         Person.j += 1
#
#     @staticmethod
#     def count_obj():
#         return Person.j
#
#     def input_data(self):
#         self.name = input('Введите имя')
#         self.surname = input('Введите фамилию')
#         self.date_of_birth = input('Введите дату рождения')
#         self.phone_number = input('Введите номер телефона')
#         self.city = input('Введите город проживания')
#         self.country = input('Введите страну проживания')
#         self.adress = input('Введите адрес проживания')
#
#
#     def info(self):
#         print(f'{self.name}, {self.surname}, {self.date_of_birth}, {self.phone_number},'
#               f' {self.city}, {self.country}, {self.adress}')
#
#     def name_surname(self):
#         print(f'{self.name}, {self.surname}')
#
#     def country_city(self):
#         print(f'{self.country}, {self.city}')
#
#
#
# ivan = Person('Ivan', 'Vasiliev', '05.01.1986', '+79996385766', 'Ekaterinburg', 'Russia', 'Frunse, 57')
# p2 = Person('Tania', 'Vasiliev', '05.01.1986', '+79996385766', 'Ekaterinburg', 'Russia', 'Frunse, 57')
# p3 = Person('Andrey', 'Vasiliev', '05.01.1986', '+79996385766', 'Ekaterinburg', 'Russia', 'Frunse, 57')
#
# print(Person.count_obj())


# class Calculator():
#
#     count = 0
#
#     # def __init__(self):
#     #     Calculator.count += 1
#
#     @staticmethod
#     def count_obj():
#         return Calculator.count
#
#     @staticmethod
#     def triangle(a, b):
#         Calculator.count += 1
#         return a * b * 0.5
#
#     @staticmethod
#     def triangle2(a, b, c):
#         Calculator.count += 1
#         p = (a + b + c) / 2
#         return (p - a) * (p - b)
#
#     @staticmethod
#     def square(n):
#         Calculator.count += 1
#         return n * n
#
#     @staticmethod
#     def rectangle(a, b):
#         Calculator.count += 1
#         return a * b
#
#     @staticmethod
#     def rombus(a, h):
#         Calculator.count += 1
#         return a * h
#
#
# c1 = Calculator.triangle(5, 6)
# c2 = Calculator.triangle2(5, 6, 7)
# c3 = Calculator.square(5)
# c4 = Calculator.rectangle(4, 7)
# c5 = Calculator.rombus(4, 7)
#
# print(c1)
# print(c2)
# print(c3)
# print(c4)
# print(c5)
# print(Calculator.count_obj())


# class Arguments():
#
#     @staticmethod
#         def max_arg(a, b, c, d):
#
#             return a * h


# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         pass
#
# class Dog(Animal):
#     def speak(self):
#         return 'Woof!'
#
# class Cat(Animal):
#     def speak(self):
#         return 'Meow!'
#
# dog = Dog('Buddy')
# cat = Cat('Whiskas')
#
# print(dog.name)
# print(cat.speak())


# class Parent:
#     def __init__(self, name):
#         self.name = name
#
#     def show_info(self):
#         print(f'name: {self.name}')
#
#
# class Child(Parent):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def show_info(self):
#         super().show_info()
#         # print('--------------')
#         print(f'Age: {self.age}')
#
#
# parent_obj = Parent('Alice')
# child_obj = Child('Bob', 10)
#
# parent_obj.show_info()
# print('--------------')
# child_obj.show_info()
#
# print(isinstance(child_obj, Parent))  #проверка является ли объект экземпляром класса
# print(issubclass(Child, Parent))

class Human():

    def __init__(self, name, surname, date_of_birth, gender):
        self.name = name
        self.surname = surname
        self.date_of_birth = date_of_birth
        self.gender = gender

    def show_info(self):
        print(f'name: {self.name}, surname: {self.surname}, date_of_birth: {self.date_of_birth}, gender: {self.gender}')


class Builder(Human):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def show_info(self):
#         super().show_info()
#         # print('--------------')
#         print(f'Age: {self.age}')