from models import *

# методы для создания записей
# Employee.create(id=1, name='Nick', age=24, salary=10000)
# Employee.create(id=2, name='Jack', age=34, salary=15000)

# методы для чтения

# employee = Employee.select()
# for user in employee:
#     print(user.name, user.age, user.salary)

# employee = Employee.get(Employee.id == 1)  # возвращает только одну запись
# print(employee.name, employee.age, employee.salary)

# методы для обновления записей

# employee = Employee.get(Employee.id == 2)
# employee.name = 'Tom'
# employee.save()

# Employee.update(age=30).where(Employee.id == 2).execute()

# методы для удаления записей

# user = Employee.get(Employee.id == 1)
# user.delete_instance()

# Employee.delete().where(Employee.id == 2).execute()

# фильтрация
# employee = Employee.select().where(Employee.name == 'Nick')
# for user in employee:
#     print(user.name, user.age, user.salary)


# and
# employee = Employee.select().where((Employee.name == 'Nick') & (Employee.age == 24))
# for user in employee:
#     print(user.name, user.age, user.salary)


# or
# employee = Employee.select().where((Employee.name == 'Nick') | (Employee.age == 24))
# for user in employee:
#     print(user.name, user.age, user.salary)

# like
# employee = Employee.select().where(Employee.name ** 'N%')
# for user in employee:
#     print(user.name, user.age, user.salary)

# employee = Employee.select().where(Employee.age << [24, 34])
# for user in employee:
#     print(user.name, user.age, user.salary)

# between

# employee = Employee.select().where(Employee.age.between(20, 34))
# for user in employee:
#     print(user.name, user.age, user.salary)


Product.create(id=1, name='Шоколад Alpengold', price=100, stock=6)
Product.create(id=2, name='Coca-Cola', price=200, stock=10)
Product.create(id=3, name='Snickers', price=90, stock=14)

product = Product.select().where(Product.price > 50)
for item in product:
    print(item.name, item.price, item.stock)

product = Product.select().where(Product.stock > 10)
for item in product:
    print(item.name, item.price, item.stock)


Product.update(price=150).where(Product.id == 1).execute()
Product.update(price=250).where(Product.id == 2).execute()
Product.update(price=100).where(Product.id == 3).execute()

Product.delete().where(Product.stock == 0).execute()


product = Product.select().where(Product.price.between(100, 150))
for item in product:
    print(item.name, item.price, item.stock)


product = Product.select().where(Product.name ** 'C%')
for item in product:
    print(item.name, item.price, item.stock)

