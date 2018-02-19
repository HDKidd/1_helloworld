# !usr/bin/env python3
# -*- coding:utf-8 -*-

import pickle
import json

# 序列模块 pickle

# 1.1 把一个对象序列化成一个bytes  pickle.dumps
print('========1.1========')

d1 = dict(name='Bob', age=20, score=88)
print(pickle.dumps(d1))


# 1.2 直接把对象序列化后写入一个file-like Object  pickle.dump()
print('========1.2========')

f1 = open('dump.txt', 'wb')
pickle.dump(d1, f1)
f1.close()


# 1.3 反序列化出对象 pickle.load()
print('========1.3========')

f2 = open('dump.txt', 'rb')
d2 = pickle.load(f2)
f2.close()
print(d2)


# 2 序列化成JSON以便在不同的编程语言之间传递对象

# 2.1 把 Python 对象变成一个 JSON
print('========2.1========')

d3 = dict(name='Bob', age=20, score=88)
print(json.dumps(d3))     # 返回一个str内容就是标准的JSON


# 2.2 把JSON的字符串反序列化为python对象
print('========2.2========')

j1 = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(j1))


# 3.1 把 class 进行 JSON 序列化
print('========3.1========')


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score


s1 = Student('Bob', 20, 88)
# print(json.dumps(s1))    不成功，需要先写一个可序列对象的转化


def student2dic(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }


print(json.dumps(s1, default=student2dic))


# 3.2 把任意 class 的实例变为可序列化的dict
print('========3.2========')

print(json.dumps(s1, default=lambda obj: obj.__dict__))


# 3.3 把JSON反序列化未一个Student的对象实例:使用object—_hook函数来转化
print('========3.3========')


def dict2student(d):
    return Student(d['name'], d['age'], d['score'])


j2 = '{"name": "Bob", "age": 20, "score": 88}'
print(json.loads(j2, object_hook=dict2student))
