from peewee import *

# db = SqliteDatabase('base.db')

# class Employee(Model):
#     name = CharField()
#     age = IntegerField()
#     salary = IntegerField()
#
#     class Meta:
#         database = db
#
#
# if __name__ == '__main__':
#     db.create_tables([Employee])

####################################################

# db = SqliteDatabase('Product.db')
#
# class Product(Model):
#     name = CharField()
#     price = IntegerField()
#     stock = IntegerField()
#
#     class Meta:
#         database = db
#
#
# if __name__ == '__main__':
#     db.create_tables([Product])

db = PostgresqlDatabase()
