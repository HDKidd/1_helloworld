# !sur/bin/env python3
# -*- coding:utf-8 -*-

import re

# 正则表达式 Regular Expression

# 1.1 基础字符描述
print('========1.1========')

'''
\d     匹配一个数字
\w     匹配一个字母或者数字或汉子或下划线
\s     表示匹配一个空格（包括Tab等空白符）
.      匹配任意字符
*      任意个字符（包括0个）
+      至少一个字符
？     0个或者1个字符
{n}    n个字符
{n,m}  n-m个字符
'''

'''
示例： \d{3}\s+\d{3,8}  

\d{3}  表示匹配三个数字
\s+    表示匹配至少一个空格
\d{3,8}表示匹配3个到8个数字

综上，以上正则表达式可以用来匹配任意空格隔开的带区号的电话号码
如果要匹配010-12345这样的号码，需要用 \ 将 - 转义

\d{3}\-\d{3,8} 
'''

# 1.2 进阶字符描述
print('========1.2========')

'''
[0-9a-zA-Z\_]     可以匹配一个数字、大小写字母或者下划线，注意是一个
[0-9a-zA-Z\_]+    可以匹配由至少一个数字、大小写字母或者下划线组成的字符串
[a-zA-Z\_][0-9a-zA-Z\_]*    可以匹配由字母或者下划线开头，后接任意个由字母数字或者下划线组成的字符串
[a-zA-Z\z][0-9a-zA-Z\_]{0,19}     精确限制了上述匹配字符串的长度是1-20个字符，其中前面1个字符，后面最多19个字符

A|B      匹配A或者B，例如用 [P|p]ython 来匹配 Python 或者 python
^        表示行的开头
^\d      表示必须以数字开头
$        表示行的结束
\d$      表示必须以数字结束
'''

# 2 re模块：包含所有正则表达式的功能
# 2.1 判断正则表达式是否匹配
print('========2.1========')

r1 = re.match(r'^\d{3}-\d{3,8}$', '010-12345')
print(r1)  # match方法判断是否匹配，如果匹配成功，返回一个match对象，否则返回None

# 常见的判断句法:
test = '010-12345'  # 此处为示例，实际为输入的字符串
if re.match(r'^\d{3}-\d{3,8}$', test):
    print('OK')
else:
    print('failed')

# 2.2 用正则表达式切分字符串
print('========2.2========')

r2 = 'a b  c'.split(' ')  # 普通的方法：识别出空格并分割，但无法识别连续的空格
print(r2)  # 注意输出结果把后面的一个空格当成有效字符输出出来了

r3 = re.split(r'\s+', 'a b  c')  # split方法是匹配出对应字符，摘除掉
print(r3)

r4 = re.split(r'[\s,;]+', 'a,b;; c   d')
print(r4)  # 摘除空格 逗号 分号，类似的语句可以用于把不规范的输入转化成正确的数组

# 2.3 分组：用正则表达式提取子串。（）表示要提取的分组
print('========2.3========')

r5 = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print(r5)
print(r5.group(0))  # group(0)永远是原始字符串
print(r5.group(1))  # group(1)是第一个子串
print(r5.group(2))  # group(2)是第二个子串

# 2.3.1 分组示例：用正则表达式识别合法的时间
print('========2.3.1========')

t = '10:05:3'

r6 = re.match(
    r'^(0[0-9]|1[0-9]|2[0-3]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',
    t)

print(r6)
print(r6.group(0))
print(r6.group(1))
print(r6.groups())  # groups方法也可以分割字符串

# 2.4 贪婪匹配：正则匹配默认是贪婪匹配，即尽可能匹配多的字符
print('========2.4========')

r7 = re.match(r'^(\d+)(0*)$', '1023000')
print(r7.groups())  # 由于\d+采用贪婪匹配，直接把后面的0全匹配了，结果0*只能匹配空字符串

r8 = re.match(r'^(\d+?)(0*)$', '1023000')
print(r8.groups())  # 为了让\d+不要贪婪匹配，加一个？


# 3.1 预编译
print('========3.1========')

re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')  # 预编译
r9 = re_telephone.match('010-12345')
print(r9.groups())

r10 = re_telephone.match('020-8086').groups()
print(r10)


# E.1 写一个验证Email地址的正则表达式，验证出纯Email地址
print('========E.1========')

email1 = input('Please input your email: ',)
re_email1 = re.compile(r'^(\w+)@([0-9a-zA-Z]+).([0-9a-zA-Z]+.?[0-9a-zA-Z]+.?[a-zA-Z]+)$')
rm1 = re_email1.match(email1)

if rm1 is None:
    print('Not a legal email address.')
else:
    print('Your email name is: ', rm1.group(1))

# E.2 写一个验证Email地址的正则表达式，验证出带有名字的Email地址
print('========E.2========')

email2 = input('Please input your email card: ',)
re_email2 = re.compile(r'^(<\w+\s?\w+>)\s(\w+@[0-9a-zA-Z]+.[0-9a-zA-Z]+.?[a-zA-Z]+.?[a-zA-Z]+)$')
rm2 = re_email2.match(email2)

if rm2 is None:
    print('Not a legal email card.')
else:
    print(rm2.group(1), 'Your email address is: ', rm2.group(2))
