# !usr/bin/env python3
# -*- coding:utf-8 -*-

import os, time, random
from multiprocessing import Process, Queue

# 进程间通信

# 1.1 queue
print('========1.1========')


def write(q):     # 写数据进程
    print('Process to write: %s' % os.getpid())  # getpid 获得当前进程的进程号
    for value in ['A', 'B', 'C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


def read(q):     # 读数据进程
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    q = Queue()      # 父进程创建Queue， 并传给各个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()       # 启动子进程pw，写入
    pr.start()       # 启动子进程pr，读取
    pw.join()        # 等待子进程pw结束
    pr.terminate()   # 强行终止子进程pr（因为pr是一个死循环代码）


