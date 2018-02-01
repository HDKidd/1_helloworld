# !usr/bin/env python3
# -*- coding:utf-8 -*-

import types

# 获取对象 Object 信息
# 1 type
print('========1========')

print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

# 1.1 type() 返回的是类型
print('========1.1========')

print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('123'))
print(type('abs') == str)
print(type('abs') == type(123))

# 1.2 type() 判断对象是否为函数
print('========1.2========')


def fn():
    pass


print(type(fn) ==types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x:x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)


# 2.1 instance 用于判断 class 的类型
print('========2.1========')


class Animal(object):
    def run(self):
        print('Animal is running')


class Dog(Animal):
    pass


class Husky(Dog):
    pass


a = Animal()
d = Dog()
h = Husky()

print(isinstance(h, Husky))
print(isinstance(h, Dog))    # 可见isinstance判断的是对象是否该类型本身
print(isinstance(h, Animal))
print(isinstance(d, Animal))
print(isinstance(d,Husky))

# 2.2 instance 用于判断 非 class 的类型（即默认的类型如 list 和 tuple）
print('========2.2========')

print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


# 3.1 dir() 获取一个对象的所有属性和方法
print('========3.1========')

print(dir('ABC'))


# 3.2 特殊属性和方法：__xxx__
print('========3.2========')

print(len('ABC'))
print('ABC'.__len__())


class MyDog(object):    # 自己定义的类如果也想达到上述等价关系，则需加定义一个方法
    def __len__(self):
        return 100


dog = MyDog()
print(len(dog))
print(dog.__len__())


# 3.3 普通属性和方法_
print('========3.3========')

print('ABC'.lower())


# 4 测试和操作对象：getattr(), setattr(), hasattr()
# 4.1 测试和操作对象的属性
print('========4.1========')


class MyObject(object):
    def __init__(self):
        self.x = 9

    def power(self):
        return self.x * self.x


obj = MyObject()

print(hasattr(obj, 'x'))    # 测试有没有属性’x'
print(obj.x)
print(hasattr(obj, 'y'))    # 测试有没有属性'y'

setattr(obj, 'y', 19)       # 设置一个属性'y'
print(hasattr(obj, 'y'))

print(getattr(obj, 'y'))    # 获取属性'y'
print(obj.y)                # 获取属性'y'

# print(getattr(obj, 'z'))    # 获取不存在的属性'z'，会报错
print(getattr(obj, 'z', 404))     # 传入参数，使获取不存在属性时候报404


# 4.2 测试和操作对象的方法
print('========4.2========')

print(hasattr(obj, 'power'))      # 测试有没有方法'power'
print(getattr(obj, 'power'))      # 获取方法'power'
fn = getattr(obj, 'power')        # 获取属性'power'并赋值到变量fn中
print(fn)
print(fn())

