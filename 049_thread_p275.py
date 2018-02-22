# !usr/bin/env python3
# -*- coding:utf-8 -*-

import time
import threading

# 多线程——高级模块：threading

# 1.1 启动一个线程就是把一个函数传入并穿件thread实例，然后调用start()方法执行
print('========1.1========')

# 新线程执行的代码：


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(0.1)
    print('thread %s endde.' % threading.current_thread().name)


print('thread %s is runnning...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
print('thread %s ended.' % threading.current_thread().name)


# 2.1 多线程变量共享同步，多进程变量不共享不同步，下为多线程改变共享变量实例
print('========2.1========')


# 假定银行存款：

balance1 = 0


def change_it1(n):
    global balance1   # global:定义为全局变量（共享变量）
    balance1 = balance1 + n
    balance1 = balance1 - n


def run_thread1(n):
    for i in range(100000):
        change_it1(n)


t1 = threading.Thread(target=run_thread1, args=(5,))
t2 = threading.Thread(target=run_thread1, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()

print(balance1)

# 多次执行上述代码可发现输出结果不定为0，原因为共享变量在t1, t2两个线程交替运作时共同改变


# 2.2 通过锁定函数，避免共享变量的不稳定：threading.lock()
print('========2.2========')

balance2 = 0
lock = threading.Lock()


def change_it2(n):
    global balance2
    balance2 = balance2 + n
    balance2 = balance2 - n


def run_thread2(n):
    for i in range(100000):
        lock.acquire()      # 先获取一个lock，相当于“锁定”，当多个线程同时执行锁定时，只有一个线程能成功
        try:
            change_it2(n)
        finally:
            lock.release()  # 释放刚才的lock，相当于“解锁”，一定要解锁，否则等待锁的其他线程会变为死线程，所以使用try finally来确保锁一定被释放


t3 = threading.Thread(target=run_thread2, args=(5,))
t4 = threading.Thread(target=run_thread2, args=(8,))
t3.start()
t4.start()
t3.join()
t4.join()

print(balance2)
