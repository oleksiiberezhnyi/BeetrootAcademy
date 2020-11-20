# Task 1

def oops():
    raise KeyError("Помилка!")


def calls_oops(dictionary):
    try:
        print(dictionary["name"])
        oops()
    except:
        print("Помилка!")


sample_dict = dict(
    Name="Oleksii",
    Last_Name="Berezhnyi"
)

calls_oops(sample_dict)


# Task 2

def two_numbers():
    try:
        a = int(input("a = "))
        b = int(input("b = "))
        return a ** 2 / b
    except (TypeError, ValueError):
        print("Це не числа!")
    except ZeroDivisionError:
        print("Ділення на нуль!")


print(two_numbers())
