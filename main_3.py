# a = 'Hello'
# b = 'World'

# print(len(a))
# print(a[4])
# print(a[-2])
# print(a[0:3])
# print(a[1:])
# print(a[0:5:2])
# print(a[::-1])

# value = 'Hexlet'

# b = value.replace('H', 'g')
# value[::]
# value[:]
# value[::2]
# value[1::2]
# value[::-1]
# value[5:]
# value[:5]
# print(a[-2:1:-1])


# a = input('Слово: ')
# if a == a[::-1]:
#     print(True)
# else:
#     print(False)

# a = input('Введите что-нибудь: ')
# gl = 'аеёиуоэюя'
# count = 0
# for letter in a:
#     if letter in gl:
#         count += 1
# c = len(a) - count
# print(f'Согласных {c}, гласных {count}')




# a = input('Введите что-нибудь: ')
# b = str(input('Какой элемент меняем: '))
# d = input('На что заменить: ')
# c = a.replace(b, d)
# print(c)


# a = input('Введите что-нибудь: ')
# b = a.replace(' ', '')
# print(b)

# list = [5, 7, 9, 10, True, False]
# string = 'hello'

# my_string = 'hello'
# my_list = list(my_string)
# print(my_list)

# a = []
# a.append(67)
# print(a)

# a = [65, 78, 45, 32, 65, 65]
# b = [5,4,3]
# print(len(b))
# print(max(b))
# print(min(b))
# print(sum(b))
# print(a==b)
# a.append(67)
# a.extend(b)
# print(a)
# a.insert(0, 78)    #вставка элемента по индексу
# a.remove(65)
# a.index(78)
# b = a.pop(1)
# a.count(65)
# a.reverse()
# print(sorted(a)) # от меньшего к большему


# list = [1,2,3,4,5,6,7,8,9,10]
# for i in list:
#     if i%2 == 0:
#         print(i)
#
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# b = [52, 17, 60]
# a.extend(b)
# print(a)


#===== Кортеж=====

# a = (12, 34, 56543, 'dfjfdj', True, [45, 5])

# a[0] = 34

# a = ()

# b = ('hello',)

# c = 'hello'

# d = tuple(c)

# print(d)  превратили строку в кортеж

# c = (54, [43,67, 93, 75])
# c = [1][0] = 67
# print(c)

# for el in c:
#     print(el)
#
# if 54 in c:
#     print(True)
#
# print(len(c))
# print(sum(c))
# print(min(c))
# print(max(c))
#
# print(c[0:3])
#
# list1 = list(c)
# print(list1)


# =====dictionary=====

# dictionary = {ключ1: значение1, ключ2: значение2}
# users = {1: 'Tom', 2: 'Jack', 3: 'Nick'}

# a = {}
# b = [
#     ['8348348', 'Tom'],
#     ['8348344', 'Jack']
#     ['58843', 'Nick']
# ]
# users = dict(b)
# # print(users['8348348'])
# users['03039'] = 'Sam'
# print(users)
#
# del users['8348348']
# print(users)
#
# users.clear()


# a = {1111: 'Tom', 2222: 'Sam'}
#
# b = {3333: 'Jack', 4444: 'Joe'}
#
# a.update(b)
# print(a)
#
# for key in a:
#     print(f'Phone: {key} User:{a[key]}')
#
# for key, value in a.items():
#     print(f'Phone: {key} User:{value}')



#=====Множества=====

# Хранит только уникальные значения

# a = {'Tom', 'Jack', 'Tom'}
# print(a)
#
# chisla = [5, 454, 32, 232]
# chisla2 = set(chisla)
# print(chisla2)
# print(len(chisla2))


# a = {'Tom', 'Jack', 'Tom'}
# a.add = {'Daniel'}
#
# a.remove('Tom')
# a.clear()
#
# for el in a:
#     print(el)
#
# users = {'Tom', 'Jack', 'Kate'}
# users2 = {'Nick', 'Bob', 'Alice'}

# users3 = users.union(users2)
# print(users3)
# print(users | users2)

# users3 = users.intersection(users2)
# print(users3)
# print(users & users2)

# users3 = users2.difference(users)
# print(users3)

# users4 = users.difference

# c = a.symmetric_difference(b)
# c = a ^ b

# users = {'Tom', 'Bob', 'Alice'}
# users2 = {'Sam', 'Tom', 'Bob', 'Alice', 'Joe'}
# print(users.issubset(users2))
# print(users2.issubset(users))   подмножество

# print(users2.issuperset(users)) надмножество


# c = frozenset({5, 56, 454, 23})
# print(len(c))
# if 5 in c:
# if 5 not in c: