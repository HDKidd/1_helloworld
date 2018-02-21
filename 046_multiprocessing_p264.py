# !usr/bin/env python3
# -*- coding:utf-8 -*-

import os
import random
import time
from multiprocessing import Pool
from multiprocessing import Process

# 多进程 multiprocessing

# 1.1 创建子进程
print('ABC')


def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))    # 创建一个进程实例
    print('Child process will start.')
    p.start()                                       # 用start()方法启动
    p.join()             # join()方法等待子进程结束后再继续往下运行，通常用于进程间的同步
    print('Child process end.')


# 2.1 进程池 Pool
print('ABC')


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)   # time.sleep 方法为推迟执行一定秒数
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(9)       # 限制同时运行的进程数最多为9个，默认大小是CPU核数
    for i in range(8):
        p.apply_async(long_time_task, args=(i,))  # apply_async 是异步非阻塞，不用等待当前进程执行完毕，随时根据系统调度来进行进程切换。
    print('Waiting for all subprocesses done...')
    p.close()     # close 方法后不能继续添加新的子进程了
    p.join()
    print('All subprocesses done.')

