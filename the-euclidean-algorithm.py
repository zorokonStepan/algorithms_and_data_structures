"""Алгоритм Евклида"""


def euclidean_algorithm(num1, num2):
    if num1 == 0:
        return num2
    elif num2 == 0:
        return num1
    else:
        if num1 < num2:
            num1, num2 = num2, num1

        if num1 % num2 == 0:
            return num2
        else:
            return euclidean_algorithm(num2, num1 % num2)


print(euclidean_algorithm(7, 5))
