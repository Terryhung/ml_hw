from cvxopt import matrix, solvers
import numpy as np
X = [[-1, -1, 0], [-1, 0, -1], [-1, 0, 1], [1, -1, 0], [1, 0, 2], [1, 0, -2], [1, -2, 0]]
Y = [-1, -1, -1, 1, 1, 1, 1]

Q = matrix([[0, 0, 0, 0, 0, 0, 0, 0],
     [0, 1, 0, 0, 0, 0, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0],
     [0, 0, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 0, 1, 0, 0, 0],
     [0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 1, 0],
     [0, 0, 0, 0, 0, 0, 0, 1]])

q = matrix([0, 0, 0, 0, 0, 0, 0, 0])

A = np.array(X)
c = 1

sol=solvers.qp(Q, q, matrix(A), c)
