import threading

class Counter(threading.Thread):

    counter = 0
    rounds = 1_000_000

    def __init__(self):
        super().__init__()

    def run(self):
        for _ in range(0, self.rounds):
            self.counter += 1

    def get_counter(self):
        return self.counter

    def __str__(self):
        return f'{self.getName()}: counter = {self.counter}'


thread_1 = Counter()
thread_2 = Counter()

thread_1.start()
thread_2.start()

# thread_1.join()
# thread_2.join()

total = thread_1.get_counter() + thread_2.get_counter()
# print(thread_1)
# print(thread_2)
print(total)
