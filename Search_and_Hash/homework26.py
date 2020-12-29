# Task 1

def binary_search(data, value):
    if value > data[len(data) - 1] or value < data[0]:
        return f'{value} is override'

    def search(first_element, last_element):
        center = (first_element + last_element) // 2
        if value == data[center]:
            return center
        elif data[center] > value:
            return search(first_element, center)
        elif data[center] < value:
            return search(center + 1, last_element)
        else:
            return f'{value} not found'

    return search(0, len(data) - 1)


# Task 2


def fibonacci_search(data, value):
    if type(data) == dict:
        data = list(data.values())
    if value < data[0] or value > data[-1]:
        return f'{value} is override'
    a = 0
    b = 1
    fib = b + a
    while fib < len(data):
        a = b
        b = fib
        fib = b + a
    index = -1
    while fib > 1:
        idx = min(index + a, (len(data) - 1))
        if data[idx] < value:
            fib = b
            b = a
            a = fib - b
            index = idx
        elif data[idx] > value:
            fib = a
            b = b - a
            a = fib - b
        else:
            return idx
    if b and index < (len(data) - 1) and data[index + 1] == value:
        return index + 1
    return f'{value} not found!'


data_list2 = list(range(2, 1000, 2))
print(data_list2)
print(f'binary search = {binary_search(data_list2, 998)}')
print(f'fibonacci search = {fibonacci_search(data_list2, 455)}')


# Task 3


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, data):
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] is None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slots[hash_value] == key:
                self.data[hash_value] = data
            else:
                next_slot = self.re_hash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[
                    next_slot] != key:
                    next_slot = self.re_hash(next_slot, len(self.slots))

                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data

    @staticmethod
    def hash_function(key, size):
        return key % size

    @staticmethod
    def re_hash(old_hash, size):
        return (old_hash + 1) % size

    def get(self, key):
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] is not None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.re_hash(position, len(self.slots))
                if position == start_slot:
                    stop = True

        return data

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)

    def __contains__(self, key):
        try:
            _ = self.__getitem__(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.size


H = HashTable()
H[54] = "cat"
H[26] = "dog"
H[93] = "lion"
H[17] = "tiger"
H[77] = "bird"
H[31] = "cow"
H[44] = "goat"
H[55] = "pig"
H[20] = "chicken"
print(f'slots = {H.slots}')
print(f'data = {H.data}')
print(f'data in slots [20] = {H[20]}')
print(f'data in slots [17] = {H[17]}')
H[20] = "duck"
print(f'replace data in slots [20] = {H[20]}')
print(f'data in slots [99] = {H[99]}')
if 25 in H:
    print('True')
else:
    print('False')
print(len(H))
