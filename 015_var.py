#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 可变参数*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum


print(calc(1, 5, 35, 7, 1, 2))


# 关键字参数**
def person(name, age, **other):
    print('name:', name, 'age:', age, 'other:', other)


print(person('Michael', 30))

print(person('Bob', 35, city='Beijing'))

print(person('Adam', 45, gender='M', job='Engineer'))

extra = {'city': 'Beijing', 'job': 'Engineer'}

print(person('Jack', 24, **extra))


# 命名关键字参数*，

def person(name, age, *, city, job):
    print(name, age, city, job)


# 参数组合

def f1(a, b, c=0, *args, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'args=', args, 'kw=', kw)


def f2(a, b, c=0, *, d, **kw):
    print('a=', a, 'b=', b, 'c=', c, 'd=', d, 'kw=', kw)


print(f1(1, 2))
print(f1(1, 2, 4))
print(f1(1, 2, c=5))
print(f1(1, 2))
print(f1(1, 2, 3, 'a', 'b'))
print(f1(1, 2, 3, 'a', 'b', x=99, y=100))
print(f2(1, 2, d=97, abs=2))

# use tuple and dict in functions

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}

print(f1(*args, **kw))

args = (1, 2, 3,)
kw = {'d': 88, 'x': '@'}

print(f2(*args, **kw))
