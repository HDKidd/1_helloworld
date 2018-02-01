# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 继承和多态
# 1 类的继承：subclass super class
# 1.1 继承的第一个特点: 子类继承父类全部功能，比如run
print('========1.1========')


class Animal(object):
    def run(self):
        print('Animal is running...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


dog = Dog()
dog.run()

cat = Cat()
cat.run()


# 1.2 对子类增加方法
print('========1.2========')


class Dog(Animal):
    def run(self):
        print('Dog is running...')

    def eat(self):
        print('Eating meat...')


dog = Dog()
dog.run()
dog.eat()

# 1.3 继承的第二个特点：多态：子类定义相同的方法覆盖父类
print('========1.3========')


class Dog(Animal):
    def run(self):
        print('Dog is running')


class Cat(Animal):
    def run(self):
        print('Cat is running')


dog = Dog()
dog.run()

cat =Cat()
cat.run()


# 2 多态
# 2.1 定义一个类的时候，实际上是定义一种新的数据类型
print('========2.1========')

a = list()    # a 是list类型
b = Animal()    # b 是Animal类型
c = Dog()    # c 是Dog类型

print(isinstance(a, list))
print(isinstance(b, Animal))
print(isinstance(c, Dog))
print(isinstance(c, Animal))    # c 的多态表现，既是Animal, 也是Dog
print(isinstance(b, Dog))    # 反之不成立


# 2.2 多态示例
print('========2.2========')


def run_twice(animal):
    animal.run()
    animal.run()


run_twice(Animal())
run_twice(Dog())
run_twice(Cat())


class Fish(Animal):
    def run(self):
        print('Fish is running')


run_twice(Fish())    # 新增一个子类，都可以正常运行建立在父类上的函数

