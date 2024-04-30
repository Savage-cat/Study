# Задача 1

# arr = input().split()
# new_arr = []
# for el in arr:
#     new_arr.append(int(el))
# new_arr.sort()
# print(new_arr[1])


# Задача 62

# numbers = input().split()
# numbers = list(map(int, numbers))
# unique_numbers = []
# for el in numbers:
#     if el not in unique_numbers:
#         unique_numbers.append(el)
#
# print(len(unique_numbers))


# numbers = input().split()
# numbers = list(map(int, numbers))
# unique_numbers = set(numbers)
#
# print(len(unique_numbers))


# print(len(set(map(int, input().split()))))

# Задача 81

# a = int(input())
# b = int(input())
# c = int(input())
#
# if a < b + c and b < a + c and c < a + b:
#     print('YES')
# else:
#     print('NO')

# Задача 352

s = input()
j = input()

count = 0

for el in j:
    if el in s:
        count += 1
print(count)
