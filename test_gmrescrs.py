from gmrescrs import Gmres
from crsmatrix import Matrix
import numpy

class TestGmresCrs:

    # def test_gmres_huge(self):
    #     A = Matrix.from_mm_file('data/bcsstk18.mtx')
    #     b = numpy.ones((A.shape()[0], 1))
    #     gmres = Gmres(A, b)
    #     output_vector, error = gmres.solve()
    #     print error
    #     assert error < Gmres.EPSILON

    def test_gmres_symmetric(self):
        A = Matrix.from_mm_file('data/494_bus.mtx')
        b = numpy.ones((A.shape()[0], 1))
        gmres = Gmres(A, b, restart_after=200)
        output_vector, error = gmres.solve()
        print error
        assert error < Gmres.EPSILON

    # def test_gmres_rectangular(self):
    #     A = Matrix.from_mm_file('data/ash958.mtx')
    #     b = numpy.ones((A.shape()[0], 1))
    #     gmres = Gmres(A, b)
    #     output_vector, error = gmres.solve()
    #     assert error < Gmres.EPSILON
