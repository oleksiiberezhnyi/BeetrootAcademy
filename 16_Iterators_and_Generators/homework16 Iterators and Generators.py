"""
Berezhnyi Oleksii
Homework 16. Iterators and Generators
"""


# Task 1


def with_index(iterable, start=0):
    for i in iterable:
        start += 1
        yield start - 1, i


s = {1, "string", 4, True}
print(list(with_index(s, 10)))


# Task 2


def in_range(start, end, step=1):
    if start < end:
        while start < end:
            start += abs(step)
            yield start - abs(step)
    else:
        while start > end:
            start -= abs(step)
            yield start + abs(step)


r = in_range(1, -100, -10)
for i in r:
    print(i)
print("*" * 80)
for i in range(1, -100, -10):  #
    print(i)


# Task 3


class Iterable:

    def __init__(self, iterable):
        self._iterable = iterable
        self._index = len(iterable)
        self._i = -1

    def __getitem__(self, item):
        self._i += 1
        return self._iterable[self._i]


iter = Iterable([2, 3, 5, 7])
for i in iter:
    print(i)
