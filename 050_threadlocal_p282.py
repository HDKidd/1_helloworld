# !usr/bin/env python3
# -*- coding:utf-8 -*-

import threading

# 多线程环境下的局部变量

# 1.1 局部变量在函数调用的时候传递很麻烦
print('========1.1========')


def process_student(name):
    std = Student(name)     # std 是局部变量，但是每个函数都要用，因此必须传进去
    do_task_1(std)
    do_task_2(std)


def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)


def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)

# 上述每个函数一层一层调用局部变量传参数，代码不够简洁


# 1.2 threadLocal
print('========1.2========')

local_school = threading.local()   # 创建全局ThreadLocal对象


def process_student():    # 获取当前线程关联的student
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))


def process_thread(name):    # 绑定 ThreadLocal 的student
    local_school.student = name
    process_student()


t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()





