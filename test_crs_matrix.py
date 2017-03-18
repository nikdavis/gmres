from crsmatrix import Matrix
import numpy

class TestMatrix:

    def test_tridiagonal_generation(self):
        m = 3
        a = Matrix.tridiagonal(m)
        assert len(a.ia) == m + 1
        assert len(a) == 3 * m - 2
        assert a.shape() == (m, m)
        assert a.a  == [2, -1, -1, 2, -1, -1, 2]
        assert a.ia == [0, 2, 5, 7]
        assert a.ja == [0, 1, 0, 1, 2, 1, 2]

    def test_mult_vect_right(self):
        input_vector    = numpy.matrix([1,1,1,1,1]).T
        expected_vector = numpy.matrix([1,0,0,0,1]).T
        test_matrix     = Matrix.tridiagonal(5)
        output_vector   = test_matrix.mult_vect_right(input_vector)
        assert (expected_vector == output_vector).all()
