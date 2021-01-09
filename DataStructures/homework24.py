# Berezhnyi Oleksii
# Task 1


class Stack:

    def __init__(self):
        self._stack = []
        self._index = -1

    def append(self, element):
        self._stack.append(element)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            return f'Stack is empty'

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == len(self._stack):
            raise StopIteration
        return self._stack[self._index]
        
    def __repr__(self):
        represent = '<Stack>\n'
        represent += '\n'.join(reversed(self._queue))
        return represent

    def __str__(self):
        return self.__repr__()
            
        
def reverse_order(sequence):
    reverse_sequence = ''
    chars = Stack()
    for i in sequence:
        chars.append(i)
    for j in sequence:
        reverse_sequence += chars.pop()
    return reverse_sequence
        
        
print(reverse_order("Hello World!"))



# Task 2

def balanced_brackets(sequence):
    brackets_string = ''
    brackets_string_reversed = ''
    brackets = Stack()
    brackets.append(sequence.count('('))
    brackets.append(sequence.count('['))
    brackets.append(sequence.count('{'))
    brackets.append(sequence.count('}'))
    brackets.append(sequence.count(']'))
    brackets.append(sequence.count(')'))
    for i in brackets:
        brackets_string += str(i)
        brackets_string_reversed += str(brackets.pop())
    if brackets_string == brackets_string_reversed:
        return f'brackets is balanced'
    else:
        return f'brackets isn\'t balanced'


print(balanced_brackets('print(reverse_order("Hello World!")'))
print(balanced_brackets(''))


def test():
    for i in range(100):
        print(i)


test()


# Task 3


class StackExtend:

    def __init__(self):
        self._stack = []
        self._index = -1

    def append(self, element):
        self._stack.append(element)

    def pop(self):
        try:
            return self._stack.pop()
        except IndexError:
            return f'Stack is empty'

    def get_from_stack(self, element):
        try:
            return self._stack.index(element)
        except ValueError:
            raise Exception(f'Your {element} not found in stack')

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == len(self._stack):
            raise StopIteration
        return self._stack[self._index]
        
    def __repr__(self):
        represent = '<Stack>\n'
        represent += '\n'.join(reversed(self._stack))
        return represent

    def __str__(self):
        return self.__repr__()


class QueueExtend:

    def __init__(self):
        self._queue = []
        self._index = -1

    def append(self, element):
        self._queue.append(element)

    def pop(self):
        try:
            return self._queue.pop(0)
        except IndexError:
            return f'Queue is empty'

    def get_from_queue(self, element):
        try:
            return self._queue.index(element)
        except ValueError:
            raise Exception(f'Your {element} not found in queue')

    def __iter__(self):
        return self

    def __next__(self):
        self._index += 1
        if self._index == len(self._queue):
            raise StopIteration
        return self._queue[self._index]
        
    def __repr__(self):
        represent = '<Queue>\n' 
        represent += '\n'.join(reversed(self._queue))
        return represent

    def __str__(self):
        return self.__repr__()


ext_list = StackExtend()
ext_list.append('1')
ext_list.append('12')
ext_list.append('456')
ext_list.append('34')
ext_list.append('453')
print(ext_list.get_from_stack('34'))

ext_list2 = QueueExtend()
ext_list2.append('1')
ext_list2.append('12')
ext_list2.append('456')
ext_list2.append('34')
ext_list2.append('453')
ext_list2.pop()
print(ext_list2)
ext_list2.pop()
print(ext_list2)
print(ext_list2.get_from_queue('34'))
