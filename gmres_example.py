from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy
from datetime import datetime

A = Matrix.from_mm_file('data/bcsstk18.mtx')
b = numpy.ones((A.shape()[0], 1))

gmres = Gmres(A, b)
x, error, metadata = gmres.solve()
print error
# times = 3
# durations = []
# for i in range(0, times):
#     gmres = Gmres(A, b, max_iterations=100000, restart_after=75)
#     print "starting"
#     start = datetime.now()
#     output_vector, error, metadata = gmres.solve()
#     end = datetime.now()
#     seconds = (end - start).seconds
#     decimal = float((end - start).microseconds) / 1e6
#     print "ending"
#     durations.append(seconds + decimal)
#
#
# print error
# print "iterations: " + str(metadata[0])
# print "duration: " + str(sum(durations) / times) + " sec"
