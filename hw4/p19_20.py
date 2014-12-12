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



def four_one(train, target):
    data_list = []

    for i in range(0, 5):
        one = train[i*40:i*40+40, :]
        one_t = target[i*40:i*40+40, :]
        four = np.vstack((train[0:i*40, :], train[i*40+40:, :]))
        four_t = np.vstack((target[0:i*40, :], target[i*40+40:, :]))
        data_list.append([(four,four_t), (one, one_t)])
    return data_list

r = read_data(train)
lam_list = map(lambda x: pow(10, x), range(-10, 3))
train_data = r[0]
target_data = r[1]
data_list = four_one(train_data, target_data)

for lam in lam_list:
    # train
    error = []

    for data in data_list:
        w_reg = opt_w(lam, data[0][0], data[0][1])
        err = predict_error(w_reg, data[1][0], data[1][1])
        error.append(err)
    e_v = np.asarray(error).sum()/5
    string = str(lam) + ": E_cv = " + str(e_v)
    print string
