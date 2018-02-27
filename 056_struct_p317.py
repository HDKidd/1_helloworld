# !usr/bin/env python3
# -*- coding:utf-8 -*-

import struct

# struct （待解决）

# struct.pack(fmt, v1, v2, ...)
# struct.unpack(fmt, buffer)

# format
# <         little-endian
# >         big-endian
# c         char            (1 byte)   1字节无定义字符
# I         unsigned int    (4 bytes)  无符号4字节整数
# H         unsigned short  (2 bytes)  无符号2字节整数


# 1.1 把一个32位无符号整数变成字节会非常麻烦
print('========1.1========')

n1 = 10240099  # 4字节无符号整数
b1 = (n1 & 0xff000000) >> 24
b2 = (n1 & 0xff0000) >> 16
b3 = (n1 & 0xff00) >> 8
b4 = n1 & 0xff
bs = bytes([b1, b2, b3, b4])
print(bs)


# 1.2 struct的pack函数把任意数据类型变成bytes
print('========1.2========')

print(struct.pack('>I', 10240099))
# pack 的第一个参数是处理指令，'>I'的意思是：>表示字节顺序是big-endian，或称网络序，I表示4字节无符号整数


# 1.3 unpack把bytes变成相应的数据类型
print('========1.3========')

print(struct.unpack('>IH', b'\xf0\xf0\xf0\xf0\x80\x80'))
# unpack 的I表示4字节无符号整数，H表示2字节无符号整数


# 2.1 用struct分析位图文件.bmp
print('========2.1========')

f1 = open('D:/Python/Programs/test.bmp', 'rb')
f2 = f1.read(30)
print(f2)
f1.close()

# 2字节的'BM'表示Win位图，'BA'表示OS/2位图；
# 4字节整数：表示位图大小；
# 4字节整数：保留位，始终为0；
# 4字节整数：实际图像的偏移量；
# 4字节整数：Header的字节数；
# 4字节整数：图像宽度；
# 4字节整数：图像高度；
# 2字节整数：始终为1；
# 2字节整数：颜色数。

print(struct.unpack('<ccIIIIIIHH', f2))
# 输出结果说明：1，是win位图；2，大小为1284x573，颜色数为24


# E.1 编写一个程序，可以检查任意文件是否是位图文件，如果是，打印出图片大小和颜色数。
print('========E.1========')


def bmp_check(file):
    with open(file, 'rb') as f3:
        bs = f3.read(30)
        ts = struct.unpack('<ccIIIIIIHH', bs)
        if ts[0] == b'B' and ts[1] == b'M':
            print('______________________')
            print('File Type: bmp')
            print('File Size: %d x %d' % (ts[6], ts[7]))
            print('File Colors: %d' % ts[9])
        else:
            print('File Type: unknown')
        print('Check done.')
        print('______________________')

bmp_check('test.bmp')
bmp_check('doctIO_rb_test.jpg')
