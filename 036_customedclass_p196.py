# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 定制类
# 1.1 __str__: 改变打印实例时输出的结果
print('========1.1========')


class Student1(object):

    def __init__(self, name):
        self.name = name


print(Student1('Michael'))


# 打印结果是：<__main__.Student object at 0x0000022E13330F28>


class Student2(object):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student2 object (name: %s)' % self.name


print(Student2('Michael'))  # 打印结果好看多了
s = Student2('Michael')

# 2.1 __iter__,__next__：使类变成可迭代对象，可用于 for in 循环
print('========2.1========')


class Fib(object):

    def __init__(self):
        self.a, self.b = 0, 1  # 初始化两个计数器

    def __iter__(self):
        return self  # 实例本身是迭代对象，故返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b  # 计算下一个值
        if self.a > 1000:  # 设定循环退出条件
            raise StopIteration()
        return self.a  # 返回最终值


l1 = []
for n in Fib():
    l1.append(n)

print(l1)

# 上述将类变成可迭代对象，但不能像list 一样按照下标取出元素

# 3.1 __getitem__: 可迭代类可以像list一样获取具体元素
print('========3.1========')


class Fib(object):

    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a


f = Fib()
print(f[0])
print(f[5])
print(f[25])

# 上述普通list的切片方法会报错，要用判断语句修正
# 原因是getitem传入的参数可能是一个int也可能是一个切片对象slice

# 3.2 修正为可以切片的类
print('========3.2========')


class Fib(object):

    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            l2 = []
            for x in range(stop):
                if x >= start:
                    l2.append(a)
                a, b = b, a + b
            return l2


f = Fib()
print(f[0:5])
print(f[2:10])


# 4.1 __getattr__ 过难，暂跳过


# 5.1 __call__: 直接调用实例
print('========5.1========')


class Student3(object):

    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)


s3 = Student3('Michael')
s3()

# 5.2 callable 对象（可调用的对象或函数）
print('========5.2========')

print(callable(Student1))
print(callable(Student3))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))

