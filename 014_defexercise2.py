#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math


def root(a, b, c):
    # if not isinstance(a,(int,float)):
    # raise TypeError('bad operand type')
    # if not isinstance(b,(int,float)):
    # raise TypeError('bad operand type')
    # if not isinstance(c,(int,float)):
    # raise TypeError('bad operand type')
    if (b ** 2 - 4 * a * c) < 0:
        return 'no root'
    else:
        x1 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        x2 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return float("{0:.2f}".format(x1)), float("{0:.2f}".format(x2))
        # return x1,x2


a = float(input('Please input \'a\':'))
b = float(input('Please input \'b\':'))
c = float(input('Please input \'c\':'))

print(root(a, b, c))
