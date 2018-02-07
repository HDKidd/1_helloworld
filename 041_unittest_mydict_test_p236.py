# !usr/bin/env python3
# -*- coding:utf-8 -*-

# 单元测试

# 2.1 编写单元测试

import unittest

from mydict import Dict


class TestDict(unittest.TestCase):

    def test_init(self):
        d = Dict(a=1, b='test')
        self.assertEqual(d.a, 1)     # 断言d.a = 1
        self.assertEqual(d.b, 'test')     # 断言d.b = 'test'
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')

    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):               # 可以在每次测试前运行一段代码，比如插入数据库
        print('setUp...')

    def tearDown(self):            # 可以在每次测试前结束上面插入的代码
        print('tearDown...')


if __name__ == '__main__':
    unittest.main()

# 直接运行本脚本即可进行单元测试
