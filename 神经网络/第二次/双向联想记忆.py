#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/25 10:15'
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

def sgn(mat):
    '''硬限幅'''
    number = mat.shape[0]
    for i in range(number):
        if mat[i]>0:
            mat[i] = 1
        else:
            mat[i] = -1
    return mat

def noise(mat, n):
    '''随机n位取反'''
    index = np.random.randint(mat.shape[0], size=n)
    for i in range(n):
        mat[index[i]] = 0 - mat[index[i]]
    return mat

a = [[1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1],
     [1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1, -1, 1, 1, -1],
     [1, 1, 1, -1, -1, -1, 1, 1, 1, -1, -1, -1, 1, 1, 1],
     [1, 1, 1, 1, -1, -1, -1, -1, 1, 1, 1, 1, -1, -1, -1]
     ]

b = [[1, 1, 1, 1, -1, -1, -1, -1, 1, 1],
     [1, 1, 1, -1, -1, -1, 1, 1, 1, -1],
     [1, 1, -1, -1, 1, 1, -1, -1, 1, 1],
     [1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
     ]

'''计算连接权重'''
w_a_b = np.mat(np.zeros([len(b[0]), len(a[0])]))
w_b_a = np.mat(np.zeros([len(a[0]), len(b[0])]))

for i in range(4):
    b1 = np.mat(b[i])
    a1 = np.mat(a[i])
    w_a_b = w_a_b + np.transpose(b1) * a1
    w_b_a = w_b_a + np.transpose(a1) * b1

print('由a到b的权值:\n', w_a_b)
print('由b到a的权值:\n', w_b_a)

'''计算能量值'''
for i in range(4):
    b1 = np.mat(b[i])
    a1 = np.mat(a[i])
    E = -a1 * w_b_a * np.transpose(b1)
    print('第{i}组能量值为：{e}'.format(i=i, e=float(E)))

'''验证联想能力'''
for i in range(4):
    b1 = np.transpose(np.mat(b[i]))
    a1 = np.transpose(np.mat(a[i]))
    for j in range(100):
        '''由b到a'''
        a1_prediction = w_b_a * b1
        sgn(a1_prediction)
        b1 = w_a_b * a1_prediction
        sgn(b1)
        '''由a到b'''
        b1_prediction = w_a_b * a1
        sgn(b1_prediction)
        a1 = w_b_a * b1_prediction
        sgn(a1)
    print('第{i}组\n由a到b预测为:{b}\n误差为:{e1}\n由b到a预测为:{a}\n误差为:{e2}'.format(i=i, b=np.transpose(b1_prediction),
                                                                     e1=np.transpose(np.transpose(np.mat(b[i]))-b1_prediction),
                                                                     a=np.transpose(a1_prediction),
                                                                     e2=np.transpose(np.transpose(np.mat(a[i]))-a1_prediction)))
