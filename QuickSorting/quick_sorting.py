from random import randint


def quicksort(array):
    # Если входной массив содержит менее двух элементов, затем вернуть его как результат функции
    if len(array) < 2:
        return array
    low, same, high = [], [], []
    # Выберите свой элемент 'pivot' случайным образом
    pivot = array[randint(0, len(array) - 1)]
    for item in array:
        # Элементы, которые меньше, чем 'pivot', переходят в список 'low'.
        # Элементы, размер которых превышает 'pivot' перейти в список 'high'.
        # Элементы, которые равны 'pivot' перейти к списку 'same'.
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        elif item > pivot:
            high.append(item)
    # Окончательный результат объединяет отсортированный 'low' список с тем же списком и отсортированным списком 'high'
    return quicksort(low) + same + quicksort(high)


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]

assert quicksort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
