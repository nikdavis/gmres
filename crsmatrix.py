import numpy
from random import random

class Matrix:
    # m x n matrix -- row major, 0 index
    # m(int)
    # n(int)
    # a(list<float>)
    # ia(list<int>)
    # ja(list<int>)
    def __init__(self, m, n, a, ia, ja):
        self.m = m
        self.n = n
        self.a = a
        self.ia = ia
        self.ja = ja

    # Length returns # of nonzero elements
    def __len__(self):
        return len(self.a)

    def __eq__(self, other):
        return isinstance(other, self.__class__) and self.m == other.m and \
            self.n == other.n and self.a == other.a and self.ia == other.ia and \
            self.ja == other.ja

    def __ne__(self, other):
        return not self.__eq__(other)


    def shape(self):
        return (self.m, self.n)

    def transpose(self):
        m = self.n
        n = self.m
        a = []
        ia = [0]
        ja = []
        count = 0
        # seems this could be improved. currently ~ m*n operations
        # seems like it could be done in nnz operations
        for k in range(0, n):
            for l in range(0, m):
                row_start = self.ia[l]
                row_end   = self.ia[l+1]
                ja_sub = self.ja[row_start:row_end]
                # are their values in row? and is this column one of them?
                if row_start == row_end or k not in ja_sub:
                    continue
                a_sub = self.a[row_start:row_end]
                val_idx = ja_sub.index(k)
                a.append(a_sub[val_idx])
                ja.append(l)
                count += 1
            ia.append(count)
        return Matrix(m, n, a, ia, ja)

    # e.g. self * some_other
    def mult_left(self, other):
        print "Not implemented yet."

    # Input vector is a numpy matrix of
    # shape m x 1.
    @staticmethod
    def from_column_vector(vector):
        a = []
        ia = [0]
        ja = []
        m = vector.shape[0]
        idx = 0
        for i in range(0, m):
            val = float(vector[i, 0])
            if numpy.isclose(val, 0):
                ia.append(idx)
                continue
            a.append(val)
            idx += 1
            ia.append(idx)
            ja.append(0)
        return Matrix(m, 1, a, ia, ja)

    # Input vector is a numpy matrix of
    # shape m x 1.
    def push_column(self, vector):
        a = self.a
        ia = self.ia
        ja = self.ja
        m_vector, n_vector = vector.shape
        # raise if m_vector != self.m and n_vector == 1
        added = 0
        for i in range(0, self.m):
            val = float(vector[i, 0])
            if numpy.isclose(val, 0):
                ia[i+1] += added
                continue
            a.insert(ia[i+1]+added, val)
            ja.insert(ia[i+1]+added, self.n)
            added += 1
            ia[i+1] += added
        self.n += 1
        return self

    @staticmethod
    def from_mm_file(filepath):
        m = n = nnz = 0
        a = []
        ja = []
        ia = [0]
        file_handle = open(filepath, 'r')
        parameters = file_handle.readline().rstrip().split(' ')
        # Filter initial comments, docs
        while True:
            line = file_handle.readline()
            if line[0] != '%':
                break
        m, n, nnz = [int(s) for s in line.rstrip().split(' ')]
        entries = []
        # make tuples, sort by row, then col
        while True:
            i = 0
            j = 0
            v = 0.0
            line = file_handle.readline().rstrip()
            if not line:
                break
            if('pattern' in parameters):
                i, j = [s for s in line.split(' ')]
                v = 1
            else:
                i, j, v = [s for s in line.split(' ')]
            i = int(i) - 1
            j = int(j) - 1
            v = float(v)
            if 'symmetric' in parameters and i != j:
                entries.append((j, i, v))
            entries.append((i, j, v))
        entries.sort()
        nnz = len(entries) # We have to recalculate as we can't predict
                           # from the offset how many entries we'll have as
                           # we populate symmetric entries

        #build up CRS format
        idx = 0
        for i in range(0, m):
            while True and idx < nnz:
                entry = entries[idx]
                if entry[0] != i:
                    ia.append(idx)
                    break
                a.append(entry[2])
                ja.append(entry[1])
                idx += 1
        ia.append(nnz)
        return Matrix(m, n, a, ia, ja)

    def to_mm_file(self, filepath):
        print "Not implemented yet."

    # Vector should come in as numpy matrix
    # e.g. mat * vect
    def mult_left_vector(self, v):
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
