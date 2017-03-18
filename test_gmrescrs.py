from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy

class TestGmresCrs:

    def test_initialize(self):
        A = Matrix.from_mm_file('data/494_bus.mtx')
        m, n = A.shape()
        b = numpy.ones((m, 1))
        gmres = Gmres(A, b)
        output_vector, error = gmres.solve()
        print error
        assert error < Gmres.EPSILON
