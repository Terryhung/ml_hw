from __future__ import division
import numpy as np


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



def E_in(w, X, y):
    y_predict = np.asarray(map(lambda x: sign(x), list(np.dot(X, w)))).reshape(y.shape)
    err = y_predict - y
    print sum(err != 0)/err.shape[0]

def predict_error(w, X, y):
    y_predict = np.asarray(map(lambda x: sign(x), list(np.dot(X, w)))).reshape(y.shape)
    err = y_predict - y
    print sum(err != 0)/err.shape[0]

# train
r = read_data(train)
train_data = r[0]
target_data = r[1]
w_reg = opt_w(10, train_data, target_data)
predict_error(w_reg, train_data, target_data)
# test
r = read_data(test)

test_data = r[0]
score_data = r[1]

predict_error(w_reg, test_data, score_data)
