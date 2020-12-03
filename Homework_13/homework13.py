import random


# Task 1

def test_function():
    a = 1
    b = 2.5
    c = "string"


print(test_function.__code__.co_nlocals)


# Task 2

def function_outside(function_inside, pow):
    return function_inside(
        [(i, i ** pow) for i in range(1, pow ** pow, pow * 2)])




# Task 3

def choose_func(nums: list, func1, func2):
    negative = 0
    for i in nums:
        if i < 0:
            negative = 1
    if negative > 0:
        return func2(nums)
    else:
        return func1(nums)


def square_nums(nums):
    return [num ** 2 for num in nums]


def remove_negatives(nums):
    return [num for num in nums if num > 0]


nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
print(choose_func(nums1, square_nums, remove_negatives))
