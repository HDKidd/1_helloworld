# !usr/bin/env python3
# -*- coding:utf-8 -*-

import functools

# 装饰器 decorator: 在代码运行期间动态增加功能的方式,本质上是一个返回函数的高阶函数
# 1.1 通过变量调用函数
print('========1.1========')


def now():
    print('2018-01-26')


f = now
print(f())

# 1.1 获取函数的名字
print('========1.1========')

print(now.__name__)
print(f.__name__)

# 2.1 定义一个能打印函数名的decorator
print('========2.1========')


def log(func):
    def wrapper(*args, **kw):
        print('This func is called: %s():' % func.__name__)
        return func(*args, **kw)
    return wrapper


@log        # @ 语法的用途是为函数装饰上log, 相当于在函数now定义时，执行了语句 now = log(now)
def now():
    print('2018-01-26')


print(now())

# 2.2 定义一个能打印文本日志的decorator
print('========2.2========')


def log(text):
    def decorator(func2):
        def wrapper2(*args, **kw):
            print('%s %s():' % (text, func2.__name__))
            return func2(*args, **kw)
        return wrapper2()
    return decorator


@log('Hello!')
def now2():
    print('2018-01-29')


print(now.__name__)    # 以上装饰器的写法会导致函数名发生改变

# 2.3 定义一个能打印文本日志的decorator, 同时不改变函数名
print('========2.3========')


def log(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper()
    return decorator


@log('hahahahahah')
def now3():
    print('2018-99-99')


# E.1 编写一个decorator 能在函数调用前后打印出begin call 和end call的日志
print('========E.1========')


def log(text1, text2):
    def decorator(func):
        @functools.wraps(func)
        def wrapper1(*args, **kw):
            print(text1)
            fun = func(*args, **kw)
            print(text2)
            return fun
        return wrapper1()
    return decorator


@log('begin call', 'end call')
def now4():
    print('2020-20-20')


# 其实是now4 = log(now4)。所以先返回 decorator 函数，并调用之，调用的时候输入的参数是now。
# 当调用参数为 now4 的 decorator 时，执行的是wrapper函数的返回值。

