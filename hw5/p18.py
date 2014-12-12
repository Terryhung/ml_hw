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

    for i in [0.001, 0.01, 0.1, 1, 10]:
        print ("-----------------------------------------")
        res = svm.libsvm.fit(X, y_0, C=i, kernel="rbf", gamma=100)
        sum_a = np.abs(res[3]).sum()
        print res[4]

        clf = svm.SVC(C=i, kernel="rbf", gamma=100)
        clf.fit(X, y_0)
        y_predict = clf.predict(X_test)
        err = y_predict - y_test
        print sum_a
        print len(clf.support_)
        print sum(err != 0)/err.shape
