def shaker(data):	
    up = range(len(data) - 1)
    while True:
        for indices in (up, reversed(up)):
            swapped = False
            for i in indices:
                if data[i] > data[i+1]:
                    data[i], data[i+1] = data[i+1], data[i]
                    swapped = True
            if not swapped:
                return data


lst = [5, 2, 3, 1, 4, 8, 7, 9, 6]

assert shaker(lst) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
