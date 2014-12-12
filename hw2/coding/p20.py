from __future__ import division
import random
import numpy as np

train_data = []
Err = []
def sign(x):
    if x > 0:
        return 1
    else:
        return -1



def generate_theta(data):
    theta_list = []
    for i in xrange(0, 99):
        theta_list.append((data[i] + data[i+1])/2)
    return theta_list


def h(x, theta, s):
    return s * sign(x - theta)


def E_out(theta, s):
    return 0.5 + 0.3 * s * (abs(theta) - 1)


def decision_stump(data, i):
    err = []
    S_list = [-1, 1]
    theta_list = generate_theta(data)
    theta_list.append(data.max() + 0.001)
    theta_list.append(data.min() - 0.001)
    for s in S_list:
        for theta in theta_list:
            x_list = np.asarray(map(lambda x: h(x, theta, s), data))
            err.append([sum(x_list != target_data)/100, theta, s, i])
    return np.amin(err, axis=0)

with open('hw2_test.dat', 'r') as f:
    for data in f:
        data_split = data.strip().split('\t')
        data_t = data_split[0].split(' ')
        tmp = []
        for i in data_t:
            tmp.append(float(i))
        train_data.append(tmp)

train_data = np.asarray(train_data)
target_data = train_data[:, 9]


result = np.asarray(map(lambda x: h(x, 1.78, -1), train_data[:, 3]))
print sum(result != target_data)/1000
