# while условие:
#     инструкции
#
#
# while условие:
#     инструкции
# else:
#     print('Цикл завершен успешно')
#
#
# number = 1
#
# while number < 5:
#     print(number)
#     number += 1
# else:
#     print(f'Итоговое число {number}, цикл завершен')

# i = 1
# while i <= 10:
#     print(i**2)
#     i += 1


# a = int(input('число: '))
# while a != 0:
#     if a < 0:
#         print('Встретилось отриц число')
#         break
#     a = int(input('число: '))
# else:
#     print('Ни одного отриц числа не было')


# a = int(input('угадайте число от 1 до 10: '))
# while a != 6:
#     if (0 < a <= 5) or (6 < a <= 10):
#         print('попробуйте ещё раз')
#
#     a = int(input('число: '))
# else:
#     print('Вы победили!')


# a = int(input('Введите число: '))
# i = 0
# while a != 0:
#     i += a
#     a = int(input('Введите число: '))
# else:
#     print(f'Сумма введенных чисел {i}')



# a = int(input('Введите положительное число: '))
# i = 0
# while i != a:
#     if i % 2 == 0:
#         print(i)
#     i += 1
#     if i == a:
#         if i % 2 == 0:
#             print(i)



# n = int(input('Введите число: '))
# count = 0
# while n >= 0:
#     count += 1
#     n = int(input('Введите число: '))
# else:
#     print('Введено отриц число')
#     print(count)

# sum = 0
#
# for i in range (101):
#     sum += i
#     print(sum)

# sum = 0
#
# for i in range (1, 6):
#     print(i**2)

# a = 'привет'
# b = 'аеёиоуыэюя'
# count = 0
# for letter in a:
#     if letter in b:
#         count += 1
# print(count)

# sum = 7
# for i in range (1, 11):
#     print(7*i)


# sqr = 0
# for i in range(1, 51):
#     sqr += i**2
# print(sqr)


n = str(input('Введите число: '))
number = 0
for i in n:
    number += int(i)
print(number)
