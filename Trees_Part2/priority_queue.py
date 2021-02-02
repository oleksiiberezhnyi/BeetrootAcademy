from max_bin_heap import MaxBinHeap


class PriorityQueue(MaxBinHeap):

    def __init__(self):
        super().__init__()
        self._queue = []
        self._size = 0

    def enqueue(self, item: MaxBinHeap):
        self._queue.append(item.delete_max())
        self._size += 1

    def dequeue(self):
        if self._size > 0:
            self._size -= 1
            return self._queue.pop()
        else:
            return 'Queue is empty'

    def __repr__(self):
        result = '<Queue>\n'
        for i in range(self._size):
            result += f'{self._queue[i]}\n'
        return result

    def __str__(self):
        return self.__repr__()


bin_heap = MaxBinHeap()
bin_heap.insert(5)
bin_heap.insert(7)
bin_heap.insert(3)
bin_heap.insert(1)
bin_heap.insert(15)
bin_heap.insert(4)
bin_heap.insert(8)

print(bin_heap)

queue = PriorityQueue()
queue.enqueue(bin_heap)
queue.enqueue(bin_heap)
queue.enqueue(bin_heap)
queue.enqueue(bin_heap)
print(queue)

queue.dequeue()

print(queue)
