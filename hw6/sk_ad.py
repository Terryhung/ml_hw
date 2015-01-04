from __future__ import division
import numpy as np
from sklearn import ensemble

train_file = 'hw6_train.dat'
test_file = 'hw6_test.dat'


def read_data_file(filename):
    X = []
    y = []
    with open(filename, 'r') as f:
        for line in f:
            data = map(lambda x: float(x),
                       filter(None,
                              line.strip().split(' ')))
            X.append(data[:-1])
            y.append(data[-1])
    return np.asarray(X), np.asarray(y)


X_train, y_train = read_data_file(train_file)
X_test, y_test = read_data_file(test_file)

clf = ensemble.AdaBoostClassifier(n_estimators=300, algorithm='SAMME')

clf.fit(X_train, y_train)

for score in clf.staged_score(X_train, y_train):
    print 1 - score

for score in clf.staged_score(X_test, y_test):
    print 1 - score

# y_predict = clf.predict(X_test)
# y_predict = clf.predict(X_test)

# print sum(y_predict != y_test)/y_test.shape
# print sum(y_predict != y_test)/y_test.shape
