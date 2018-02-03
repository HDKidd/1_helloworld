# !usr/bin/env python3
# -*- coding:utf-8 -*-

# @property
# 1.1 限制属性的范围，以达到检查参数的目的
print('========1.1========')


class Student1(object):
    def get_score(self):
        return self.score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100!')
        self.score = value


s1 = Student1()
s1.set_score(60)
print(s1.get_score())

# s1.set_score(101)    会报错


# 2.1 使用 @property 把一个方法变成属性调用的（限制属性的范围，以达到检查参数的目的）
print('========2.1========')


class Student2(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 and 100！')
        self._score = value

# 把一个 getter 方法变成属性，只需要加上@property 就可以了，
# @property 本身又创建了另一个装饰器@score.setter，负责把一个 setter 方法变成属性赋值，


s2 = Student2()
s2.score = 100   # 实际转化为 s.set_score(100)
print(s2.score)  # 实际转化为 s.get_score()


# 2.2 使用 @property 定义只读属性（只定义getter方法，不定义setter方法）
print('========2.2========')


class Student2(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2018 - self._birth


# 上述birth是可读写属性，但age是只读属性，通过birth计算出来


# E.1 使用 @property 给一个screen对象加上width和height属性，以及一个只读属性resolution
print('========E.1========')


class Class1(object):

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            raise ValueError('width value must be positive!')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value < 0:
            raise ValueError('height value must be positive')
        self._height = value

    @property
    def res(self):
        return self._width * self._height


screen = Class1()
screen.width = 10
screen.height = 25
print(screen.width)
print(screen.height)
print(screen.res)
