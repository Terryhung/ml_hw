from __future__ import division
from read_file_data import read_data_file
from sklearn import svm
from sklearn import cross_validation
import numpy as np

if __name__ == "__main__":
    filename = "features.train"
    X, y = read_data_file(filename)
    X = np.asarray(X, dtype="float64")
    y_0 = map(lambda x: 0 if x == 0 else float(1), y)
    y_0 = np.asarray(y_0, dtype="float64")

    box = {}
    box[0] = 0
    box[1] = 0
    box[2] = 0
    box[3] = 0
    box[4] = 0
    for j in range(100):
        X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y_0, test_size=0.2, random_state=j)
        err_box = []
        for i in [1, 10, 100, 1000, 10000]:
            clf = svm.SVC(C=0.1, kernel="rbf", gamma=i)
            clf.fit(X_train, y_train)
            y_predict = clf.predict(X_test)
            err = y_predict - y_test
            print sum(err != 0)/err.shape[0]
            err_box.append(sum(err != 0)/err.shape[0])
        box[err_box.index(min(err_box))] = box[err_box.index(min(err_box))] + 1
        print box

    print box
