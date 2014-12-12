from __future__ import division
import random
import numpy as np


Err = []


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def dataset():
    Data = []
    for times in xrange(0, 20):
        x = random.uniform(-1, 1)
        filps = random.randint(0, 4)
        if filps == 3:
            y = -sign(x)
        else:
            y = sign(x)
        tmp_array = [x, y]
        Data.append(tmp_array)
    Data.sort()
    Data = np.asarray(Data)
    return Data


def generate_theta(data):
    theta_list = []
    column_1 = data[:, 0]
    for i in xrange(0, 10):
        theta_list.append((column_1[i] + column_1[i-1])/2)
    return theta_list


def h(x, theta, s):
    return s * sign(x - theta)


def E_out(theta, s):
    return 0.5 + 0.3 * s * (abs(theta) - 1)


def decision_stump(data):
    err = []
    S_list = [-1, 1]
    theta_list = generate_theta(data)
    theta_list.append(data.max() + 0.001)
    theta_list.append(data.min() - 0.001)
    for s in S_list:
        for theta in theta_list:
            x_list = np.asarray(map(lambda x: h(x, theta, s), data[:, 0]))
            err.append([sum(x_list != data[:, 1])/20, E_out(theta, s)])
    return np.amin(err, axis=0)

for times in xrange(0, 5000):
    DATA = np.asarray(dataset())
    Err.append(decision_stump(DATA))
print "Problem 17: " + str(np.asarray(Err)[:, 0].sum()/5000)
print "Problem 18: " + str(np.asarray(Err)[:, 1].sum()/5000)
