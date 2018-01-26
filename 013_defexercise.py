#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import math


def move(x, y, step, angle):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = (100, 100, 60, math.pi / 6)
print(x, y)
