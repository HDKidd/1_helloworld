#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# dict 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)

for value in d.values():
    print(value)

for k, v in d.items():
    print(k, v)

# string 迭代
s = 'ABCD'
for ch in s:
    print(ch)

# 判断数据类型是否可迭代
from collections import Iterable

print(isinstance('abc', Iterable))
print(isinstance(123, Iterable))

# 枚举迭代 enunmerate 函数（枚举函数）
L = ['A', 'B', 'C']
for i, value in enumerate(L):
    print(i, value)

# 多变量迭代
L = [(1, 2, 3), (2, 3, 4), (3, 4, 5), (4, 5, 6)]
for a, b, c in L:
    print(a, b, c)
