import random

# Task 1. The greatest number

list_random = []  # Create blank list

i = 0

while i < 10:
    list_element = random.randint(1, 100)  # Generate random element for list
    list_random.append(list_element)  # Add random element to list
    i += 1

print(f"Максимальне значення зі списку {list_random} = {max(list_random)}\n")

# Task 2. Exclusive common numbers

list_1 = []  # Create blank list_1
list_2 = []  # Create blank list_2

i = 0

while i < 10:
    list_1.append(random.randint(1, 10))  # Add random element to list_1
    list_2.append(random.randint(1, 10))  # Add random element to list_2
    i += 1

list_3 = list(set(list_1) & set(list_2))  # Generate list_3

print(f"Список №1: {list_1}\nСписок №2 {list_2}\nСписок зі спільними елементами: {list_3}\n")

# Task 3. Extracting numbers

list_int = list(range(1, 101))  # Generate list that contains all int from 1 to 100
list_separate = []  # Create blank separated list

i = 0

while i < len(list_int):
    if list_int[i] % 7 == 0 and not list_int[i] % 5 == 0:  # divisible by 7 but not multiple of 5
        list_separate.append(list_int[i])
    i += 1

print(f"Список чисел, які кратні 7, але не кратні 5:\n{list_separate}")
