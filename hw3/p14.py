from __future__ import division
import numpy as np
from _generate_data_t import generate_data
from _generate_data_t import sign


def a(x, y):
    return sign(-1 - 0.05*x + 0.08*y + 0.13*x*y + 1.5*x*x + 1.5*y*y)


def b(x, y):
    return sign(-1 - 0.05*x + 0.08*y + 0.13*x*y + 1.5*x*x + 15*y*y)


def c(x, y):
    return sign(-1 - 0.05*x + 0.08*y + 0.13*x*y + 15*x*x + 1.5*y*y)


def d(x, y):
    return sign(-1 - 1.5*x + 0.08*y + 0.13*x*y + 0.05*x*x + 0.05*y*y)


def e(x, y):
    return sign(-1 - 1.5*x + 0.08*y + 0.13*x*y + 0.05*x*x + 1.5*y*y)

g = generate_data(1000)
data = np.matrix(g[0])
target = g[1]
w_lin = np.dot(np.dot(np.dot(data.T, data).getI(), data.T), target)

g = generate_data(100)
data = g[0]
target = g[1]

a_box = 0
b_box = 0
c_box = 0
d_box = 0
e_box = 0
for index, value in enumerate(data):
    t = target[index]
    if a(value[1], value[2]) != t:
        a_box = a_box + 1
    if b(value[1], value[2]) != t:
        b_box = b_box + 1
    if c(value[1], value[2]) != t:
        c_box = c_box + 1
    if d(value[1], value[2]) != t:
        d_box = d_box + 1
    if e(value[1], value[2]) != t:
        e_box = e_box + 1

y_predict = np.dot(data, w_lin.T)
y_predict = map(lambda x: sign(x), list(y_predict))
err = np.array(y_predict) - target
print ('a: %d' %a_box)
print ('b: %d' %b_box)
print ('c: %d' %c_box)
print ('d: %d' %d_box)
print ('e: %d' %e_box)
print ('my: %d' %sum(err != 0))
