"""Быстрая сортировка"""


def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    less = [i for i in arr[1:] if i <= pivot]
    greater = [i for i in arr[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)


A = [9, 30, 15, 81, 9, 9, 30, 15, 74]
print(quick_sort(A))
