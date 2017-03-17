from itertools import chain

class Matrix:

    # m x n matrix -- row major, 0 index
    def __init__(self, m, n, a, ia, ja):
        self.m = 10
        self.n = 10
        self.a = a
        self.ia = ia
        self.ja = ja

    # Length returns # of nonzero elements
    def __len__(self):
        return len(self.a)

    def shape(self):
        return (self.m, self.n)

    @staticmethod
    def tridiagonal(size = 10):
        sequence = [-1, 2, -1]
        print "helllooo"
        a = sequence[1:]
        ia = [0, 2]
        ja = [0, 1]
        ia_sum = 2
        ja_ptr = 1  # what column are we inserting on?
        for i in range(1, size-1):
            ia_sum += 3
            ia.append(ia_sum)
            ja.append(ja_ptr)
            ja.append(ja_ptr + 1)
            ja.append(ja_ptr + 2)
            ja_ptr += 3
            a += sequence
        a += sequence[:-1]
        return Matrix(10, 10, a, ia, ja)
