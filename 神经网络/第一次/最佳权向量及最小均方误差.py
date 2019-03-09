#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/19 23:25'
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
import scipy.io as sio
import numpy as np

file1 = 'lms_samp.mat'
data1 = sio.loadmat(file1)
samp1 = data1['samp']
samp1 = np.array(samp1)

P = 0
R = 0

for i in samp1:
    data = np.mat(i[:2])
    label = i[2]
    R = data.transpose() * data + R
    P = label * data + P
R = R / 200
P = P / 200

W = P * np.linalg.inv(R)

bias = 0
for i in samp1:
    data = np.mat(i[:2])
    label = i[2]
    a = label - W * data.transpose()
    bias = bias + a * a
bias = bias / 200

print('最佳权向量为{w}，最小均方误差为{b}'.format(w=W, b=bias))
