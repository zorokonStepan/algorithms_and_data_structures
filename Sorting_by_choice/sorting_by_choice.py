"""Сортировка выбором"""


def find_smallest(arr):
    smallest_index = 0
    smallest = arr[smallest_index]
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def sorting_by_choice(arr: list):
    new_arr = []
    for i in range(len(arr)):
        smallest_index = find_smallest(arr)
        new_arr.append(arr.pop(smallest_index))
    return new_arr


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]

assert sorting_by_choice(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
