from __future__ import division
from random import uniform
from random import randint


def generate_data(size):
    data = []
    target = []
    for i in xrange(0, size):
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        data.append([1, x, y])
        target.append(target_function(x, y))
    return data, target


def sign(x):
    if x > 0:
        return 1
    else:
        return -1


def target_function(x, y):
    k = randint(1, 10)
    if k == 3:
        return -sign(x*x + y*y - 0.6)
    else:
        return sign(x*x + y*y - 0.6)
