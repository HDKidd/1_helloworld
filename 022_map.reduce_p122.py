#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

# 1. 函数式编程 functional programming
# 1.1 高阶函数
print('========1.1========')


def add(x, y, g):
    return g(x) + g(y)


print(add(-5, 6, abs))

''' # 运行过程如下：
x = -5
y = 6
f = abs
f(x)+f(y)>>>>>> abs(-5)+abs(6)>>>>>11
return 11
'''

# 1.2 map函数（将函数作用到每个元素上）
# 1.2.1 将函数f(x) = x ** 2 作用到list的每个元素上
print('========1.2.1========')


def f(x):
    return x * x


r1 = map(f, list(range(1, 10)))
print('r1=', list(r1))  # print(r) 无法返回结果，因为通过map返回的是一个Iterator惰性序列，无法print

# 1.2.2 将list每个元素转化为字符串
print('========1.2.2========')

r2 = map(str, list(range(1, 10)))
print('r2=', list(r2))

# 1.3 reduce 函数 （将一种计算关系作用到每两个连续元素上）
# 1.3.1 序列求和：将加法作用到list的每两个连续元素上
print('========1.3.1========')


def add(x, y):
    return x + y


r3 = reduce(add, list(range(5)))
print('r3=', r3)  # reduce返回的是一个非Iterator

# 1.3.2 按list元素序列排成一个整数
print('========1.3.2========')


def toint(x, y):
    return x * 10 + y


r4 = reduce(toint, list(range(5)))
print('r4=', r4)

# 1.4 用 map 和 reduce 构造 str to int函数
print('========1.4========')


def str2int(ss):
    def list2int(x, y):
        return x * 10 + y

    def char2num(c):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[c]
    return reduce(list2int, (map(char2num, ss)))


s0 = '127656554'
s1 = str2int(s0)
print('s1=', s1)
print('ins?', isinstance(s1, int))
print('ss*2=', s0 * 2)
print('s1*2=', s1 * 2)

# Exercise.1 利用 map 函数把用户输入的不规范英文变为首字母大写
print('========E.1========')


def normalize(name):
    return name.capitalize()


L1 = ['adam', 'LISA', 'batT']
L2 = list(map(normalize, L1))
print('L2=', L2)

# Exercise.2 利用 reduce 函数编写求积函数
print('========E.2========')


def prod(x, y):
    return x * y


L3 = reduce(prod, list(range(3, 5)))
print('L3 = ', L3)

# Exercise.3 利用 map 和 reduce 函数编写 str2float 函数
print('========E.3========')


def str2float(sss):
    def list2int(x, y):
        return x * 10 + y
    n = sss.index('.')
    sss1 = list(map(int, list(x for x in sss[:n])))
    sss2 = list(map(int, list(x for x in sss[n + 1:])))
    return reduce(list2int, sss1) + reduce(toint, sss2) / (10 ** len(sss2))


s = '123.45476'
print(str2float(s))
