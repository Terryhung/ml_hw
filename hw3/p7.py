from __future__ import division
from math import exp


def E(u, v):
    print exp(u) + exp(2*v) + exp(u*v) + u*u - 2*u*v + 2*v*v - 3*u - 2*v


def gd(u, v):
    x = exp(u) + v*exp(u*v) + 2*u - 2*v - 3
    y = 2*exp(2*v) + u*exp(u*v) - 2*u - 2 + 4*v
    return (x, y)

n = 0.01
point = [0, 0]

for i in xrange(0, 5):
    point[0] = point[0] - n*gd(point[0], point[1])[0]
    point[1] = point[1] - n*gd(point[0], point[1])[1]

print point[0]
print point[1]
E(point[0], point[1])
E(0, 0)
