# Task 1

def number_of_locals(func):
    return func.__code__.co_nlocals


def test_function():
    a = 1
    b = 2.5
    c = "string"


print(number_of_locals(test_function))


# Task 2

def function_outside(pow):
    def function_inside(pow2):
        return [(i, i ** pow) for i in range(1, pow ** pow2, pow2 * 2)]

    return function_inside


print(function_outside(4)(1))

# Task 3

def choose_func(nums: list, func1, func2):
    negative = 0
    for i in nums:
        if i < 0:
            negative = 1
            break
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
