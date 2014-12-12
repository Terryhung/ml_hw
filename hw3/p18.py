from __future__ import division
from math import exp
import numpy as np

import warnings

warnings.filterwarnings('error')


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def logistic_func(s):
    return 1/(1+np.exp(-s))


def readfile(filename):
    train_data = []
    target_data = []
    with open(filename, 'r') as f:
        for data in f:
            data_split = data.strip().split('\t')
            data_t = data_split[0].split(' ')
            tmp = []
            for i in data_t:
                tmp.append(float(i))
            train_data.append(tmp[:-1])
            target_data.append(tmp[-1])
            l = len(tmp[:-1])
    return np.matrix(train_data), np.asarray(target_data), l


def gd(y, w, x):
    logis_term = logistic_func(np.multiply(-y, np.dot(x, w.T)))
    e_in = np.mean(np.multiply(np.multiply(logis_term, -y), x), axis = 0)
    # e_in = e_in/np.linalg.norm(e_in)
    return w - 0.001*e_in

data = readfile('hw3_train.dat')
x = data[0]
y = data[1].reshape(1000, 1)
w = np.zeros(data[2]).reshape(1, 20)
gd(y, w, x)
for i in xrange(0, 2000):
    w = gd(y, w, x)

data = readfile('hw3_test.dat')
x = data[0]
y = data[1].reshape(3000, 1)
y_predict = np.dot(x, w.T)
y_predict = map(lambda x: sign(x), list(y_predict))
err = y - np.asarray(y_predict).reshape(3000, 1)
print sum(err != 0)/err.shape[0]
