from crsmatrix import Matrix
import numpy

class TestMatrix:

    def test_left_mult(self):
        A = Matrix.tridiagonal(3)
        a_inv = [0.75, 0.5, 0.25, 0.5 , 1., 0.5, 0.25, 0.5, 0.75]
        ia_inv = [0, 3, 6, 9]
        ja_inv = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        a = [1.0, 1.0, 1.0]
        ia = [0, 1, 2, 3]
        ja = [0, 1, 2]
        A_inv = Matrix(3, 3, a_inv, ia_inv, ja_inv)
        I = Matrix(3, 3, a, ia, ja)
        assert A * A_inv == I

    def test_transpose(self):
        m = n = 3
        a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ia = [0, 3, 6, 9]
        ja = [0, 1, 2, 0, 1, 2, 0, 1, 2]
        initial_matrix = Matrix(m, n, a, ia, ja)
        a_trans = [1, 4, 7, 2, 5, 8, 3, 6, 9]
        expected_matrix = Matrix(m, n, a_trans, ia, ja)
        output_matrix = initial_matrix.transpose()
        assert expected_matrix == output_matrix

    def test_from_column_vector(self):
        m = 3
        n = 1
        a = [1, 2, 3]
        ia = [0, 1, 2, 3]
        ja = [0, 0, 0]
        input_vector = numpy.matrix([[1],[2],[3]])
        expected_matrix = Matrix(m, n, a, ia, ja)
        output_matrix = Matrix.from_column_vector(input_vector)
        assert expected_matrix == output_matrix

    def test_push_column(self):
        m = 3
        n = 2
        a = [1, 4, 2, 5, 3, 6]
        ia = [0, 2, 4, 6]
        ja = [0, 1, 0, 1, 0, 1]
        first_vector = numpy.matrix([[1],[2],[3]])
        second_vector = numpy.matrix([[4],[5],[6]])
        expected_matrix = Matrix(m, n, a, ia, ja)
        output_matrix = Matrix.from_column_vector(first_vector)
        output_matrix.push_column(second_vector)
        assert expected_matrix == output_matrix

    def test_push_column_with_zeros(self):
        m = 3
        n = 2
        a = [1, 2, 5, 3]
        ia = [0, 1, 3, 4]
        ja = [0, 0, 1, 0]
        first_vector = numpy.matrix([[1],[2],[3]])
        second_vector = numpy.matrix([[0],[5],[0]])
        expected_matrix = Matrix(m, n, a, ia, ja)
        output_matrix = Matrix.from_column_vector(first_vector)
        output_matrix.push_column(second_vector)
        assert expected_matrix == output_matrix

    def test_from_mm_file(self):
        file_path = './data/ash958.mtx'
        ash958 = Matrix.from_mm_file(file_path)
        assert ash958.shape() == (958, 292)
        assert len(ash958) == 1916

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
