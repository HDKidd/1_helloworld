#!/usr/bin/env python3
# -*- coding:utf-8 -*-

age = int(input('Please insert your age:',))
if age >= 18:
    print('your age is', age)
    print('adult')
elif age >= 6:
    print('your age is', age)
    print('teenager')
else:
    print('your age is', age)
    print('Kid')
