#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2019/1/12 22:09'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
import numpy as np
from scipy.linalg import solve

a = np.mat([[42, 38, 18, 2], [52, 29, 13, 6],
              [61, 21, 10, 8], [67, 15, 7, 11]])
b1 = np.mat([210, 220, 230, 240]).T
b2 = np.mat([390, 400, 410, 420]).T
b3 = np.mat([330, 340, 350, 360]).T
b4 = np.mat([190, 200, 210, 220]).T

x1 = solve(a, b1)
x2 = solve(a, b2)
x3 = solve(a, b3)
x4 = solve(a, b4)

# print(x1)
# print(x2)
# print(x3)
# print(x4)

b5 = np.mat([57, 24, 12, 7])
print(b5*x1)
print(b5*x2)
print(b5*x3)
print(b5*x4)
