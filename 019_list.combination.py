#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 生成一维list
L1 = list(range(1, 11))
print(L1)

# 列表生成式
L2 = [x * x for x in range(1, 11)]
print(L2)

L3 = [3 ** n for n in range(1, 11)]
print(L3)

L4 = [x * x for x in range(1, 11) if x % 2 == 0]
print(L4)

L5 = [3 ** n for n in range(1, 11) if n % 5 == 0]
print(L5)

# 双循环（多循环）生成全组合
L6 = [m + n for m in 'ABCDEF' for n in 'ABCDEF']
print(L6)

# 双循环（多循环）生成全排列
L8 = [m + n for m in 'ABC' for n in 'DEF']
print(L8)

# 列出当前目录下的所有文件和目录名
import os  # 导入os模块

L9 = [d for d in os.listdir('.')]  # os.listdir 为列出文件和目录
print(L9)

# 双变量生成list
D1 = {'x': 'A', 'y': 'B', 'z': 'C'}
L10 = [k + '=' + v for k, v in D1.items()]
print(L10)

# 改变list中元素的属性
L11 = ['Hello', 'World', 'IBM', 'Apple']
L12 = [l.lower() for l in L11]  # 全部小写
L13 = [u.upper() for u in L12]
L14 = [c.capitalize() for c in L12]  # 首字母大写

print(L11)
print(L12)
print(L13)
print(L14)

# 作业：对数据类型复杂的list生成新list:挑出其中的str并小写化

L1 = ['Hello', 'World', 19, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s, str) == True]
print(L2)
