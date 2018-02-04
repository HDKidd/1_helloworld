# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 枚举类 enumerated class

# 1.1 定义常量的方法：大写+整数
print('========1.1========')

JAN = 1
FEB = 2
MAR = 3

# 1.2 定义常量的方法：定义一个枚举类
print('========1.2========')

from enum import Enum

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)  # value 属性是自动付给成员int常量，从1开始计数

# 1.3 自定义的枚举类
print('========1.3========')

from enum import Enum, unique


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)

print(Weekday.Tue)

print(Weekday['Wed'])

print(Weekday.Thu.value)

print(day1 == Weekday.Mon)

print(day1 == Weekday.Tue)

print(Weekday(1))

print(day1 == Weekday(1))

