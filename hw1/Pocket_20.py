from __future__ import division
import numpy as np
import random

train_data = []
test_data = []
test_target = []
t_data = []
test_data = []


def sign(x):
    return np.sign(np.sign(x) - 0.5)


def err_rate(w, X, y):
    return (sign(np.dot(X, w)) != y).astype(int).mean()


def Pocket(data, w, update_c):
    tmp_w = np.copy(w)
    pocket_w = np.copy(w)
    update = 0
    data = np.array(data)
    X = data[:, :-1]
    y = data[:, -1]
    while update < 100:
        # ind = np.random.randint(0, 499)

        # if sign(np.dot(X[ind], tmp_w)) != y[ind]:
        #     pick_w = tmp_w + X[ind] * y[ind]

        #     if err_rate(pick_w, X, y) <= err_rate(tmp_w, X, y):
        #         print "I'm updating"
        #         tmp_w = pick_w
        #         update = update + 1

        tmp_result = np.dot(X, tmp_w)

        tmp_result[tmp_result == 0] = -1

        err_inds = np.where(np.sign(tmp_result) != y)[0]

        pick_index = random.randint(0, err_inds.shape[0]-1)
        pick_index = err_inds[pick_index]
        pick_w = tmp_w + X[pick_index] * y[pick_index]

        if err_rate(pick_w, X, y) <= err_rate(tmp_w, X, y):
            pocket_w = pick_w

        tmp_w = pick_w
        print "I'm updating"
        update = update + 1

        # for i in xrange(0, 400):
        #     arr = data[i, :]
        #     target = data[i][5]
        #     r = sign(np.dot(tmp_w, arr))
        #     if r != target:
        #         error_tmp.append(i)

        # pick_index = random.randint(0, len(error_tmp))
        # pick_w = tmp_w + data[pick_index][5]*data[pick_index][:5]
        # error_time = 0
        # for i in xrange(0, 400):
        #     arr = data[i][:5]
        #     target = data[i][5]
        #     r = sign(np.dot(pick_w, arr))
        #     if r != target:
        #         error_time = error_time + 1
        # if error_time <= len(error_tmp):
        #     tmp_w = pick_w
        #     update = update + 1
    return pocket_w


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
    r = Pocket(t_data, np.array([0, 0, 0, 0, 0]), 0)
    result_sum.append(err_rate(r, test_array, test_target))
print np.asarray(result_sum).sum()/2000
