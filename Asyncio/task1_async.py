import asyncio
import time


async def fibonacci(n):
    result = []
    n1 = 0
    n2 = 1
    for i in range(1, n + 1):
        await asyncio.sleep(0)
        result.append(n1)
        n1, n2 = n2, n1 + n2
    return result


async def factorial(n):
    result = []
    a = 1
    for i in range(1, n + 1):
        await asyncio.sleep(0)
        a *= i
        result.append(a)
    return result


async def square(n):
    result = []
    for i in range(1, n + 1):
        await asyncio.sleep(0)
        a = i ** 2
        result.append(a)
    return result


async def cubic(n):
    result = []
    for i in range(1, n + 1):
        await asyncio.sleep(0)
        a = i ** 3
        result.append(a)
    return result


n = 1000


async def main_asynchronous():
    start_time = time.time()
    print('Fibonacci: ', await fibonacci(n))
    print('Factorial: ', await factorial(n))
    print('Squares: ', await square(n))
    print('Cubics', await cubic(n))
    end_time = time.time()
    print(f'Total time: {end_time - start_time}')



if __name__ == '__main__':
    asyncio.run(main_asynchronous())
