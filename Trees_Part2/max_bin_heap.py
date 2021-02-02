class MaxBinHeap:

    def __init__(self):
        self.heap_list = []
        self.size = 0

    def insert(self, value):
        self.heap_list.append(value)
        self.size += 1
        self._up(self.size - 1)

    def delete_max(self):
        if self.size != 0:
            self.heap_list[self.size - 1], self.heap_list[0] = \
                self.heap_list[0], self.heap_list[self.size - 1]
            res = self.heap_list.pop()
            self.size -= 1
            self._down(0)
        else:
            res = "heap is empty"
        return res

    def max_element(self):
        if self.size != 0:
            return self.heap_list[0]
        else:
            return "heap is empty"

    def _up(self, index):
        center = index // 2
        if center < 0:
            return
        if self.heap_list[index] > self.heap_list[center]:
            self.heap_list[index], self.heap_list[center] = \
                self.heap_list[center], self.heap_list[index]
            self._up(center)

    def _down(self, index):
        child_index = 2 * index + 1
        if child_index >= self.size:
            return
        if child_index + 1 < self.size and self.heap_list[child_index] < \
                self.heap_list[child_index + 1]:
            child_index += 1
        if self.heap_list[child_index] > self.heap_list[index]:
            self.heap_list[child_index], self.heap_list[index] = \
                self.heap_list[index], self.heap_list[child_index]
            self._down(child_index)

    def __str__(self):
        result = ''
        for i in range(0, self.size // 2):
            result += f'left {str(self.heap_list[2 * i + 1])} | ' \
                      f'root {str(self.heap_list[2 * i])} | ' \
                      f'right {str(self.heap_list[2 * i + 2])}\n'
        return result


bin_heap = MaxBinHeap()
bin_heap.insert(5)
bin_heap.insert(7)
bin_heap.insert(3)
bin_heap.insert(1)
bin_heap.insert(15)
bin_heap.insert(4)
bin_heap.insert(8)

print(bin_heap)
print(bin_heap.delete_max())
print(bin_heap.delete_max())
print(bin_heap.delete_max())
print(bin_heap.delete_max())
print(bin_heap.delete_max())
print(bin_heap.delete_max())
print(bin_heap.delete_max())
