# !usr/bin/env python3
# -*- coding:utf-8 -*-

'hashlib'

__author__ = 'HDKidd'

import hashlib

# hashlib.md5()
# mp5.update()
# md5.hexdigest()

# 1.1 使用MD5算法计算出一个字符串的MD5值
print('========1.1========')

md5_1 = hashlib.md5()
md5_1.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5_1.hexdigest())

md5_3 = hashlib.md5()
md5_3.update('123456'.encode('utf-8'))
print(md5_3.hexdigest())

md5_4 = hashlib.md5()
md5_4.update('888888'.encode('utf-8'))
print(md5_4.hexdigest())

md5_5 = hashlib.md5()
md5_5.update('password'.encode('utf-8'))
print(md5_5.hexdigest())


# 1.2 使用MD5算法计算出一个字符串的MD5值：分块多次调用update()
print('========1.2========')

md5_2 = hashlib.md5()
md5_2.update('how to use md5 in '.encode('utf-8'))
md5_2.update('python hashlib?'.encode('utf-8'))
print(md5_2.hexdigest())


# 2.1 使用SHA1算法计算出一个字符串的SHA1值
print('========2.1========')

sha1_1 = hashlib.sha1()
sha1_1.update('123456'.encode('utf-8'))
print(sha1_1.hexdigest())


# 3.1 摘要算法应用：储存用户名和密码  (未解决）
print('========3.1========')

db = {
    'Michael': 'e10adc3949ba59abbe56e057f20f883e',
    'Bob': '21218cca77804d2ba1922c33e0151105',
    'Alice': '5f4dcc3b5aa765d61d8327deb882cf99'
}


def login(username, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    print(str(md5.hexdigest()))
    print(str(db[username]))
    if str(md5.hexdigest) == str(db[username]):
        print('login success!')
    else:
        print('Wrong password or username!')


# input_username = input('Please input your username: ',)
# input_password = input('Please input your password: ',)

# login(input_username, input_password)


# 3.2 摘要算法应用：储存用户名和密码: 增加保护——+salt
print('========3.2========')


def calc_md5(password):
    return get_md5(password + 'the-salt' + username)


# E.1 根据用户输入的登陆名和口令模拟用户注册，计算更安全的MD5
print('========E.1========')

db = {}


def get_md5(username, password):
    md5 = hashlib.md5()
    md5.update( )

def register(username, password):
    db2[username] = get_md5(password + username + 'the-salt')



