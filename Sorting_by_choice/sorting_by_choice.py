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


A = [9, 1, 3, 6, 8, 2, 7, 5, 4]
print(sorting_by_choice(A))
