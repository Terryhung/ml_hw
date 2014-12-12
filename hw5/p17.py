from __future__ import division
from read_file_data import read_data_file
from sklearn import svm
import numpy as np

if __name__ == "__main__":
    filename = "features.train"
    X, y = read_data_file(filename)
    X = np.asarray(X, dtype="float64")

    e_in_box = []
    for i in [0, 2, 4, 6, 8]:
        y_0 = map(lambda x: 0 if x == i else float(1), y)
        y_0 = np.asarray(y_0, dtype="float64")
        clf = svm.SVC(C=0.01, kernel="poly", degree=2)
        clf.fit(X, y_0)
        y_predict = clf.predict(X)
        err = y_predict - y_0
        e_in_box.append(sum(err != 0)/err.shape[0])
    print e_in_box
    print min(e_in_box)
