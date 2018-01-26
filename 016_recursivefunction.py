#!\usr\bin\env python3
# -*- coding:utf-8 -*-

# 递归函数

# 利用递归函数实现阶乘

'''
def fact(n):
    if n == 1:
        return 1
    return n*fact(n-1)
    
print(fact(1))

print(fact(5))

print(fact(100))

#用尾递归实现阶乘

def fact(n):
    return fact_iter(n,1)
    
def fact_iter(num,product):
    if num == 1:
        return product
    return fact_iter(num - 1,num * product)

print(fact(6))
'''

# 利用递归函数求出河内塔解法


def solve(n, a, b, c):
    if n == 1:
        print('move', a, 'to', c)
    else:
        solve(n-1, a, c, b)
        solve(1, a, b, c)
        solve(n-1, b, a, c)
    return 'Finish!'


n = int(input('Please input the initial level of pillar \'A\':'))

print(solve(n, 'A', 'B', 'C'))
