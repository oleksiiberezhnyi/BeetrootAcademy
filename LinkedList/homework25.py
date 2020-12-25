class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next

    def __repr__(self):
        return f'{self.data} | {self.next}'


class UnorderedList:

    def __init__(self):
        self.head = None

    def append(self, data = None):
        new_data = Node(data)
        if self.head is None:
            self.head = new_data
            return
        prev_node = self.head
        while prev_node.next:
            prev_node = prev_node.next
        prev_node.next = new_data

    def index(self, data):
        current_node = self.head
        node_id = 0
        result = []
        while current_node is not None:
            if current_node.get_data() == data:
                result.append(node_id)
            current_node = current_node.get_next()
            node_id += 1
        return result

    def pop(self):
        current_node = self.head
        prev_node = None
        while current_node.get_next() is not None:
            prev_node = current_node
            current_node = current_node.get_next()
        prev_node.set_next(None)
        return

    def insert(self, data, index = 0):
        current_node = self.head
        prev_node = None
        new_data = Node(data)
        idx = 0
        while current_node is not None and idx < index:
            prev_node = current_node
            current_node = current_node.get_next()
            idx += 1
        if index == 0:
            new_data.set_next(self.head)
            self.head = new_data
        else:
            if current_node is None:
                prev_node.set_next(new_data)
            else:
                new_data.set_next(current_node)
                prev_node.set_next(new_data)

    def _size(self):
        current_node = self.head
        size = 0
        while current_node is not None:
            current_node = current_node.get_next()
            size += 1
        return size

    def __len__(self):
        return self._size()

    def __getitem__(self, item):
        self.result = None
        print(f'_____ {self.result}')
        if isinstance(item, slice):
            start = item.start
            stop = item.stop
            step = item.step
            if stop > self._size():
                raise IndexError
            slice_list = range(start, stop, step)
            current_node = self.head
            current_index = 0
            # print(f'0000 {self.result}')
            while current_node is not None:
                # print(f'1 {current_node.get_data()}')
                if current_index in slice_list:
                    new_data = Node(current_node.get_data())
                    # print(f'new data {new_data}')
                    if self.result is None:
                        # print(f'result {self.result}')
                        self.result = new_data
                        # print((f'new result {self.result}'))
                    prev_node = self.result
                    # print(f'prevprevprev{self.result}')
                    # print(f'prev_node {prev_node}')
                    # print(f'prev_node next {prev_node.get_next()}')
                    while prev_node.next is not None:
                        prev_node = prev_node.next
                        # print(f'next next {prev_node}')
                    prev_node.set_next(new_data)
                current_node = current_node.next
                # print(f'22 {current_node}')
                current_index += 1


        if isinstance(item, int):
            index = item
            print(index)
        return self.result

    def __repr__(self):
        next_node = self.head
        result = ''
        while next_node:
            result += f'{str(next_node.get_data())} --> '
            next_node = next_node.get_next()
        return result

    def __str__(self):
        return self.__repr__()


l = UnorderedList()
l.append(3)
l.append(45)
l.append(45)
l.append(67)
l.append(765)
print(l)
l.pop()
print(l)
print(l.index(45))
l.insert(867, 1)
print(l)
print(len(l))


# Task 2


class Stack:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_data = Node(data)
            new_data.next = self.head
            self.head = new_data

    def pop(self):
        if self.isempty():
            return None
        else:
            prev_node = self.head
            self.head = self.head.next
            prev_node.next = None
            return prev_node.data

    def __repr__(self):
        iter_node = self.head
        result = ''
        if self.isempty():
            print("Stack Empty")
        else:
            while (iter_node != None):
                result += (f'{iter_node.data}\n|\nV\n ')
                iter_node = iter_node.next
            return result

    def __str__(self):
        return self.__repr__()


stack_list = Stack()
stack_list.push('sdkfj')
stack_list.push('234')
stack_list.push('asjhdg')
stack_list.push(345)
print(stack_list)
stack_list.pop()
print(stack_list)


class Queue:

    def __init__(self):
        self.head = None

    def isempty(self):
        if self.head is None:
            return True
        else:
            return False

    def push(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new_data = Node(data)
            new_data.next = self.head
            self.head = new_data

    def get(self):
        if self.isempty():
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
        result = ''
        if self.isempty():
            print("Queue Empty")
        else:
            while (iter_node != None):
                result += (f'{iter_node.data}\n|\nV\n ')
                iter_node = iter_node.next
            return result

    def __str__(self):
        return self.__repr__()


queue_list = Queue()
queue_list.push('sdkfj')
queue_list.push('234')
queue_list.push('asjhdg')
queue_list.push(345)
print(queue_list)
queue_list.get()
print(queue_list)