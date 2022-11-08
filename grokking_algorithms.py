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
#    for i in range(len(massive)):
#        min_index = i
#        for j in range(i + 1, len(massive)):
#            if massive[min_index] > massive[j]:
#                min_index = j
#        massive[i], massive[min_index] = massive[min_index], massive[i]
#
#    return massive


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

# Mergesort
# def mergesort(massive):
#     def massive_merge(a, b):
#         i = j = 0
#         result = []
#         while i < len(a) and j < len(b):
#             if a[i] < b[j]:
#                 result.append(a[i])
#                 i += 1
#             else:
#                 result.append(b[j])
#                 j += 1
#         while i < len(a):
#             result.append(a[i])
#             i += 1
#         while j < len(b):
#             result.append(b[j])
#             j += 1
#         return result
#     if len(massive) == 1:
#         return massive
#     middle = len(massive) // 2
#     left = mergesort(massive[:middle])
#     right = mergesort(massive[middle:])
#     return massive_merge(left, right)
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 10))]
# print(random_massive)
# print(mergesort(random_massive))

# Bubble sort
# def bubble_sort(massive):
#     for i in range(len(massive) - 1):
#         for j in range(len(massive) - i - 1):
#             if massive[j] > massive[j + 1]:
#                 massive[j], massive[j + 1] = massive[j + 1], massive[j]
#     return massive
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 10))]
# print(random_massive)
# print(bubble_sort(random_massive))

# Insertion sort
# def insertion_sort(massive):
#     for i in range(1, len(massive)):
#         for j in range(i, 0, -1):
#             if massive[j] < massive[j - 1]:
#                 massive[j], massive[j - 1] = massive[j - 1], massive[j]
#             else:
#                 break
#     return massive
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 10))]
# print(random_massive)
# print(insertion_sort(random_massive))

# Heap sort
# def heapify(arr, n, i):
#     largest = i
#     left = 2 * i + 1
#     right = 2 * i + 2
#
#     if left < n and arr[i] < arr[left]:
#         largest = left
#
#     if right < n and arr[largest] < arr[right]:
#         largest = right
#
#     if largest != i:
#         arr[i], arr[largest] = arr[largest], arr[i]
#         heapify(arr, n, largest)
#
#
# def heap_sort(massive):
#     for i in range(len(massive) // 2, -1, -1):
#         heapify(massive, len(massive), i)
#     for i in range(len(massive) - 1, 0, -1):
#         massive[i], massive[0] = massive[0], massive[i]
#         heapify(massive, i, 0)
#     return massive
#
#
# random_massive = [randint(0, 100) for _ in range(randint(0, 10))]
# print(random_massive)
# print(heap_sort(random_massive))
