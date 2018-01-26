#!/usr/bin/env python3
# -*- coding:utf-8 -*-

height = float(input('Please input your heiget(m):',))
weight = float(input('Please input your weight(kg):',))
bmi = weight/(height*height)
if bmi < 18.5:
    print('Your BMI is:%.2f' % bmi)
    print('you are underweight')
elif bmi < 25:
    print('Your BMI is:%.2f' % bmi)
    print('you are normal-weight')
elif bmi < 28:
    print('Your BMI is:%.2f' % bmi)
    print('you are overweight')
elif bmi < 32:
    print('Your BMI is:%.2f' % bmi)
    print('you are fat')
else:
    print('Your BMI is:%.2f' % bmi)
    print('you are obesity')

