# !usr/bin/env python3
# -*- coding:utf-8 -*-

import random
import queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support

# 分布式进程   注： 暂未成功

# 1.1 服务进程：负责启动Queue，把Queue注册到网络上，然后往Queue里写入任务
print('========1.1========')

#  task master 代码：

task_queue = queue.Queue()     # 发送任务的队列
result_queue = queue.Queue()   # 接受结果的队列


class QueueManager(BaseManager):    # 从BaseManager 继承QueueManager
    pass

'''
# 把两个Queue注册到网络上，callable参数关联了Queue对象
QueueManager.register('get_task_queue', callable=lambda: task_queue)
QueueManager.register('get_result_queue', callable=lambda: result_queue)

# 注意：廖雪峰的教程里，是默认在Linux下运行的，Win下callable不能以 lambda表达式赋值，故此代码做了一定修改
'''


# 把两个Queue注册到网络上，callable参数关联了Queue对象
def return_task_queue():
    global task_queue
    return task_queue


def return_result_queue():
    global result_queue
    return result_queue


def runf():
    QueueManager.register('get_task_queue', callable=return_task_queue)
    QueueManager.register('get_result_queue', callable=return_result_queue)

    # 绑定端口5000，设置验证密码'abc'，注意Linux下address留空为本机，win下还是要输入本机IP
    manager = QueueManager(address=('155.69.191.250', 5000), authkey=b'abc')
    manager.start()  # 启动Queue

    # 获得通过网络访问的Queue对象
    task = manager.get_task_queue()
    result = manager.get_result_queue()

    # 设置任务
    for i in range(10):
        n = random.randint(0, 10000)
        print('Put task %d...' % n)
        task.put(n)

    # 从result队列读取结果
    print('Try get results...')
    for i in range(10):
        r = result.get(timeout=10)
        print('Result: %s' % r)

    # 关闭
    manager.shutdown()
    print('master has been shutdown.')


# 增加主模块判断
if __name__ == '__main__':
    freeze_support()   # 函数的任务是检查它正在运行的进程是否应该通过管道或不运行代码
    runf()



