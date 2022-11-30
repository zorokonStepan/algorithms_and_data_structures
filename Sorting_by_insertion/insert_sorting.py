def insert_sort(array):
    for i in range(1, len(array)):
        while i > 0 and array[i] < array[i-1]:
            array[i], array[i-1] = array[i-1], array[i]
            i -= 1
    return array


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]
assert insert_sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
