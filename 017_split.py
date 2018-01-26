#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 利用循环语句构造列表
'''
L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)


#笨方法取列表前三元素

L1 = ['Michael','Sarah','Tracy','Bob','Jack']
L2 = [L1[0],L1[1],L1[2]]
print(L2)

#利用循环取列表前N元素

L3 = []
n = 3
for i in range(n):
    L3.append(L1[i]) 
print(L3)

#利用切片获取列表元素
L4 = L1[0:3]
print(L4)

L4 = L1[:3]
print(L4)

L4 = L1[-5:-2]
print(L4)
'''

# 对list,tuple,string使用切片
L = list(range(100))
L1 = L[:10]
L2 = L[10:20]
L3 = L[-10:]
L4 = L[:10:2]
L5 = L[::5]
L6 = L[:]

T = list(range(5))
T1 = T[:3]
T2 = T[::5]

s = 'abcdefgh'
s1 = s[:3]
s2 = s[::4]

print(L1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(L2)  # [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(L3)  # [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
print(L4)  # [0, 2, 4, 6, 8]
print(L6)  # 原列表
print(T1)  # [0, 1, 2]
print(T2)  # [0, 5]
print(s1)  # abc
print(s2)  # ae
