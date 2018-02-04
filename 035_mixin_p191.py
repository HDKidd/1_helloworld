# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 多重继承 & Mixin
# 1.1 多重继承
print('========1.1========')


class Animal(object):    # 总类
    pass


class Mammal(Animal):    # 大类1
    pass


class Bird(Animal):      # 大类2
    pass


class Dog(Mammal):       # 小类1.1
    pass


class Bat(Mammal):       # 小类1.2
    pass


class Parrot(Bird):      # 小类2.1
    pass


class Ostrich(Bird):     # 小类2.2
    pass


class Runnable(object):  # 定义大类3：runnable
    def run(self):
        print('Running...')


class Flyable(object):
    def fly(self):       # 定义大类4：flyable
        print('Flying...')


class Dog(Mammal, Runnable):    # 小类多重继承：2,3.1
    pass


class Bat(Mammal, Flyable):     # 小类多重继承：2,4.2
    pass




