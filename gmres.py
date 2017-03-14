from numpy import *
from numpy.linalg import *

A = matrix([
    [ 2, -1,  0,  0,  0,  0,  0],
    [-1,  2, -1,  0,  0,  0,  0],
    [ 0, -1,  2, -1,  0,  0,  0],
    [ 0,  0, -1,  2, -1,  0,  0],
    [ 0,  0,  0, -1,  2, -1,  0],
    [ 0,  0,  0,  0, -1,  2, -1],
    [ 0,  0,  0,  0,  0, -1,  2]
])

b = matrix([
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ]
])

x0 = matrix([
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ],
    [ 1 ]
])



def next_iteration(P, B, x, r, m):
    print "iteration: " + str(m)
    beta = [float(p * r) for p in P.T]
    p_squiggly = r
    for b, p in zip(beta, P.T):
        p_squiggly = p_squiggly - b * p.T
    p_norm = 1 / norm(p_squiggly) * p_squiggly
    b = A * p_norm
    P = concatenate((P, p_norm), axis=1)
    B = concatenate((B, b), axis=1)
    Q, R = qr(B)
    # solve new t by back substitution
    # R * t = Q.T * r
    intermediate = Q.T * r
    print R
    rows, cols = R.shape
    t = zeros((rows, 1))
    for i in range(0, rows):
        row = rows - 1 - i # start from bottom
        col = row
        t_new = intermediate[row, 0]
        for j in range(row + 1, cols):
            t_new = t_new - R[row, j] * t[j, 0]
        t[row, 0] = t_new / R[row, col]
    print t
    x_next = x + P * t
    r_next = r - B * t
    return P, B, x_next, r_next

m = 1
limit = 100
# unused right now
restart = 15
tolerance = 1e-6

# Iteration m = 1
b0 = A * x0
r0 = b - b0
p1 = 1/norm(r0) * r0
b1 = A * p1

t = float((b1.T * r0) / (b1.T * b1))
x1 = x0 + t * p1
r1 = r0 - t * b1 # b - A * x1

# Iteration m = 2
m += 1

P = p1
B = b1
x = x1
r = r1

while norm(r) > tolerance and m <= limit:
    P, B, x, r = next_iteration(P, B, x, r, m)
    print "Iteration " + str(m) + ", ||r|| = " + str(norm(r))
    m += 1

x_cheat = inv(A) * b
print isclose(x, x_cheat)

print x_cheat.T
print x.T

# # Iteration m = 3
# beta1 = float(p1.T * r1)
# p2_squiggly = r1 - beta1 * p1
# p2 = 1 / norm(p2_squiggly) * p2_squiggly
# b2 = A * p2
#
# B = concatenate((b1, b2), axis=1)
#
# Q, R = qr(B)
# Q_t = transpose(Q)
# intermediate = Q_t * r1
# t1 = float(intermediate[1] / R[1, 1])
# t0 = float((intermediate[0] - (R[0, 1] * t1)) / R[0, 0])
# t = matrix([t0, t1]).T
# P = concatenate((p1, p2), axis=1)
# #t = dot(inv(R), dot(Q_t, r1))
# print "Q:"
# print Q
# print "R:"
# print R
# print "P:"
# print P
# print "t:"
# print t
# x2 = x1 + P*t
# r2 = r1 - B*t

#
# # Iteration m = 3
# beta1 = dot(transpose(p1), r2)
# beta2 = dot(transpose(p2), r2)
# p3_squiggly = r2 - beta1 * p1 - beta2 * p2
# p3 = 1 / norm(p3_squiggly) * p3_squiggly
# b3 = dot(A, p3)
#
# B = concatenate((b1, b2, b3), axis=1)
#
# Q, R = qr(B)
# Q_t = transpose(Q)
# intermediate = dot(Q_t, r2)
# t2 = intermediate[2] / R[2][2]
# t1 = (intermediate[1] - R[1][2] * t2) / R[1][1]
# t0 = (intermediate[0] - R[0][2] * t2 - R[0][1] * t1) / R[0][0]
# t = array([t0, t1, t2])
# P = concatenate((p1, p2, p3), axis=1)
# x3 = x2 + dot(P, t)
# r3 = r2 - dot(B, t)

#
# print norm(r0)
# print norm(r1)
# print norm(r2)

# print "Ax = b"
# print "x = "
# print inv(A) * b
