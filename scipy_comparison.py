import scipy.io as sio
import numpy as np
from scipy.sparse.linalg import gmres

A = sio.mmread('./data/bcsstk18.mtx')
b = np.ones((A.shape[0], 1))
solution = gmres(A, b)
