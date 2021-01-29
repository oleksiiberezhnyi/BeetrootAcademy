import asyncio
import time


async def fibonacci(n):
    result = []
    n1 = 0
    n2 = 1
    for i in range(1, n + 1):
        result.append(n1)
        n1, n2 = n2, n1 + n2
    return result


async def factorial(n):
    result = []
    a = 1
    for i in range(1, n + 1):
        a *= i
        result.append(a)
    return result


async def square(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 2
        result.append(a)
    return result


async def cubic(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 3
        result.append(a)
    return result


n = 999


async def main_asynchronous():
    start_time = time.time()
    fib = loop.create_task(fibonacci(n))
    fact = loop.create_task(factorial(n))
    sq = loop.create_task(square(n))
    cub = loop.create_task(cubic(n))
    await asyncio.wait([fib, fact, sq, cub])
    end_time = time.time()
    print(f'Total time: {end_time - start_time}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main_asynchronous())
    loop.close()