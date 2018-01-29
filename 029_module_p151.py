# !usr/bin/env python3
# -*- coding:utf-8 -*-

'a test module'

__author__ = 'He Dekun'

import sys

# 模块 Module
# 1.1 模块示例：编写一个 hello 模块
print('========1.1========')


def test():
    args = sys.argv
    if len(args) == 1:
        print('Hello, world')
    elif len(args) == 2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


if __name__ == '__main__':    # 如果直接运行本模块文件的话，if判定会成功，会打印出测试结果，如果从别处导入本模块的话，则不会
    test()

# 2.1 作用域：规定某些变量和函数只在模块内部使用：_或者__起头的
print('========2.1========')


def _private_1(name):
    return 'Hello, %s' % name


def _private_2(name):
    return 'Hi, %s' % name


def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)


# 在模块里被公开的是greeting函数，而这个函数的内部逻辑用private隐藏了起来。
# 因此，调用greeting函数时不用关心内部的细节，可以实现代码的封装和抽象。

