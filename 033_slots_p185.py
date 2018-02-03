# !usr/bin/env python3
# -*- coding:utf-8 -*-

# __slots__
# 1.1 实例可以绑定属性和方法
print('========1.1========')


class Student(object):
    pass


s1 = Student()
s1.name = 'Michael'  # 动态给实例s1绑定一个属性name
print(s1.name)


def set_age(self, age):  # 定义一个函数为实例方法
    self.age = age


from types import MethodType

s1.set_age = MethodType(set_age, s1)  # 给实例s1绑定刚才定义的函数作为方法
s1.set_age(25)  # 调用实例方法
print(s1.age)   # 测试结果

s2 = Student()
# print(s2.set_age(25))   # 给s1绑定的方法，对于其他实例是不起作用的


def set_score(self, score):
    self.score = score


Student.set_score = MethodType(set_score, Student)    # 给类绑定方法

s1.set_score(100)
print(s1.score)

s2.set_score(99)
print(s2.score)


# 2.1 使用__slots__限制实例的可以添加的属性
print('========2.1========')


class Student2(object):
    __slots__ = ('name', 'age')    # 用tuple定义允许绑定的属性名称


s3 = Student2()
s3.name = 'Michael'
s3.age = 99
# s3.score = 99    # 绑定失效


# 2.2 使用__slots__只对当前类起作用，对子类不起作用
print('========2.2========')


class GradStudent2(Student2):
    pass


g1 = GradStudent2()
g1.score = 99
print(g1.score)

