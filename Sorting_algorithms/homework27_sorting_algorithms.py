from random import randint
import time


# Task 1

def bubble_sort_in_both_directions(arr):
    start = 0
    stop = len(arr) - 1
    reverse_directions = True
    while reverse_directions is True:
        reverse_directions = False
        for i in range(start, stop):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                reverse_directions = True
        if reverse_directions is False:
            break
        reverse_directions = False
        stop -= 1
        for i in range(stop - 1, start - 1, -1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                reverse_directions = True
        start += 1


list1 = [1, 4, 2, 5, 7, 2, 1, 9, 3, 5]
bubble_sort_in_both_directions(list1)
for i in range(len(list1)):
    print(list1[i], end=', ')


# Task 2


def merge_sort(arr: list):
    if len(arr) <= 1:
        return arr
    left_list = []
    right_list = []
    center = len(arr) // 2
    i = 0
    while i < center:
        left_list.append(arr[i])
        i += 1
    while i >= center:
        if i < len(arr):
            right_list.append(arr[i])
            i += 1
        else:
            break
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)

    def merge(left: list, right: list):
        merged_list = []
        while len(left) != 0 and len(right) != 0:
            if left[0] < right[0]:
                merged_list.append(left[0])
                left.remove(left[0])
            else:
                merged_list.append(right[0])
                right.remove(right[0])
        if len(left) == 0:
            merged_list += right
        else:
            merged_list += left
        return merged_list

    return list(merge(left_list, right_list))


list2 = [1, 4, 2, 5, 7, 2, 1, 9, 3, 5, 8]
print('\n', merge_sort(list2))


# Task 3


def quick_sort(arr):
    quick_sort_helper(arr, 0, len(arr) - 1)


def quick_sort_helper(arr, first, last):
    if first < last:
        split_point = partition(arr, first, last)

        quick_sort_helper(arr, first, split_point - 1)
        quick_sort_helper(arr, split_point + 1, last)


def partition(arr, first, last):
    pivot_value = arr[first]

    left_mark = first + 1
    right_mark = last

    done = False
    while not done:

        while left_mark <= right_mark and arr[left_mark] <= pivot_value:
            left_mark = left_mark + 1

        while arr[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1

        if right_mark < left_mark:
            done = True
        else:
            temp = arr[left_mark]
            arr[left_mark] = arr[right_mark]
            arr[right_mark] = temp

    temp = arr[first]
    arr[first] = arr[right_mark]
    arr[right_mark] = temp

    return right_mark


list3 = []
for i in range(0, 1000):
    n = randint(1, 100000)
    list3.append(n)
print(list3)
quick_sort(list3)
for i in range(len(list3)):
    print(list3[i], end=', ')
