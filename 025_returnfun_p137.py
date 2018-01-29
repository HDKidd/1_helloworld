# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 返回函数
# 1.1 返回函数
# 1.1.1.1 一般的求和函数
print('========1.1.1.1========')


def ordinary_sum(*args):
    x = 0
    for n in args:
        x = x + n
    return x


print(ordinary_sum(1, 2, 3, 4, 5))


# 1.1.1.2 不返回求和结果，只返回求和的函数
print('========1.1.1.2========')


def functional_sum(*args):
    def sum():
        x = 0
        for n in args:
            x = x + n
        return x
    return sum


print(functional_sum())
f = functional_sum(1, 2, 3, 4, 5)
print(f())

# 1.1.1.3 每次调用都会返回一个新的函数，即使传入相同的参数
print('========1.1.1.3========')

f1 = functional_sum(1, 2, 3, 4, 5)
f2 = functional_sum(1, 2, 3, 4, 5)
print(f1 == f2)

# 1.1.2 Closure(闭包结构)返回的函数不会立即引用内部变量，只有最终才会。
# 故返回闭包的时候不要引用循环变量或者会变化的变量
print('========1.1.2========')


def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i*i
        fs.append(f)
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 1.1.3如果一定要引用循环变量的话，就要再创建一个函数来绑定循环函数当前值
print('========1.1.3========')


def count():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i))    # f(i)立刻被执行，i的当前值被传入f()中
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
