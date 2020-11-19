# Task 1

movie_title = input("Який ваш найулюбленіший фільм? ")

def favorite_movie(name: str):
    print(f"Ваш улюблений фільм – {name}")

favorite_movie(movie_title)

# Task 2

def make_country(name="", capital=""):
    print("Створіть свою країну!")
    countries = dict()
    i = 1
    while True:
        name = input("Введіть назву країни: ")
        if len(name) != 0:
            capital = input("Назвіть столицю цієї країни: ")
            countries.update({f"Country №{i}": {"Name": name, "Capital": capital}})
            i += 1
        else:
            print(f"All created countries:\n{countries}")
            return False

make_country()

# Task 3

def make_operation(operand, *args):
    try:
        i = 0
        res_text = ""
        while i < len(args):
            if i < len(args) - 1 and str(abs(i)).isnumeric():
                res_text = res_text + str(args[i]) + operand
            elif i == len(args) - 1 and str(abs(i)).isnumeric():
                res_text = res_text + str(args[i])
            i += 1
        print(eval(res_text))
    except:
        print("Не правильно введені дані!")

make_operation("-", 5, 5, -10, -20)