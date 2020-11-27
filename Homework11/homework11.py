# Task1

# class Person():
#
#     def __init__(self, first_name, last_name, birthday, phone, email):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.full_name = first_name + last_name
#         self.birthday = birthday
#         self.phone = phone
#         self.email = email
#
#     def add_teacher(self):
#         pass
#
#     def add_students(self):
#         pass
#
# class Student(Person):
#     pass
#
# class Teacher(Person):
#
#     def __init__(self, salary):
#         self.salary = salary
#
#     def add_salary(self):
#         pass
#
# # Task 2
#
# class Mathematician():
#
#     def square_nums(self, math_list: list):
#         return [i ** 2 for i in math_list]
#
#     def remove_positives(self, math_list: list):
#         return [i for i in math_list if i < 0]
#
#     def filter_leaps(self, math_list: list):
#         return [i for i in math_list if i % 4 == 0]
#
# m = Mathematician()
#
# print(m.square_nums([7, 11, 5, 4]))
# print(m.remove_positives([26, -11, -8, 13, -90]))
# print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))

# Task 3

class Product:

    def __init__(self, type_of_product, name, price):
        self.type = type_of_product
        self.name = name
        self.price = price

class ProductStore(Product):

    # def __init__(self, type_of_product, name, price, dict_of_product):
    #     self.dict_of_products = dict_of_product
        # {"type": self.type, "name": self.name, "price": self.price}

    list_of_products = []

    def add(self, product: dict):
        super().__init__(type_of_product, name, price)
        return product

#
#     def set_discount(self, identifier, percent, identifier_type = "name"):
#         pass
#
#     def sell_product(self, product_name, amount):
#         pass
#
#     def get_income(self):
#         pass
#
#     def get_all_products(self):
#         pass
#
#     def get_product_info(self, product_name):
#         pass
p = Product("Sport", "Football T-Shirt", 100)
p2 = Product("Food", "Ramen", 1.5)
print(p, p2)
s = ProductStore()
s.add(p)
print(s)