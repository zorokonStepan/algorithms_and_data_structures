def comb_sort(seq):
    step = len(seq) - 1
    while step > 0:
        for i in range(0, len(seq)-step):
            if seq[i] > seq[i+step]:
                seq[i], seq[i+step] = seq[i+step], seq[i]
        step = int(step // 1.247)
    return seq


a = [7, 5, 1, 4, 8, 9, 3, 2, 6]
assert comb_sort(a) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
