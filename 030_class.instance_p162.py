# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 类和实例 Class & Instance
# 1.1 定义类，创建实例
print('========1.1========')


class Student1(object):  # 类名通常是大写的单词，object是所有类最终都会继承的类
    pass


bart1 = Student1()
print(bart1)  # 输出的 0x0000028BF695FF28 是内存地址
print(Student1)

# 1.2.1 给一个实例绑定属性
print('========1.2.1========')

bart1.name = 'Bart Simpsn'
print(bart1.name)

# 1.2.2 定义类的时候强制定义属性，此时在创建实例时必须传入匹配的参数
print('========1.2.2========')


class Student2(object):
    def __init__(self, name, score):  # __init__的第一个参数永远是self表示实例本身
        self.name = name
        self.score = score


bart2 = Student2('A', 59)  # 此时创建实例的话必须传入匹配的参数
print(bart2.name)
print(bart2.score)

# 2.1 数据封装: 直接在类的内部定义访问数据的函数（这种函数称为方法Method)
print('========2.1========')


class Student3(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))


bart3 = Student3('B', 66)
print(bart3.name)
bart3.print_score()

# 3.1.1 访问限制：实例的变量名以__开头，使其变为私有变量
print('========3.1.1========')


class Student4(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))


bart4 = Student4('D', 99)
# print(bart4.__name)    # 此处会报错，无法从外部访问实例变量
