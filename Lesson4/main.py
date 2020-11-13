import random

r = random.rand(1, 10, 1)

while True:
    if input("Введіть число: ") == r:
        print("Ура!")
        break
    else:
        print("Спробуйте ще раз")
        continue

