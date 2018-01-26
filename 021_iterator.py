#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 用 Iterable 判断是否可迭代对象（其实就是可循环对象）

from collections import Iterable

print(isinstance([], Iterable))
print(isinstance({}, Iterable))
print(isinstance('abc', Iterable))
print(isinstance((x for x in range(10)), Iterable))
print(isinstance(100, Iterable))

print('====')
# 用 Iterator 判断是否为迭代器

from collections import Iterator

print(isinstance([], Iterator))
print(isinstance({}, Iterator))
print(isinstance('abc', Iterator))
print(isinstance(100, Iterator))
print(isinstance((x for x in range(100)), Iterator))

print('====')
# 用 iter() 函数把 Iterable 变成 Iterator
print(isinstance(iter([]), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter('avx'), Iterator))
