# !usr/bin/env python3
# -*- coding:utf-8 -*-

import base64

# base64 用64个字符来表示任意二进制数据的二进制编码方法

# 1.1 一般的base64编解码
print('========1.1========')

print(base64.b64encode(b'binary\x00string'))      # 编码
print(base64.b64decode(b'YmluYXJ5AHN0cmluZw=='))  # 解码


# 1.2 url safe的base64编解码：把不能在URL中不能直接作为参数的+和/ 分别变成-和_
print('========1.2========')

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))

# base64 使用于小段内容的编码，比如数学证书签名、cookie的内容等


