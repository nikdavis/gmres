from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy

max_matrix_size = 1000
max_iterations = 500
max_restart = 500

A = Matrix.tridiagonal(max_matrix_size)
b = numpy.ones((A.m, 1))

x, error, metadata = Gmres(A, b, max_iterations=max_iterations, restart_after=max_restart).solve()
error_time_values = []
delta = metadata[1]
dur = metadata[2][1:] # discard the first to match siz of deltas
for i in range(0, metadata[0]-1):
    et = delta[i] / dur[i]
    error_time_values.append(et)

handle = open('generated_data.csv', 'a')
handle.write('matrix_size,iteration_norm,error_delta_normed,duration,error_time\n')
for i in range(0, metadata[0]-1):
    iteration_norm = float(i + 1) / max_matrix_size
    items = [max_matrix_size, iteration_norm, delta[i], dur[i], error_time_values[i]]
    line = ','.join([str(s) for s in items]) + '\n'
    handle.write(line)
