# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 元类

# 1.1 type() 既可以返回一个对象的类型，又可以创建出新的类型
print('========1.1========')


def fn1(self, name='world'):    # 定义函数
    print('Hello, %s.' % name)


Hello = type('Hello', (object,), dict(hello=fn1))    # 创建 Hello class

# 用type 创建对象的话，要依次传入三个参数，第一个是名字，第二个是父类集合，第三个是方法名称和函数绑定

h = Hello()
h.hello()

print(type(Hello))
print(type(h))


# 2.1 使用metaclass，即元类，控制类的创建行为
print('========2.1========')

# 此部分较难，暂跳过
