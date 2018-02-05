# !usr/bin/env python3
# -*- coding:utf-8 -*-

# debug

# 1.1 错误码
print('========1.1========')


def foo():
    r = abs(-1)
    if r==(-1):
        return (-1)
    return r


def bar():
    r = foo()
    if r==(-1):
        print('Error')
    else:
        pass


# 2.1 try 捕获错误类
print('========2.1========')

try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


# 2.2 上述代码存在错误，将被除数改为2如下：
print('========2.2========')

try:
    print('try...')
    r = 10 / 2
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')


# 2.3 可以有多个except来捕获不同类型的错误
print('========2.3========')

try:
    print('try...')
    r = 10 / int('b')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError：', e)
else:
    print('no Error')
finally:
    print('finally...')
print('END')


# 2.4 错误也是类，except不仅捕获该类错误，也会捕获该类的子类
print('========2.4========')

try:
    foo()
except ValueError as e:
    print('ValueError')
except UnicodeDecodeError as e:
    print('UnicodeDecodeError')
else:
    print('No Error')
finally:
    print('finally...')
print('END')

# 以上代码，第二个except永远不会捕获成功，因为UnicodeDecodeError是ValueError的子类

# 2.5 try except 可以跨越多层调用捕获错误
print('========2.5========')


def foo1(s):
    return 10 / int(s)


def bar1(s):
    return foo1(s) * 2


def main():
    try:
        bar1('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')


print(main())


# 3 调用堆栈

# 3.1 如果错误没有被捕获，就会一直向上直到被解释器捕获
print('========3.1========')


def foo2(s):
    return 10 / int(s)


def bar2(s):
    return foo2(s) * 2


def main2():
    bar2('0')


# main2() 输出错误信息如下：
'''
Traceback (most recent call last):    # 表明代码存在错误

File "D:/Python/Programs/039_debug_p219.py", line 130, in <module>
    main2()                           # 在第130行调用main()时出错了

File "D:/Python/Programs/039_debug_p219.py", line 127, in main2
    bar2('0')                         # 上面调用的错误原因在第127行的调用bar2错误
    
File "D:/Python/Programs/039_debug_p219.py", line 123, in bar2
    return foo2(s) * 2                 # 上面调用的错误原因在第123行的调用foo2错误

File "D:/Python/Programs/039_debug_p219.py", line 119, in foo2
    return 10 / int(s)                 # 上面调用的错误原因在第119行的语句错误
    
ZeroDivisionError: division by zero    # 表明具体错误类型
'''


# 4.1 logging 模块：记录错误信息
print('========4.1========')

import logging


def foo3(s):
    return 10 / int(s)


def bar3(s):
    return foo3(s) * 2


def main3():
    try:
        bar3('0')
    except Exception as e:
        logging.exception(e)


# 执行 main3()
print('END')


# 5.1 抛出错误：实质是在错误类中创建实例
print('========5.1========')


class FooError(ValueError):
    pass


def foo4(s):
    n = int(s)
    if n == 0:
        raise FooError('invalid value: %s' % s)
    return 10 / n


# 执行foo4('0') 可以跟踪到自己定义的错误
