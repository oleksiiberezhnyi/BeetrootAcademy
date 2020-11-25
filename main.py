class Car():

    total_number_of_cars = 0

    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.total_driven_km = 0
        Car.total_number_of_cars += 1

    def repaint(self, color):
        self.color = color

    def drive(self, km_driven):
        self.total_driven_km += km_driven

# my_car = Car("Volvo", "V40", "2019", "white")
# print(my_car.color)
# my_car.repaint("green")
# print(my_car.color)
# print(my_car.total_driven_km)
# my_car.drive(1000)
# print(my_car.total_driven_km)

car1 = Car("Volvo", "V40", 2019, "white")
print(Car.total_number_of_cars)
car2 = Car("Kia", "Picanto", 2018, "lime")
print(Car.total_number_of_cars)

# print(type(car1))
# print(type(car2))

# print("car1 is of brand " + car1.brand)
# print("car2 is of brand " + car2.brand)

