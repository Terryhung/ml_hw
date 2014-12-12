from __future__ import division
from read_file_data import read_data_file
from sklearn import svm
import numpy as np

if __name__ == "__main__":
    filename = "features.train"
    X, y = read_data_file(filename)
    X = np.asarray(X, dtype="float64")

    for i in [0, 2, 4, 6, 8]:
        y_0 = map(lambda x: 0 if x == i else float(1), y)
        y_0 = np.asarray(y_0, dtype="float64")
        res = svm.libsvm.fit(X, y_0, C=0.01, kernel="poly", degree=2)
        sum_a = np.abs(res[3]).sum()

        print sum_a
