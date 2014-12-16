from sklearn import svm
import numpy as np
X = [[1, 1, 0], [1, 0, 1], [1, 0, -1], [1, -1, 0], [1, 0, 2], [1, 0, -2], [1, -2, 0]]
Y = [-1, -1, -1, 1, 1, 1, 1]

X = np.asarray(X, dtype="float64")
Y = np.asarray(Y, dtype="float64")

clf = svm.libsvm.fit(X, Y, kernel="poly", degree=2 , C=10000000)

print clf[1]
