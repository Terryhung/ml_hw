from __future__ import division
import numpy as np
import random

train_data = []
test_data = []
test_target = []
t_data = []
test_data = []


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def PLA(data, w, update_c):
    while 50 == update_c:
        for i in xrange(0, 400):
            arr = data[i][:5]
            target = data[i][5]
            r = sign(np.dot(w, arr))
            if r != target:
                w = w + (1/2)*target*arr
                update_c = update_c + 1
    return w

with open('hw1_18_train.dat', 'r') as f:
    for data in f:
        data_split = data.strip().split('\t')
        data_t = data_split[0].split(' ')
        data_t.append(1)
        data_t.append(int(data_split[1]))
        tmp = []
        for i in data_t:
            tmp.append(float(i))
        train_data.append(tmp)

for i in train_data:
    t_data.append(np.asarray(i))

with open('hw1_18_test.dat', 'r') as f:
    for data in f:
        data_split = data.strip().split('\t')
        data_t = data_split[0].split(' ')
        data_t.append(1)
        tmp = []
        for i in data_t:
            tmp.append(float(i))
        test_data.append(tmp)
        test_target.append(int(data_split[1]))

test_array = np.append(test_data, [[0,0,0,0,0]], axis=0)
test_target.append(-1)
test_target = np.asarray(test_target)
result_sum = []

for i in xrange(0, 2000):
    r = PLA(np.random.permutation(t_data), np.array([0, 0, 0, 0, 0]), 0)
    p = np.asarray(r).reshape(-1, 1)
    test_result = np.dot(test_array, p)
    test_result = np.asarray(map(lambda x: sign(x), list(test_result)))
    e = test_target - test_result
    e = sum(e!=0)/501
    result_sum.append(e)
print round(np.asarray(result_sum).sum()/2000, 2)
