# Task 1

text_string = input("Введіть текст: ")

split_string = text_string.split()

word_list = dict()

for words in split_string:
    if word_list.get(words) == None:
        word_list[words] = 1
    else:
        word_list[words] += 1

print(word_list)

# Task 2

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

def total_price(stock: dict, prices: dict):
    total = 0
    for position in stock:
        if position in stock and position in prices:
            total = total + stock.get(position) * prices.get(position)
    return(total)

print(f"Загальна вартість товару: {total_price(stock, prices)} у.о.")

# Task 3

squared = [(i, i ** 2) for i in range(11)]

print(squared)
