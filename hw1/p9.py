from __future__ import division
import math


def fac(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1, n+1))


def math_c(n, m):
    return fac(n)/(fac(n-m)*fac(m))


def hof_ineq(N, epsilon):
    return 2*math.exp((-2)*math.pow(epsilon, 2)*N)


print math_c(35, 10)*math.pow(0.1, 10)*math.pow(0.9, 25)
