from random import randint


# Binary Search
# def bin_search(massive):
#     num = int(input())
#     low, high = 0, len(massive) - 1
#     while low <= high:
#         mid = (low + high) // 2
#         guess = massive[mid]
#         if guess == num:
#             return 'Искомый элемент находится под индексом ' + str(mid)
#         elif guess > num:
#             high = mid - 1
#         else:
#             low = mid + 1
#     return None
#
#
# random_massive = sorted([randint(0, 100) for _ in range(10)])
# print(random_massive)
# print(bin_search(random_massive))

# Selection Sort
# def selection_sort(massive):
#     for i in range(len(massive) - 1):
#         smallest = massive[i]
#         smallest_index = i
#         for j in range(i + 1, len(massive)):
#             if smallest > massive[j]:
#                 smallest = massive[j]
#                 smallest_index = j
#         if smallest_index != i:
#             massive[i], massive[smallest_index] = massive[smallest_index], massive[i]
#
#     return massive
#
#
# random_massive = [randint(0, 100) for _ in range(10)]
# print(random_massive)
# print(selection_sort(random_massive))

# Sum array recursion
# def sum_of_elements(massive):
#     if len(massive) == 0:
#         return 0
#     else:
#         return massive[0] + sum_of_elements(massive[1:])
#
#
# random_massive = [randint(0, 100) for _ in range(10)]
# print(random_massive)
# print(sum_of_elements(random_massive))

# Array elements counting recursion
# def counting(massive):
#     if len(massive) == 0:
#         return 0
#     else:
#         return 1 + counting(massive[1:])
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 1))]
# print(random_massive)
# print(counting(random_massive))

# Finding max number in massive by recursion
# def max_number(massive):
#     if len(massive) == 2:
#         return massive[0] if massive[0] > massive[1] else massive[1]
#     elif len(massive) < 2:
#         return massive
#     return massive[0] if massive[0] > max_number(massive[1:]) else max_number(massive[1:])
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 10))]
# print(random_massive)
# print(max_number(random_massive))

# Quicksort
# def quicksort(massive):
#     if len(massive) < 2:
#         return massive
#     pivot_el = massive[0]
#     less_than_pivot = [i for i in massive[1:] if i < pivot_el]
#     pivot_equals = [i for i in massive if i == pivot_el]
#     greater_than_pivot = [i for i in massive[1:] if i > pivot_el]
#     return quicksort(less_than_pivot) + pivot_equals + quicksort(greater_than_pivot)
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 10))]
# print(random_massive)
# print(quicksort(random_massive))

