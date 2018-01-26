# !usr/bin/env/python3
# -*- coding:utf-8 -*-

# filter 过滤器
# 1.1 filter 示例
# 1.1.1 使用filter筛出奇数
print('========1.1.1========')


def is_odd(n):
    return n % 2 == 1


L1 = list(filter(is_odd, range(1, 10)))
print("L1 = ", L1)

# 1.1.2 使用filter剔除空格
print('========1.1.2========')


def not_empty(s):
    return s and s.strip()


L2 = list(filter(not_empty, ['A', '', None, 'C', '']))
print('L2 = ', L2)

# 1.1.3 使用filter求素数
print('========1.1.3========')


def odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n


def not_divisible(n):
    return lambda x: x % n > 0


def primes():
    yield 2
    it = odd_iter()  # 初始序列
    while True:
        n = next(it)  # 返回序列的下一个数
        yield n
        it = filter(not_divisible(n), it)  # 构造新序列


L3 = [2]
m1 = int(input('Please input the maximum number: ',))

for n in primes():
    if n < m1:
        L3.append(n)
    else:
        break

print(L3)

# Exercise.1 使用filter求回数
print('========Exercise.1========')


def iter1():
    n = 0
    while True:
        n = n + 1
        yield n


def not_pal():
    return lambda x: list(str(x)) == list(str(x))[::-1]


def pals():
    yield 0
    it1 = iter1()  # 初始序列
    while True:
        n = next(it1)  # 返回序列的下一个数
        yield n
        it1 = filter(not_pal(), it1)  # 构造新序列


L4 = []
m2 = int(input('Please input the maximum number: ',))

for n in pals():
    if n < m2:
        L4.append(n)
    else:
        break

print(L4)
