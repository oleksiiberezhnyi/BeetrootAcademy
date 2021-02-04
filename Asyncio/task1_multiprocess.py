import multiprocessing
import time


def fibonacci(n):
    result = []
    n1 = 0
    n2 = 1
    for i in range(1, n + 1):
        result.append(n1)
        n1, n2 = n2, n1 + n2
    return result


def factorial(n):
    result = []
    a = 1
    for i in range(1, n + 1):
        a *= i
        result.append(a)
    return result


def square(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 2
        result.append(a)
    return result


def cubic(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 3
        result.append(a)
    return result


n = 999


def main_multiprocess():
    start_time = time.time()

    fibonacci_process = multiprocessing.Process(target=fibonacci, args=(n, ))
    factorial_process = multiprocessing.Process(target=factorial, args=(n, ))
    square_process = multiprocessing.Process(target=square, args=(n, ))
    cubic_process = multiprocessing.Process(target=cubic, args=(n, ))

    fibonacci_process.start()
    factorial_process.start()
    square_process.start()
    cubic_process.start()

    fibonacci_process.join()
    factorial_process.join()
    square_process.join()
    cubic_process.join()

    end_time = time.time()
    print(f'Total time: {end_time - start_time}')


if __name__ == '__main__':
    main_multiprocess()
