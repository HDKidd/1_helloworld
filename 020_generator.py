#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 使用 () 将列表生成式改为生成器
L1 = [x * x for x in range(10)]
print(L1)
g1 = (x * x for x in range(10))
print(next(g1))
print(next(g1))

# 对generator 进行迭代
g1 = (x * x for x in range(10))
for n in g1:
    print(n)


# 使用函数输出启波那契数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'Done'


print(fib(6))


# generator function 示例

def odd():
    print('step 1')
    yield (1)
    print('step 2')
    yield (3)
    print('step 3')
    yield (5)


o = odd()
print(next(o))
print(next(o))
print(next(o))


# 使用 yeild 将函数改为生成式

def fibg(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield (b)
        a, b = b, a + b
        n = n + 1
    return 'Done'


for n in fibg(6):
    print(n)


# exer: 使用generator输出杨辉三角

def yhtri(level):
    L = [1]
    while True:
        yield (L)
        L = [L[x] + L[x + 1] for x in range(len(L) - 1)]
        L.insert(0, 1)
        L.append(1)
        if len(L) > 10:
            break
    return 'Done'


yh = yhtri(9)
for n in yh:
    print(n)
