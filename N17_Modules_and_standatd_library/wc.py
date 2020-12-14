# Task 3

def count_lines(filename):
    with open(filename, 'r') as file:
        return len(file.readlines())


def count_chars(filename):
    with open(filename, 'r') as file:
        return len(file.read())


def test(filename):
    return count_lines(filename), count_chars(filename)
