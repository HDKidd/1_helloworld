# !usr/bin/env python3
# -*- coding:utf-8 -*-

import functools

# 偏函数 partial function
# 1.1 偏函数示例：int
print('========1.1========')

print(int('12345'))    # int函数将字符串转化为整数

print(int('12345', base=8))    # int函数还提供额外的base参数，默认值为10，可以做进制转化(N进制转为10)

print(int('12345', 16))    # 使用int函数进行16进制转换


def int2(x, base=2):    # 定义一个base参数固定为2的函数用于二进制转换
    return int(x, base)


print(int2('1010111001'))

int3 = functools.partial(int, base=2)    # 使用偏函数来改变参数默认值

print(int3('1011000101'))

print(int3('1100', base=10))    # 偏函数仅仅是改变参数默认值，该参数值还是可以重新定义的


