from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy

max_matrix_size = 1000
max_iterations = 500
max_restart = 500

A = Matrix.tridiagonal(max_matrix_size)
b = numpy.ones((A.m, 1))

x, error = Gmres(A, b, max_iterations=max_iterations, restart_after=max_restart).solve()
