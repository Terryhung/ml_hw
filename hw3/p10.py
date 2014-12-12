from __future__ import division
import numpy as np
from math import exp


def b_uu(u, v):
    return (exp(u) + v*v*(exp(u*v)) + 2)


def b_vv(u, v):
    return (4*exp(2*v) + u*u*(exp(v)) + 4)


def b_uv(u, v):
    return exp(u*v) + u*v*(exp(u*v)) - 2


def bu(u, v):
    return exp(u) + v*exp(u*v) + 2*u - 2*v - 3


def bv(u, v):
    return 2*exp(2*v) + u*exp(u*v) - 2*u + 4*v - 2


def H(u, v):
    return np.matrix([[b_uu(u, v), b_uv(u, v)], [b_uv(u, v), b_vv(u, v)]])


def gd(u, v):
    return np.matrix([bu(u, v), bv(u, v)]).T


def E(u, v):
    return exp(u) + exp(2*v) + exp(u*v) + u*u - 2*u*v + 2*v*v - 3*u - 2*v

point = np.matrix([0, 0]).T

for i in xrange(0, 5):
    point = point - np.dot(H(float(point[0]), float(point[1])).getI(), gd(float(point[0]), float(point[1])))
print point

print E(float(point[0]), float(point[1]))
