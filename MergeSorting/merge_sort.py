"""Сортировка слиянием"""


def Merge(A, p, q, r):
    # Делаем копии обоих массивов, которые мы пытаемся объединить
    # Увеличиваем второй параметр на 1
    p_copy = A[p:q + 1]
    r_copy = A[q + 1:r + 1]

    # Начальные значения для переменных, которые мы используем для хранения
    # игдекса, где мы остановились в каждом массиве
    p_copy_index = 0
    r_copy_index = 0
    sorted_index = p

    # Проходим обе копии массивов, пока у нас не закончатся элементы в одной из них
    while p_copy_index < len(p_copy) and r_copy_index < len(r_copy):

        if p_copy[p_copy_index] <= r_copy[r_copy_index]:
            A[sorted_index] = p_copy[p_copy_index]
            p_copy_index = p_copy_index + 1
        else:
            A[sorted_index] = r_copy[r_copy_index]
            r_copy_index = r_copy_index + 1

        sorted_index = sorted_index + 1

    # У нас закончились элементы в p_copy или r_copy
    # пройдемся по оставшимся элементам и добавим их
    while p_copy_index < len(p_copy):
        A[sorted_index] = p_copy[p_copy_index]
        p_copy_index = p_copy_index + 1
        sorted_index = sorted_index + 1

    while r_copy_index < len(r_copy):
        A[sorted_index] = r_copy[r_copy_index]
        r_copy_index = r_copy_index + 1
        sorted_index = sorted_index + 1


def Sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        Sort(A, p, q)
        Sort(A, q + 1, r)
        Merge(A, p, q, r)


array = [33, 42, 9, 37, 8, 47, 5, 29, 49, 31, 4, 48, 16, 22, 26]
Sort(array, 0, len(array) - 1)
print(array)

# Пример массива:
A = [5, 2, 4, 6, 1, 3, 2, 6]

# Примера запуска:
Sort(A, 0, len(A) - 1)
print(A)
