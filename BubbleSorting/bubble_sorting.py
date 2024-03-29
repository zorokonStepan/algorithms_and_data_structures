def bubble_sort(array):
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return array


def bubble_sort_2(array: list):
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def bubble_sort_3(arr):
    swapped = False
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return arr


lst = [5, 2, 3, 1, 4]

assert bubble_sort(lst) == [1, 2, 3, 4, 5]
assert bubble_sort_2(lst) == [1, 2, 3, 4, 5]
assert bubble_sort_3(lst) == [1, 2, 3, 4, 5]
