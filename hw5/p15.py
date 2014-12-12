from read_file_data import read_data_file
from sklearn import svm
import numpy as np

if __name__ == "__main__":
    filename = "features.train"
    X, y = read_data_file(filename)
    X = np.asarray(X, dtype="float64")
    y = map(lambda x: 0 if x == 0 else float(1), y)
    y = np.asarray(y, dtype="float64")

    clf = svm.SVR(C=0.01, kernel="linear")
    clf.fit(X, y)
    print np.linalg.norm(clf.coef_)
