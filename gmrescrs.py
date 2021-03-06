from numpy import zeros, ones, concatenate, matrix
from numpy.linalg import norm, qr
from datetime import datetime

class Gmres:
    MAX_ITERATIONS = 10000
    RESTART_AFTER = 500
    EPSILON = 1e-6

    # A(crsmatrix.Matrix) m x n
    # b(numpy.matrix) n x 1
    def __init__(self, A, b, max_iterations = MAX_ITERATIONS, \
                    epsilon = EPSILON, restart_after = RESTART_AFTER):
        self.A = A  # CRS
        self.b = b  # Numpy matrix
        self.m, self.n = A.shape()
        self.x0 = ones((self.n, 1))
        self.Q = None
        self.R = None
        self.total_iterations = 0
        self.max_iterations = max_iterations
        self.epsilon = epsilon
        self.restart_after = restart_after

    def solve(self):
        A = self.A
        b = self.b
        x = self.x0
        error = 1
        iteration = 1
        errors = []
        error_deltas = []
        durations = []

        #start iterating
        while error > self.epsilon and self.total_iterations < self.max_iterations and \
            iteration <= self.n and iteration <= self.restart_after:
            start = datetime.now()
            if(iteration == 1):
                P, B, x, r = self.first_iteration(A, b, x)
            else:
                P, B, x, r = self.next_iteration(P, B, x, r, iteration)

            error = norm(r)
            end = datetime.now()

            timedelta = end - start
            duration_seconds = float(timedelta.seconds)
            duration_decimal = float(timedelta.microseconds) / 1e6
            durations.append(duration_seconds + duration_decimal)
            errors.append(error)

            print self.total_iterations
            print error

            if(self.total_iterations > 0):
                idx = self.total_iterations
                # find the delta and norm it to the last error
                error_delta = (errors[idx-1] - errors[idx]) / errors[idx-1]
                error_deltas.append(error_delta)

            # print "Iteration " + str(self.total_iterations + 1)
            # print "error: " + str(error)

            if(iteration == self.restart_after):
                iteration = 1
                # print "Restarting!"
            else:
                iteration += 1
            self.total_iterations += 1

        return x, error, [self.total_iterations, error_deltas, durations] # and stuff

    def first_iteration(self, A, b, x0):
        self.Q = None
        self.R = None
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
        # make b orthogonal to all other Bs
        if self.Q is None:
            self.Q, self.R = qr(B)
        else:
            Q = self.Q
            R = self.R
            q_orth = b
            constants = []
            for i in range(0, Q.shape[1]):
                q_sub = Q[:, i]
                #print q_sub
                constant = float(q_sub.T * b)
                constants.append(constant)
                q_orth = q_orth - constant * q_sub
            q_norm = norm(q_orth)
            q_orth = 1 / norm(q_orth) * q_orth
            # print constants
            # print q_orth.T * q_sub
            # print self.Q
            # print self.R
            # print q_orth
            # print matrix(constants).T
            self.Q = concatenate((self.Q, q_orth), axis=1)
            self.R = concatenate((self.R, matrix(constants).T), axis=1)
            Rm = self.R.shape[1]
            # print zeros((1, Rm))
            self.R = concatenate((self.R, zeros((1, Rm))))
            self.R[Rm-1, Rm-1] = q_norm
            # print self.Q
            # print self.R

        #self.Q, self.R = qr(B)
        # solve new t by back substitution
        # R * t = Q.T * r
        intermediate = self.Q.T * r
        # print "R: "
        # print R
        rows, cols = self.R.shape
        t = zeros((rows, 1))
        for i in range(0, rows):
            row = rows - 1 - i # start from bottom
            col = row
            t_new = intermediate[row, 0]
            for j in range(row + 1, cols):
                t_new = t_new - self.R[row, j] * t[j, 0]
            t[row, 0] = t_new / self.R[row, col]
        # print "t: "
        # print t
        x_next = x + P * t
        r_next = r - B * t
        return P, B, x_next, r_next
