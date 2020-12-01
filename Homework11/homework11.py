from datetime import datetime

# Task1


class Person:

    def __init__(self, first_name, last_name, birthday, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = first_name + last_name
        self.birthday = birthday
        self.phone = phone
        self.email = email

    def add_teacher(self):
        pass

    def add_students(self):
        pass

class Student(Person):
    pass

class Teacher(Person):

    def __init__(self, salary):
        super().__init__(self, first_name, last_name, birthday, phone, email)
        self.salary = salary

    def add_salary(self):
        pass


# Task 2


class Mathematician():

    def square_nums(self, math_list: list):
        return [i ** 2 for i in math_list]

    def remove_positives(self, math_list: list):
        return [i for i in math_list if i < 0]

    def filter_leaps(self, math_list: list):
        return [i for i in math_list if i % 4 == 0]

m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))
print(m.remove_positives([26, -11, -8, 13, -90]))
print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))


# Task 3


class Product:

    def __init__(self, type_of_product, name, price):
        self.type = type_of_product
        self.name = name
        self.price = price

    def __repr__(self):
        return str(self.__dict__)


class ProductStore:

    def __init__(self):
        self.dict_of_products = dict()
        self.all_earnings = 0

    def __repr__(self):
        return str(self.dict_of_products)

    def add(self, product: Product, amount: int):
        self.dict_of_products.update(
            {product.name: {"type": product.type, "price": product.price, "amount": amount}}
        )
        return self.dict_of_products

    def set_discount(self, identifier: str, percent: int, identifier_type: str = "name"):
        if identifier_type == "name":
            try:
                self.dict_of_products[identifier]["discount"] = percent
            except KeyError:
                print("Product not found!")
        elif identifier_type == "type":
            count_of_found_products_by_type = 0
            for nested_key in self.dict_of_products.keys():
                if self.dict_of_products[nested_key]["type"] == identifier:
                    self.dict_of_products[nested_key]["discount"] = percent
                    count_of_found_products_by_type += 1
            if count_of_found_products_by_type == 0:
                print("Type of products not found!")
        return self.dict_of_products

    def sell_product(self, product_name, amount):
        try:
            the_balance_of_product = self.dict_of_products[product_name]["amount"]
            current_price = self.dict_of_products[product_name]["price"] * 1.3
            try:
                current_discount = self.dict_of_products[product_name]["discount"] / 100
            except KeyError:
                current_discount = 1
        except KeyError:
            print("Product not found!")
        else:

            if the_balance_of_product > amount:
                self.dict_of_products[product_name]["amount"] = the_balance_of_product - amount
                self.dict_of_products[product_name]["income"] = amount * current_price * current_discount
            else:
                print("insufficient amount")
        return self.dict_of_products

    def get_income(self):
        for nested_dict in self.dict_of_products.values():
            try:
                self.all_earnings = self.all_earnings + nested_dict.get("income")
            except Exception:
                pass
        return print(f"All earnings: {round(self.all_earnings, 2)}")

    def get_all_products(self):
        count_of_all_products = 0
        for nested_key in self.dict_of_products.keys():
            count_of_all_products = count_of_all_products + self.dict_of_products[nested_key]["amount"]
            print(f'{nested_key} - {self.dict_of_products[nested_key]["amount"]}')
        print("-" * 80, f"\nALL - {count_of_all_products}")

    def get_product_info(self, product_name):
        print((product_name, self.dict_of_products[product_name]["amount"]))


p = Product("Sport", "Football T-Shirt", 150)
p2 = Product("Food", "Ramen", 65)
p3 = Product("Sport", "Pants", 120)
p4 = Product("Food", "Burger", 90)
s = ProductStore()
s.add(p, 100)
s.add(p2, 300)
s.add(p3, 20)
s.add(p4, 176)
s.set_discount("Food", 80, "type")
s.sell_product("Football T-Shirt", 2)
s.sell_product("Burger", 45)
s.get_income()
s.get_all_products()
s.get_product_info("Burger")


# Task 4


class CustomException(Exception):

    def __init__(self, message: str = "Помилка!"):
        self.message = message
        super().__init__(self.message)
        self.current_time = datetime.today()
        with open("log.txt", "a") as self.file:
            self.file.write(f"{self.current_time} - {message}!\n")


    def __repr__(self):
        return str(self.current_time)


raise CustomException("Custom Exception")
