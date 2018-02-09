# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 文件读写

# 1.1 读文件文件 open(r)
print('========1.1========')

f = open('D:\Python\Programs\doctIO_readtest.txt', 'r')

print(f.read())

f.close()


# 1.2 使用try...finally 来保证文件正确关闭
print('========1.2========')

try:
    f = open('D:\Python\Programs\doctIO_readtest.txt', 'r')
    print(f.read())
finally:
    if f:
        f.close()


# 1.3 使用 with 实现自动调用 close()
print('========1.3========')

with open('D:\Python\Programs\doctIO_readtest.txt', 'r') as f:
    print(f.read())


# 1.4 read() 几种模式
print('========1.4========')

with open('D:\Python\Programs\doctIO_readtest.txt', 'r') as f:
    print(f.read(10))     #  读取10个字节的内容
    print(f.read(10))     #  读取10个字节的内容
    print(f.readline())   #  读取下一个行的内容
    for line in f.readlines():
        print(line.strip())    # 读取所有行的内容


# 2.1 读二进制文件 open(rb) 如图片，视频
print('========2.1========')

f2 = open('D:\Python\Programs\doctIO_rb_test.jpg', 'rb')
print(f2.read(100))


# 3.1 读非UTF-8文件：如读取GBK编码文件
print('========3.1========')

# with open('D:\Python\Programs\doctIO_test.txt', 'r'， encoding='gbk') as f:


# 4.1 写文件
print('========4.1========')

with open('D:\Python\Programs\doctIO_writetest.txt', 'w') as f:
    f.write('write test')   # 此写入是覆盖的

