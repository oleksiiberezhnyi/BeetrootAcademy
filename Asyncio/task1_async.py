import asyncio
import time


async def fibonacci(n):
    result = []
    n1 = 0
    n2 = 1
    for i in range(1, n + 1):
        result.append(n1)
        n1, n2 = n2, n1 + n2
    await asyncio.sleep(0.001)
    return result


async def factorial(n):
    result = []
    a = 1
    for i in range(1, n + 1):
        a *= i
        result.append(a)
    await asyncio.sleep(0.001)
    return result


async def square(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 2
        result.append(a)
    await asyncio.sleep(0.001)
    return result


async def cubic(n):
    result = []
    for i in range(1, n + 1):
        a = i ** 3
        result.append(a)
    await asyncio.sleep(0.001)
    return result


n = 100000


tasks = []
for task in [fibonacci(n), factorial(n), square(n), cubic(n)]:
    tasks.append(task)


async def main_asynchronous():
    await asyncio.gather(*tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    start_time = time.time()
    asyncio.run(main_asynchronous())
    end_time = time.time()
    print(f'Total time: {end_time - start_time}')
