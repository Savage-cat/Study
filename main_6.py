# print(5 + 5)
# print('N' * 5)


#__add__ +
#__sub__ -
#__mul__ *
#__truediv__ /
#__floordiv__ //
#__mod__ %

#__lt__ <
#__gt__ >
#__le__ <=
#__ge__ >=
#__eq__ ==


# class Y:
#     def __init__(self, y):
#         self.y = y
#     # def __lt__(self, y_):
#     #     if self.y < y_.y:
#     #         return 'Объект 1 меньше объекта 2'
#     #     else:
#     #         return 'Объект 1 больше объекта 2'
#     # def __add__(self, y_):
#     #     return self.y + y_.y
#
#     def __eq__(self, y_):
#         if self.y == y_.y:
#             return 'Числа равны'
#         else:
#             return 'Числа не равны'

# obj1 = Y(3)
# obj2 = Y(5)
# print(obj1 == obj2)

# print(obj1 < obj2)
# obj3 = Y('Sam')
# obj4 = Y('Bob')

# print(obj1 + obj2)
# print(obj3 + obj4)

# num = 10
# num1 = 20
# print(num == num1)



# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, obj):
#         return self.x + obj.x, self.y + obj.y
#
#     def __sub__(self, obj):
#         return self.x - obj.x, self.y - obj.y
#
#     def __mul__(self, k):
#         k = 5
#         return self.x * k, self.y * k
#
#
# obj1 = Vector(2, 3)
# obj2 = Vector(4, 6)
# # k = 5
# obj3 = Vector.__mul__(obj1, obj2)
#
# print(obj1 + obj2)
# print(obj1 - obj2)
# print(obj3)

class Matrix:
    def __init__(self, a11, a12, a21, a22):
        self.a11 = a11
        self.a12 = a12
        self.a21 = a21
        self.a22 = a22

    def __add__(self, obj):
        return f'{self.a11 + obj.a11} {self.a12 + obj.a12}\n{self.a21 + obj.a21} {self.a22 + obj.a22}'

    def __sub__(self, obj):
        return f'{self.a11 - obj.a11} {self.a12 - obj.a12}\n{self.a21 - obj.a21} {self.a22 - obj.a22}'

    # def __mul__(self, k):
    #     return self.a11 * k, self.a12 * k, self.a21 * k, self.a22 * k

    def __mul__(self, obj):
        return (self.a11 * obj.a11 + self.a12 * obj.a21), (self.a11 * obj.a12 + self.a12 * obj.a22), (self.a21 * obj.a11 + self.a22 * obj.a21), (self.a21 * obj.a12 + self.a22 * obj.a22)


m1 = Matrix(2, 1, 3, 5)
m2 = Matrix(1, 6, 3, 1)

print(m1 + m2)
print(m1 - m2)
# print(m1 * 5)
print(m1 * m2)
