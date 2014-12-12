from __future__ import division
from read_file_data import read_data_file
from sklearn import svm
import numpy as np

if __name__ == "__main__":
    filename = "features.train"
    X, y = read_data_file(filename)
    X = np.asarray(X, dtype="float64")
    y_0 = map(lambda x: 0 if x == 0 else float(1), y)
    y_0 = np.asarray(y_0, dtype="float64")

    filename = "features.train"
    X_test, y_test = read_data_file(filename)
    X_test = np.asarray(X_test, dtype="float64")
    y_test = map(lambda x: 0 if x == 0 else float(1), y_test)
    y_test = np.asarray(y_test, dtype="float64")

    for i in [1, 10, 100, 1000, 10000]:
        clf = svm.SVC(C=0.01, kernel="rbf", gamma=i)
        clf.fit(X, y_0)
        y_predict = clf.predict(X_test)
        err = y_predict - y_test
        print sum(err != 0)/err.shape
