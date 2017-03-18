import numpy

class Matrix:

    # m x n matrix -- row major, 0 index
    def __init__(self, m, n, a, ia, ja):
        self.m = m
        self.n = n
        self.a = a
        self.ia = ia
        self.ja = ja

    # Length returns # of nonzero elements
    def __len__(self):
        return len(self.a)

    def shape(self):
        return (self.m, self.n)

    def transpose(self):
        print "who the f knows"

    # Vector should come in as numpy matrix
    # e.g. mat * vect
    def mult_vect_right(self, v):
        # a  -> nnz
        # ia -> m + 1
        # ja -> nnz
        vals = []
        for row in range(0, self.m):   # row
            summation = 0
            for l in range(self.ia[row], self.ia[row + 1]):  # j is used to fetch item and determine col
                col = self.ja[l]
                val = self.a[l]
                summation += float(v[col, 0]) * val
            vals.append(summation)
        return numpy.matrix(vals).T


    @staticmethod
    # Generate a useful, invertable tridiagonal matrix like:
    #   [ [  2, -1,  0 ],
    #     [ -1,  2, -1 ],
    #     [  0, -1,  2 ] ]
    # of any size.
    def tridiagonal(size = 10):
        sequence = [-1, 2, -1]
        a = sequence[1:]
        ia = [0, 2]
        ja = [0, 1]
        ia_sum = 2
        ja_ptr = 0  # what column are we inserting on?
        for i in range(1, size-1):
            print i
            ia_sum += 3
            ia.append(ia_sum)
            ja.append(ja_ptr)
            ja.append(ja_ptr + 1)
            ja.append(ja_ptr + 2)
            ja_ptr += 1
            a += sequence
        a += sequence[:-1]
        ia.append(len(a))
        ja += [size - 2, size - 1]
        return Matrix(size, size, a, ia, ja)
