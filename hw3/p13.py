from __future__ import division
import numpy as np
from _generate_data import generate_data
from _generate_data import sign

err_box = []
for i in xrange(0, 1000):
    g = generate_data(1000)
    data = np.matrix(g[0])
    target = g[1]
    # w_lin = (data.T * data).getI() * data.T * target
    w_lin = np.dot(np.dot(np.dot(data.T, data).getI(), data.T), target)
    # y_predict = data * w_lin
    y_predict = np.dot(data, w_lin.T)
    y_predict = map(lambda x: sign(x), list(y_predict))
    err = np.array(y_predict) - target
    err_box.append(sum(err != 0) / err.shape[0])

print np.array(err_box).sum()/1000
