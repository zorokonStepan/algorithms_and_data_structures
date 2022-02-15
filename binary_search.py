"""Бинарный поиск"""


def binary_search(lst: list, search_element: int):
    # low - нижняя, high - верхняя границы поиска
    low = 0
    high = len(lst) - 1

    while low <= high:
        # mid - середина диапозона поиска
        mid = (high + low) // 2
        # guess - средний элемент из диапозона поиска
        guess = lst[mid]

        if guess == search_element:
            return mid
        elif guess < search_element:
            low = mid + 1
        else:
            high = mid - 1

    return None


A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]

print(binary_search(A, 1))

# my_list = [1, 3, 5, 7, 9]
#
# print(binary_search(my_list, 9))
# print(binary_search(my_list, -1))
