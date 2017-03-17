from crsmatrix import Matrix

class TestMatrix:

    def test_tridiagonal_generation(self):
        m = 10
        a = Matrix.tridiagonal(m)
        assert len(a) == (3 * m - 2)
        assert a.shape() == (m, m)
