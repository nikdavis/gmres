from crsmatrix import Matrix
import numpy

class TestMatrix:

    # def test_transpose(self):
    #     m = n = 3
    #     a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    #     ia = [0, 3, 6, 9]
    #     ja = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    #     initial_matrix = Matrix(m, n, a, ia, ja)
    #     a_trans = [1, 4, 7, 2, 5, 8, 3, 6, 9]
    #     expected_matrix = Matrix(m, n, a_trans, ia, ja)
    #     output_matrix = initial_matrix.transpose()
    #     assert input_matrix == output_matrix

    def test_tridiagonal_generation(self):
        m = 3
        a = Matrix.tridiagonal(m)
        assert len(a.ia) == m + 1
        assert len(a) == 3 * m - 2
        assert a.shape() == (m, m)
        assert a.a  == [2, -1, -1, 2, -1, -1, 2]
        assert a.ia == [0, 2, 5, 7]
        assert a.ja == [0, 1, 0, 1, 2, 1, 2]

    def test_eq_and_ne(self):
        m = 3
        m1 = Matrix.tridiagonal(m)
        a = [2, -1, -1, 2, -1, -1, 2]
        ia = [0, 2, 5, 7]
        ja = [0, 1, 0, 1, 2, 1, 2]
        m2 = Matrix(m, m, a, ia, ja)
        assert m1 == m2
        a = [1, 1, 1, 1, 1, 1, 1]
        m3 = Matrix(m, m, a, ia, ja)
        assert m2 != m3

    def test_mult_vect_right(self):
        input_vector    = numpy.matrix([1,1,1,1,1]).T
        expected_vector = numpy.matrix([1,0,0,0,1]).T
        test_matrix     = Matrix.tridiagonal(5)
        output_vector   = test_matrix.mult_left_vector(input_vector)
        assert (expected_vector == output_vector).all()
