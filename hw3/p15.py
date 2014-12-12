from __future__ import division
import numpy as np
from _generate_data_t import generate_data
from _generate_data_t import sign

g = generate_data(1000)
data = np.matrix(g[0])
target = g[1]
w_lin = np.dot(np.dot(np.dot(data.T, data).getI(), data.T), target)

g = generate_data(1000)
data = np.matrix(g[0])
target = g[1]
y_predict = np.dot(data, w_lin.T)
y_predict = map(lambda x: sign(x), list(y_predict))
err = np.array(y_predict) - target

print sum(err != 0)/err.shape[0]
