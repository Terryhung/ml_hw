from __future__ import division
import numpy as np
from math import sqrt
from math import log
train_file = 'hw6_train.dat'
test_file = 'hw6_test.dat'

def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def generate_theta(data):
    theta_list = []
    my_data = sorted(data)
    for i in xrange(0, 99):
        theta_list.append((my_data[i] + my_data[i+1])/2)
    return theta_list


def h(x, theta, s):
    return s * sign(x - theta)


def decision_stump(data, i):
    err = []
    S_list = [-1, 1]
    theta_list = generate_theta(data)
    theta_list.append(data.max() + 0.001)
    theta_list.append(data.min() - 0.001)
    for s in S_list:
        for theta in theta_list:
            one_error = 0
            x_list = np.asarray(map(lambda x: h(x, theta, s), data))
            for index, value in enumerate(x_list):
                if value != y_train[index]:
                    one_error = one_error + u[index]
            if one_error < 1e-30:
                break
            magic_err = sqrt((1-one_error)/one_error)
            alpha = log(magic_err)
            err.append([one_error, theta, s, i, alpha, magic_err])
    err.sort()
    return err[0]


def update_u(data, theta, s, magic_err):
    x_list = np.asarray(map(lambda x: h(x, theta, s), data))
    for index, value in enumerate(x_list):
        if value != y_train[index]:
            u[index] = u[index]*magic_err
        else:
            u[index] = u[index]/magic_err


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
    return X, y


X_train, y_train = read_data_file(train_file)
X_train = np.asarray(X_train)
u = np.ones(100)/100

count = 0

# [theta, s, i, alpha]
H = []

# [one_error, theta, s, i, alpha, magic_err]
while count != 300:
    print u.sum()
    Err = []
    for i in range(0, 2):
        DATA = X_train[:, i]
        Err.append(decision_stump(DATA, i))

    Err.sort()
    DATA = X_train[:, Err[0][3]]
    print Err[0]
    H.append([Err[0][1], Err[0][2], Err[0][3], Err[0][4]])
    update_u(DATA, Err[0][1], Err[0][2], Err[0][-1])
    count = count + 1
