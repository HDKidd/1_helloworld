# !usr/bin/env python3
# -*- coding:utf-8 -*-

from io import StringIO
from io import BytesIO

# StringIO 及 BytesIO

# 1 StringIO 操作 str 数据
# 1.1 把str写入StringIO, 并获取值
print('========1.1========')

f1 = StringIO()
print(f1.write('Hello'))
print(f1.write(' '))
print(f1.write('world!'))
print(f1.getvalue())

# 1.2 读取StringIO
print('========1.2========')

f2 = StringIO('Hello!\nHi!\nGoodbye')     # \n 换行符
while True:
    s2 = f2.readline()
    if s2 == '':
        break
    print(s2.strip())


# 2 BytesIO 操作 bytes 数据
# 2.1 把bytes写入BytesIO, 并获取值
print('========1.1========')

f3 = BytesIO()
print(f3.write('中文'.encode('utf-8')))
print(f3.getvalue())                      # 写入的是二进制的bytes, 不是str


# 2.2 读取BytesIO
print('========2.2========')

f4 = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f4.read())
