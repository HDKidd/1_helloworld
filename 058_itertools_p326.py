# !usr/bin/env python3
# -*- coding:utf-8 -*-

"""itertools"""

__author__ = 'HDKidd'

import itertools

# 1 itertools 提供的几个“无限”迭代器：
# 1.1 itertools.count：无限迭代出自然数数列
print('========1.1========')

natuals = itertools.count(1)
# for n in natuals:
    # print(n)


# 1.2 itertools.cycle：无限迭代出序列（字符串也是一种序列）
print('========1.2========')

cs = itertools.cycle('ABC')
# for c in cs:
    # print(c)


# 1.3 itertools.repeat: 把一个元素无限重复下去，如果提供第二个参数就可以限定重复次数
print('========1.3========')

ns = itertools.repeat('A', 10)
for n in ns:
    print(n)


# 2 迭代器操作函数
# 2.1 takewhile(): 根据条件判断来从无限序列中截取有限的序列
print('========2.1========')

natuals2 = itertools.count(1)
ns2 = itertools.takewhile(lambda x: x <= 10, natuals2)
print(list(ns2))


# 2.2 chain(): 把一组迭代对象串联起来，形成一个更大的迭代器
print('========2.2========')

for c in itertools.chain('ABC', 'XYZ'):
    print(c)


# 2.3 groupby(): 把迭代器中相邻的重复元素挑出来放在一起
print('========2.3========')

for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))

for key, group in itertools.groupby('AaaBBbcCAAa', lambda c: c.upper()):
    print(key, list(group))

