"""Примеры рекурсий"""


# рекурсивная функция для подсчета суммы элементов списка
def summa_arr(arr: list):
    if not arr:
        return 0
    return arr[0] + summa_arr(arr[1:])


# print(summa_arr([1, 2, 3, 4, 5, 6]))

# рекурсивная функция для подсчета количества элементов списка
def len_arr(arr: list):
    if not arr:
        return 0
    return 1 + len_arr(arr[1:])


# print(len_arr([1, 2, 3]))

# Найдите наибольшее число в списке.
def max_elem(arr: list):
    if not arr:
        return None
    elif len(arr) == 1:
        return arr[0]

    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_elem(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max


A = [111, 2, 334, 4, 3232]
print(max_elem(A))
