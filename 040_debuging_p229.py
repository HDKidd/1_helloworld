# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 调试

# 1.1 直接用print把可能有问题的变量打印出来
print('========1.1========')


def foo1(s):
    n = int(s)
    print('>>>n = %d' % n)
    return 10 / n


def main1():
    foo1('0')


# main1() 输出结果中会有 n = 0    此方法缺点是以后还要再删掉

# 1.2 使用 assert 辅助查看错误信息
print('========1.2========')


def foo2(s):
    n = int(s)
    assert n != 0, 'n is zero'
    return 10 / n


def main2():
    foo2('0')


# main2() 输出结果会有 AssertionError: n is zero

# 启动 Python 解释器时可以用-O 参数来关闭 assert


# 1.2 使用 logging 记录和输出错误到文件
print('========1.3========')

import logging
logging.basicConfig(level=logging.INFO)

s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
