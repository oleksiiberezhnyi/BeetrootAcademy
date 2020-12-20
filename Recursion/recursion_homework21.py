# Berezhnyi Oleksii

from typing import Union


# Task 1


def to_power(x: Union[int, float], exp: int) -> Union[int, float]:
    if exp == 0:
        return 1
    elif exp < 0:
        raise ValueError('This function works only with exp > 0')
    else:
        return x * to_power(x, exp - 1)


print(to_power(3, 3))
print(to_power(3.5, 2))
print(to_power(2, 1))


# Task 2


def is_palindrome(looking_str: str) -> bool:
    if len(looking_str) == 0:
        return True
    else:
        if looking_str[0] == looking_str[-1]:
            return is_palindrome(looking_str[1: -1], index)
        else:
            return False


print(is_palindrome("m"))


# Task 3


def mult(a: int, n: int) -> int:
    if n == 1:
        return a
    else:
        return a + mult(a, n - 1)


print(mult(2, 10))


# Task 4


def reverse(input_str: str) -> str:
    if len(input_str) == 0:
        return input_str
    else:
        return f'{reverse(input_str[1:])}{input_str[0]}'


print(reverse("adrakadabra"))


# Task 5


def sum_of_digits(digit_string: str) -> int:
    if not digit_string.isdigit():
        raise ValueError('Input string must be digit string')
    else:
        if len(digit_string) == 1:
            return int(digit_string[0])
        return int(digit_string[0]) + sum_of_digits(digit_string[1:])


print(sum_of_digits("221134"))
assert sum_of_digits("26") == 8
