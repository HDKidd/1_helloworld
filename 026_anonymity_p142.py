# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 匿名函数
# 1.匿名函数 lambda
# 1.1 lambda 例子
print('========1.1========')

L1 = list(map(lambda x: x*x, list(range(1, 10))))
print(L1)

# 1.2 lambda 函数也可以利用变量来调用
print('========1.2========')
f = lambda x: x*x
print(f(5))

# 1.3 lambda 函数也可以利用变量来返回
print('========1.3========')


def build(x, y):
    return lambda: x*x+y*y


print(build(2, 5))
g = build(2, 5)
print(g())


