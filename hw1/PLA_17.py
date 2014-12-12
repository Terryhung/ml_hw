from __future__ import division
import numpy as np


train_data = []
train_target = []
t_data = []


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def PLA(data, w, update_c):
    error = 1
    while error == 1:
        stop = update_c
        for i in xrange(0, 400):
            arr = data[i][:5]
            target = data[i][5]
            r = sign(np.dot(w, arr))
            if r != target:
                w = w + (1/2)*target*arr
                update_c = update_c + 1
        if stop == update_c:
            error = 0
    return update_c


with open('hw1_15_train.dat', 'r') as f:
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


result_sum = []
for i in xrange(0, 2000):
    r = PLA(np.random.permutation(t_data), np.array([0, 0, 0, 0, 0]), 0)
    result_sum.append(r)

result_sum = np.asarray(result_sum)
print result_sum.sum()/2000
