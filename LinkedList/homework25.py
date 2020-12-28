class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return f'{self.data}'

    def __str__(self):
        return self.__repr__()

    def __bool__(self):
        return self.data is not None


class UnorderedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def append(self, data=None):
        self.size += 1
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        if self.size > 1:
            new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def index(self, data):
        current_node = self.head
        node_id = 0
        while current_node is not None:
            if current_node.get_data() == data:
                return node_id
            current_node = current_node.get_next()
            node_id += 1
        raise ValueError(f'{data} not found')

    def pop(self):
        self.size -= 1
        result = self.tail
        self.tail = self.tail._prev
        self.tail._next = None
        return result

    def insert(self, data, index=-1):
        if index == -1:
            self.append(data)
            return
        new_node = Node(data)
        current_node_index = 0
        current_node = self.head
        prev_node = self.head
        if index > self.size:
            raise ValueError('Node index overflow')
        while current_node is not None:
            if current_node_index == index:
                prev_node._next = new_node
                new_node.prev = prev_node
                new_node.next = current_node
                self.size += 1
                break
            prev_node = current_node
            current_node = current_node._next
            current_node_index += 1

    def __len__(self):
        return self.size

    def __getitem__(self, item):
        copy_list = UnorderedList()
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if stop > self.size:
                raise IndexError
            slice_list = range(start, stop, step)
            current_node = self.head
            current_index = 0
            while current_node is not None:
                if current_index in slice_list:
                    copy_list.append(current_node.get_data())
                current_node = current_node._next
                current_index += 1
        if isinstance(item, int):
            if item > self.size:
                raise IndexError
            current_node = self.head
            current_index = 0
            while current_node is not None:
                if current_index == item:
                    copy_list.append(current_node.get_data())
                current_node = current_node._next
                current_index += 1
        return copy_list

    def __repr__(self):
        current_node = self.head
        result = ''
        if self.size < 1:
            result = 'None'
        elif self.size == 1:
            result = str(current_node.get_data())
        else:
            while current_node is not None:
                result += f'{str(current_node.get_data())} --> '
                current_node = current_node.get_next()
        return result

    def __str__(self):
        return self.__repr__()


linked_list = UnorderedList()
for i in range(3, 57, 4):
    print(f'Appending {i}')
    linked_list.append(i)
print(linked_list)
print('Pop element:')
linked_list.pop()
print(linked_list.pop())
print(linked_list)
print(f'Index of 45: {linked_list.index(27)}')
print(f'Insert 867 into 1 position: {linked_list.insert(867, 1)}')
print(linked_list)
print(f'Insert 999 into 1 position: {linked_list.insert(999, 1)}')
print(linked_list)
print(f'Lenght = {len(linked_list)}')
print(f'2:6:1 item = {linked_list[2:6:1]} {type(linked_list)}')
print(f'4th item = {linked_list[4]} {type(linked_list)}')


# Task 2


class Stack:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not bool(self.head)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_data = Node(data)
            new_data.next = self.head
            self.head = new_data

    def pop(self):
        if self.is_empty():
            return None
        else:
            prev_node = self.head
            self.head = self.head._next
            prev_node._next = None
            return prev_node._data

    def __repr__(self):
        iter_node = self.head
        result = '<Stack>\n'
        if self.is_empty():
            print("Stack Empty")
        else:
            while iter_node is not None:
                result += f'{iter_node._data}\n'
                iter_node = iter_node._next
            return result

    def __str__(self):
        return self.__repr__()


stack_list = Stack()
stack_list.push(1)
stack_list.push(2)
stack_list.push(3)
stack_list.push(4)
print(stack_list)
stack_list.pop()
print(stack_list)


class Queue:

    def __init__(self):
        self.head = None

    def is_empty(self):
        return not bool(self.head)

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_data = Node(data)
            new_data.next = self.head
            self.head = new_data

    def get(self):
        if self.is_empty():
            return None
        else:
            current_node = self.head
            prev_node = None
            while current_node.get_next() is not None:
                prev_node = current_node
                current_node = current_node.get_next()
            prev_node.set_next(None)
            return

    def __repr__(self):
        iter_node = self.head
        result = '<Queue>\n'
        if self.is_empty():
            print("Queue Empty")
        else:
            while iter_node is not None:
                result += f'{iter_node._data}\n'
                iter_node = iter_node._next
            return result

    def __str__(self):
        return self.__repr__()


queue_list = Queue()
queue_list.push(1)
queue_list.push(2)
queue_list.push(3)
queue_list.push(4)
print(queue_list)
queue_list.get()
print(queue_list)
