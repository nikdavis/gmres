from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy

A = Matrix.from_mm_file('data/ash958.mtx')
# b = numpy.ones((A.shape()[0], 1))
# gmres = Gmres(A, b, max_iterations=10000, restart_after=50)
# output_vector, error = gmres.solve()
# print error
print A.shape()
print len(A)
B = A.transpose()
print B.shape()
print len(B)

B.to_mm_file('data/ash958_transpose.mtx')
