# Berezhnyi Oleksii

# Task 1


def logger(func):
    def wraper(*args):
        print(f"{func.__name__} called with "
              f"{', '.join(str(arg) for arg in args)}")

    return wraper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


add(2, 3)
square_all(4, 5, 6, 7)


# Task 2


def stop_words(words: list):
    def wrap(func):
        def string_edited(*args: str):
            list_of_words = func("".join(args))[:-1].split()
            for i in list_of_words:
                for j in words:
                    if i == j:
                        list_of_words[list_of_words.index(j)] = "*"
                        censored_text = " ".join(list_of_words)
            return censored_text

        return string_edited

    return wrap


@stop_words(["pepsi", "BMW"])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("Oleksii"))


# Task 3


def arg_rules(type_: type, max_lenght: int, contains: list):
    def wrap(func):
        def check_string(*args: str):
            errors = []
            if type("".join(args)) != type_:
                errors.append(
                    f"\n— Your data does not match the specified type {type_}"
                )
            if len("".join(args)) > max_lenght:
                errors.append(
                    f"\n— Text length is more than {max_lenght} characters"
                )
            if True:
                for i in contains:
                    if "".join(args).find(i) == -1:
                        errors.append(f'\n— Not found "{i}"')
            if len(errors) > 0:
                return f'Your mistakes: {", ".join(errors)}'
            else:
                return func("".join(args))

        return check_string

    return wrap


@arg_rules(str, 15, ["com", "@"])
def create_slogan(name: str):
    return f"{name} drinks pepsi in his brand new BMW!"


print(create_slogan("ovasdaer@me.com"))
