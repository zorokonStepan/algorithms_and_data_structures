"""Быстрая сортировка"""


def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]

assert quick_sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
