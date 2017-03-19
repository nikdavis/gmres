from numpy import zeros, ones, concatenate
from numpy.linalg import norm, qr

class Gmres:
    ITERATIONS = 10000
    RESTART_AFTER = 100
    EPSILON = 1e-6

    # A(crsmatrix.Matrix) m x n
    # b(numpy.matrix) n x 1
    def __init__(self, A, b):
        self.A = A  # CRS
        self.b = b  # Numpy matrix
        self.m, self.n = A.shape()
        self.x0 = ones((self.n, 1))
        self.total_iterations = 0

    def solve(self):
        A = self.A
        b = self.b
        x = self.x0
        error = 1

        #start iterating
        while error > self.EPSILON and self.iteration <= self.ITERATIONS and \
            self.iteration <= self.n and self.iteration <= self.RESTART_AFTER:

            if(self.iteration == 1):
                P, B, x, r = self.first_iteration(A, b, x)
            else:
                P, B, x, r = self.next_iteration(P, B, x, r, self.iteration)

            error = norm(r)
            print "Iteration " + str(self.iteration)
            print "error: " + str(error)

            if(self.iteration == self.RESTART_AFTER):
                self.iteration = 1
                print "Restarting!"
            else:
                self.iteration += 1
            self.total_iterations += 1

        return x, error # and stuff

    def first_iteration(self, A, b, x0):
        b0 = A.mult_left_vector(x0)
        r0 = b - b0
        r0_norm = error = norm(r0)
        p1 = 1/r0_norm * r0
        b1 = A.mult_left_vector(p1)
        t = float((b1.T * r0) / (b1.T * b1))
        x1 = x0 + t * p1
        r1 = r0 - t * b1 # b - A * x1
        P = p1
        B = b1
        x = x1
        r = r1
        return P, B, x, r

    def next_iteration(self, P, B, x, r, m):
        A = self.A
        #print "iteration: " + str(m)
        beta = [float(p * r) for p in P.T]
        p_squiggly = r
        for b, p in zip(beta, P.T):
            p_squiggly = p_squiggly - b * p.T
        p_norm = 1 / norm(p_squiggly) * p_squiggly
        b = A.mult_left_vector(p_norm)
        P = concatenate((P, p_norm), axis=1)
        B = concatenate((B, b), axis=1)
        # print "B: "
        # print B
        Q, R = qr(B)
        # solve new t by back substitution
        # R * t = Q.T * r
        intermediate = Q.T * r
        # print "R: "
        # print R
        rows, cols = R.shape
        t = zeros((rows, 1))
        for i in range(0, rows):
            row = rows - 1 - i # start from bottom
            col = row
            t_new = intermediate[row, 0]
            for j in range(row + 1, cols):
                t_new = t_new - R[row, j] * t[j, 0]
            t[row, 0] = t_new / R[row, col]
        # print "t: "
        # print t
        x_next = x + P * t
        r_next = r - B * t
        return P, B, x_next, r_next
