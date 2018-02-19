# !usr/bin/env python3
# -*- coding:utf-8 -*-

import os

# 操作文件和目录，使用os 模块

# 1.1 操作系统类型 os.name
print('========1.1========')

print(os.name)  # 输出 nt 表示 windows 系统，posix 表示 Linux\Unix\mac OS 系统

# 2.1 环境变量 os.environ
print('========2.1========')

print(os.environ)  # 查看所有的环境变量

# 2.2 获取某个环境变量的值 os.environ.get
print('========2.2========')

print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))

# 3.1 操作文件和目录 os.path.abspath
print('========3.1========')
print(os.path.abspath('.'))  # 查看当前目录的绝对路径：

# 3.2 创建和删除目录 os.path.mkdir rmdir
print('========3.2========')
os.path.join('D:/Python/Programs', '044_testdir')  # 把新目录的完整路径（合并路径）表现出来（还未创建）
# os.mkdir('D:/Python/Programs/044_testdir')    # 创建新目录
# os.rmdir('D:/Python/Programs/044_testdir')    # 删除该目录


# 3.3 合并路径 os.path.join()
print('========3.3========')

print(os.path.join('D:/Python/Programs', '044_testdir'))  # 注意Windows的路径分隔符是逆斜杠

# 3.4.1 拆分路径 os.path.split()
print('========3.4.1========')

print(os.path.split('D:/python/Programs/044_testdir'))

# 3.4.2 拆分扩展名 os.path.splittext()
print('========3.4.2========')

print(os.path.splitext('D:/python/Programs/doctIO_writetest.txt'))

# 3.5  重命名文件 os.rename
print('========3.5========')

# os.rename('IOdir_text.txt', 'IOdir_textrename.txt')


# 3.6  删除文件 os.remove
print('========3.6========')

# os.remove('IOdir_textrename.txt')


# 4.1 列出当前目录下所有目录
print('========4.1========')

print([x for x in os.listdir('.') if os.path.isdir(x)])

# 4.2 列出当前目录下所有目录
print('========4.2========')

print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

# E.1 利用os模块编写一个实现dir-L输出的程序   暂未解决
print('========E.1========')


def dir_l(path='.'):
    L = os.listdir(path.abspath('D:\python\Programs'))
    for file in L:
        print(file)


# E.2 编写一个能在当前目录以及所有子目录下查找文件名包含指定字符串的文件，并打印相对路径
print('========E.2========')

# 暂未解决
