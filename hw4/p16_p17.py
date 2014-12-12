from __future__ import division
import numpy as np
from math import pow

train = 'hw4_train.dat'
test = 'hw4_test.dat'


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def read_data(filename):
    train = []
    target = []
    with open(filename, 'r') as f:
        for data in f:
            data_split = data.strip().split('\t')
            data_t = [1]
            data_t = data_t + data_split[0].split(' ')
            tmp = []
            for i in data_t:
                tmp.append(float(i))
            train.append(tmp[:3])
            target.append(tmp[3])

    train = np.matrix(train)
    target = np.matrix(target).T
    return (train, target)


def opt_w(lam, X, y):
    w_reg = np.dot((np.dot(X.T, X) + lam*np.identity(X.shape[1])).getI(), np.dot(X.T, y))
    return w_reg



def predict_error(w, X, y):
    y_predict = np.asarray(map(lambda x: sign(x), list(np.dot(X, w)))).reshape(y.shape)
    err = y_predict - y
    return float(sum(err != 0)/err.shape[0])


r = read_data(train)
t = read_data(test)
lam_list = map(lambda x: pow(10, x), range(-10, 3))

for lam in lam_list:
    # train
    train_data = r[0][:120, :]
    target_data = r[1][:120, :]
    # valid
    train_data_v = r[0][120:, :]
    target_data_v = r[1][120:, :]
    # test
    test_data = t[0]
    score_data = t[1]

    w_reg = opt_w(lam, train_data, target_data)
    e_in = predict_error(w_reg, train_data, target_data)
    e_v = predict_error(w_reg, train_data_v, target_data_v)
    e_out = predict_error(w_reg, test_data, score_data)
    string = str(lam) + " : Ein = " + str(e_in) + " Ev = "+ str(e_v) + " Eout = " + str(e_out)
    print string
