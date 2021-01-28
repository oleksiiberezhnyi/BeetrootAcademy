from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


NUMBERS = [2,  # prime
           1099726899285419,
           1570341764013157,  # prime
           1637027521802551,  # prime
           1880450821379411,  # prime
           1893530391196711,  # prime
           2447109360961063,  # prime
           3,  # prime
           2772290760589219,  # prime
           3033700317376073,  # prime
           4350190374376723,
           4350190491008389,  # prime
           4350190491008390,
           4350222956688319,
           2447120421950803,
           5,  # prime
           ]


def is_prime(numbers):
    def prime(n):
        a = 2
        while a ** 2 <= n and n % a != 0:
            a += 1
        return a ** 2 > n
    for number in numbers:
        print(number, prime(number))


thread_start_time = time.time()
thread_executor = ThreadPoolExecutor(max_workers=len(NUMBERS))
thread = thread_executor.submit(is_prime(NUMBERS))
thread_end_time = time.time()
thread_time = thread_end_time - thread_start_time

process_start_time = time.time()
process_executor = ProcessPoolExecutor(max_workers=len(NUMBERS))
process = thread_executor.submit(is_prime(NUMBERS))
process_end_time = time.time()
process_time = process_end_time - process_start_time

print(f'thread time: {thread_time}')
print(f'process time: {process_time}')
print(f'delta: {thread_time - process_time}')
