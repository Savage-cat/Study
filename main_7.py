# class Person:
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     #     сеттер для установки возраста
#     def set_age(self, age):
#         if 0 < age < 110:
#             self.__age = age
#         else:
#             print('Недопустимый возраст')
#
#     #     геттер для установки возраста
#     def get_age(self):
#         return self.__age
#
#
#     def print_person(self):
#         print(f'Имя {self.__name}\nВозраст {self.__age}')
#
# tom = Person('Tom', 40)
# # tom.__name = 'Nick'
# # tom.__age = -20
# tom.print_person()
#
# tom.set_age(-126)
# tom.set_age(23)
#
# tom.print_person()

# import random
#
#
# class MusicAlbum:
#
#     def __init__(self, title, artist, release_year, genre, tracklist):
#         self.title = title
#         self.artist = artist
#         self.release_year = release_year
#         self.genre = genre
#         self.tracklist = tracklist
#
#     def show_info(self):
#         print(f'Название: {self.title}\nисполнитель: {self.artist}\nГод: {self.release_year}\nжанр: {self.genre}\nТреки: {self.tracklist}')
#
#     def play_random_track(self):
#         random_index = random.choice(self.tracklist)
#         return print(f'Воспроизводится трек {self.tracklist.index(random_index)}: {random_index}')
#
# m1 = MusicAlbum('Deutschland', 'Rammstein', '2019', 'Neue Deutsche Harte', ['Deutschland', 'Radio', 'Zeig dich', 'Auslander', 'Sex', 'Puppe', 'Was ich liebe','Diamant',
#                                                                             'Weigt weg', 'Tattoo', 'Hallomann'])
# m1.show_info()
# m1.play_random_track()


# class Student:
#
#     def __init__(self, name, age, grade, score):
#         self.name = name
#         self.age = age
#         self. grade = grade
#         self.score = score
#
#     def show_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.age}\nКласс: {self.grade}')
#         print('Оценки:', *self.score, sep=' ')
#         # print(' '.join(map(str, self.score)))  если в списке цифры, есть такой метод
#
#
#     def average_score(self):
#         average_sum = sum(self.score) / len(self.score)
#         return print(f'Средний бал: {average_sum}')
#
#
# s1 = Student('Егор Данилов', '12', '5В', [5, 4, 4, 5])
#
# s1.show_info()
# s1.average_score()


class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f'Марка: {self.brand}\nМодель: {self.model}')


class Car(Vehicle):

    def __init__(self, brand, model, num_door):
        super().__init__(brand, model)
        self.num_door = num_door

    def display_info(self):
        super().display_info()
        print(f'Количество дверей: {self.num_door}')


class Motorcycle(Vehicle):

    def __init__(self, brand, model, engine_capasity):
        super().__init__(brand, model)
        self.engine_capasity = engine_capasity

    def display_info(self):
        super().display_info()
        print(f'Объём двигателя см3: {self.engine_capasity}')


c1 = Vehicle('Ferrari', 'F50')
c1.display_info()

c2 = Car('Lada', 'Granta', '5')
c2.display_info()

m1 = Motorcycle('BMW', 'Bandit', '1000')
m1.display_info()
