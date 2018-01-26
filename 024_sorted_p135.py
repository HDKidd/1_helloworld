# !usr/bin/env python3
# -*- coding:utf-8 -*-

# sorted 算法
# 1.1 sorted 示例
# 1.1.1.1 sorted 对 list 排序
print('========1.1.1.1========')

L1 = [36, 5, -12, 9, -21]
L2 = sorted(L1)
print('L2= ', L2)

# 1.1.1.2 接收 key函数 对 list 实现自定义排序
print('========1.1.1.2========')

L3 = sorted(L1, key=abs)
print('L3= ', L3)

# 1.1.2.1 sorted 对 string 排序
print('========1.1.2.1========')

L4 = ['bob', 'about', 'Zoo', 'Credit']
L5 = sorted(L4)
print('L5= ', L5)

# 1.1.2.2 接收 key函数 对 string 实现不区分大小写排序
print('========1.1.2.2========')
L6 = sorted(L4, key=str.lower)
print('L6= ', L6)


# sorted 算法
# Exercise.1.1 对一组tuple按照学生名字排序
print('========Exercise.1========')


def keysindict(t1):
    return t1[0].lower()


L7 = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L8 = sorted(L7, key=keysindict)
print('L8= ', L8)

# Exercise.1.2 对一组tuple按照成绩排序，由高到低
print('========Exercise.2========')


def itemsindict(t2):
    return t2[1]


L9 = sorted(L7, key=itemsindict, reverse=True)
print('L9= ', L9)
