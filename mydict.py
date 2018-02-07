# !usr/bin/env python3
# -*- coding:utf-8 -*-

'a unit test module'

__author__ = 'Kidd He'


class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value



# 单元测试 以上是编写一个Dict类，这个类的行为和dict一致，本文件作为被测试模块

