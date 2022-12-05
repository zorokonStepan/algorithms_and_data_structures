def merge_sort(array):
    if len(array) <= 1:
        return array
    L = merge_sort(array[:len(array) // 2])
    R = merge_sort(array[len(array) // 2:])
    B = []
    l = r = 0
    while l < len(L) and r < len(R):
        B.append(L[l] if L[l] <= R[r] else R[r])
        [l, r] = [l + 1, r] if L[l] <= R[r] else [l, r + 1]
    for l in range(l, len(L)):
        B.append(L[l])
    for r in range(r, len(R)):
        B.append(R[r])
    return B


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]

assert merge_sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
