def choice_sort(array):
    for i in range(0, len(array)):
        for n in range(i+1, len(array)):
            if array[n] < array[i]:
                array[n], array[i] = array[i], array[n]
    return array


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]

assert choice_sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
