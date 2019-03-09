#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/14 11:22'
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
import scipy.io as sio

# file1 = 'lms_samp.mat'
# data1 = sio.loadmat(file1)
# samp1 = data1['samp']
# samp1 = np.array(samp1)
#
# w = np.mat(np.load('w_0.01_1.npy'))
# for j in samp1:
#     mse1 = 0
#     data = np.mat(j[:2])
#     label = j[2]
#     '''计算加权值'''
#     result1 = np.array(w*data.reshape(2, 1))[0][0]
#     '''计算误差'''
#     bias2 = abs(label - result1) * abs(label - result1)
#     mse1 = mse1 + bias2
# print(mse1)


#w = np.mat(np.random.randn(2))


# file2 = 'lms_tstsamp.mat'
# data2 = sio.loadmat(file2)
# samp2 = data2['tstsamp']
# samp2 = np.array(samp2)
# print(samp2)

a = np.mat([1, 2, 3])

b = np.mat([1, 2, 3])

print((a+b) / 3)

print(a.transpose())
