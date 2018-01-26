#!/usr/bin/env python3
# -*- coding:utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)
    
sum = 0
l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in l1:
    sum = sum + x
    print(sum)
    
l2 = list(range(101))
sum = 0
for x in l2:
    sum = sum + x
print(sum)

sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print(sum)

