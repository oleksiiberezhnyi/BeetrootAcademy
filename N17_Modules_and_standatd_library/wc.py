# Task 3

def count_lines(filename):
    with open(filename, 'r') as file:
        print(f'Count of lines in {filename}: {len(file.readlines())}')


def count_chars(filename):
    with open(filename, 'r') as file:
        print(f'Count of chars in {filename}: {len(file.read())}')


def test(filename):
    count_lines(filename)
    count_chars(filename)
