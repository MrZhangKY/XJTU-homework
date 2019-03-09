#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/13 22:33'
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
# import scipy.io as sio
# import numpy as np
# import matplotlib.pyplot as plt
#
# alpha = [0.002, 0.008, 0.01, 0.02, 0.05, 0.1, 0.3, 0.35]
# P = [2, 5, 50, 200]
# e = 0.001
#
# n1 = 7
# n2 = 3
#
# file1 = 'lms_samp.mat'
# file2 = 'lms_tstsamp.mat'
#
#
# '''读取数据并绘散点图'''
# # x1 = []
# # y1 = []
# #
# # x2 = []
# # y2 = []
#
# data1 = sio.loadmat(file1)
# samp1 = data1['samp']
# samp1 = np.array(samp1)
#
# data2 = sio.loadmat(file2)
# samp2 = data2['tstsamp']
# samp2 = np.array(samp2)
#
# # for i in samp1:
# # #for i in samp2:
# #     if i[2] == 1:
# #         x1.append(i[0])
# #         y1.append(i[1])
# #     else:
# #         x2.append(i[0])
# #         y2.append(i[1])
# #
# # a = plt.subplot()
# # a.scatter(x1, y1, c='r', marker='o')
# # a.scatter(x2, y2, c='b', marker='o')
# # plt.show()
#
# '''训练神经网络权重，计算所有样本均方误差，并保存'''
#
# '''初始化权重'''
# w = np.mat(np.array([1, 1]))
#
# '''训练'''
# mse = []
#
# for k in range(200):
#     number = P[n2]
#     w_change = 0
#
#     for i in samp1:
#         data = np.mat(i[:2])
#         label = i[2]
#         '''计算加权值'''
#         result1 = np.array(w*data.reshape(2, 1))[0][0]
#         '''计算误差'''
#         bias1 = label - result1
#
#         # '''更新权值，随机逼近算法'''
#         # w = w + 2*alpha[n1]*bias1*data
#
#         '''更新权值，基于统计算法'''
#         w_change = w_change + bias1*data
#         number -= 1
#         if number == 0:
#             w = w + 2*alpha[n1]*w_change/P[n2]
#             number = P[n2]
#             w_change = 0
#
#             '''计算所有样本均方误差'''
#             mse1 = 0
#             for j in samp1:
#                 '''遍历一遍，计算误差平方和'''
#                 data = np.mat(j[:2])
#                 label = j[2]
#                 result1 = np.array(w*data.reshape(2, 1))[0][0]
#                 bias2 = abs(label - result1) * abs(label - result1)
#                 mse1 = mse1 + bias2
#             mse1 = mse1/200
#             mse.append(mse1)
#
#             '''判断均方误差'''
#             if mse1 < e:
#                 print('最终收敛样本均方误差：', mse1)
#                 break
#
# long = len(mse)
# if mse[-1] < e:
#     print('经过{long}步收敛'.format(long=long))
# else:
#     print('α为{alpha}，P为{p}，经过{long}步收敛未收敛与预期误差，最终样本均方误差为：{mse}'.format(alpha=alpha[n1],
#                                                                        p=P[n2], long=long, mse=mse[-1]))
# step = []
# for i in range(long):
#     step.append(i)
# plt.plot(step, mse)
# plt.show()
# print('此时权重为：', w)
# np.save('w_{alpha}_1'.format(alpha=alpha[n1]), w)
#
#
# '''测试'''
# '''正确的个数，及正确率'''
# accuracy = 0
# mse1 = 0
#
# for j in samp2:
#     '''遍历一遍，计算误差平方和'''
#     data = np.mat(j[:2])
#     label = j[2]
#     result1 = np.array(w*data.reshape(2, 1))[0][0]
#     bias2 = abs(label - result1) * abs(label - result1)
#     mse1 = mse1 + bias2
#     if result1 > 0:
#         result1 = 1
#     else:
#         result1 = -1
#     if result1 == label:
#         accuracy += 1
# print('检验正确的点的个数{n1}，正确率{n2}，均方误差{n3}'.format(n1=accuracy, n2=accuracy/200, n3=mse1/200))
#
#
# '''
# 18.12.14 测试数据散点图绘制，还有偏差怎么确定？
# '''

import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt

alpha = [0.002, 0.008, 0.01, 0.02, 0.05, 0.1, 0.3, 0.35]
P = [2, 5, 50, 200]
e = 0.001

n1 = 6
n2 = 3

file1 = 'lms_samp.mat'
file2 = 'lms_tstsamp.mat'


'''读取数据并绘散点图'''
# x1 = []
# y1 = []
#
# x2 = []
# y2 = []

data1 = sio.loadmat(file1)
samp1 = data1['samp']
samp1 = np.array(samp1)

data2 = sio.loadmat(file2)
samp2 = data2['tstsamp']
samp2 = np.array(samp2)

# for i in samp1:
# #for i in samp2:
#     if i[2] == 1:
#         x1.append(i[0])
#         y1.append(i[1])
#     else:
#         x2.append(i[0])
#         y2.append(i[1])
#
# a = plt.subplot()
# a.scatter(x1, y1, c='r', marker='o')
# a.scatter(x2, y2, c='b', marker='o')
# plt.show()

'''训练神经网络权重，计算所有样本均方误差，并保存'''

'''初始化权重'''
w = np.mat(np.array([1, 1]))

'''训练'''
mse = []

#for k in range(200):
number = P[n2]
w_change = 0

for i in samp1:
    data = np.mat(i[:2])
    label = i[2]
    '''计算加权值'''
    result1 = np.array(w*data.reshape(2, 1))[0][0]
    '''计算误差'''
    bias1 = label - result1

    '''更新权值，随机逼近算法'''
    w = w + 2*alpha[n1]*bias1*data

    # '''更新权值，基于统计算法'''
    # w_change = w_change + bias1*data
    # number -= 1
    # if number == 0:
    #     w = w + 2*alpha[n1]*w_change/P[n2]
    #     number = P[n2]
    #     w_change = 0

    '''计算所有样本均方误差'''
    mse1 = 0
    for j in samp1:
        '''遍历一遍，计算误差平方和'''
        data = np.mat(j[:2])
        label = j[2]
        result1 = np.array(w*data.reshape(2, 1))[0][0]
        bias2 = abs(label - result1) * abs(label - result1)
        mse1 = mse1 + bias2
    mse1 = mse1/200
    mse.append(mse1)

    '''判断均方误差'''
    if mse1 < e:
        print('最终收敛样本均方误差：', mse1)
        break

long = len(mse)
if mse[-1] < e:
    print('经过{long}步收敛'.format(long=long))
else:
    print('α为{alpha}，P为{p}，经过{long}步收敛未收敛与预期误差，最终样本均方误差为：{mse}'.format(alpha=alpha[n1],
                                                                       p=P[n2], long=long, mse=mse[-1]))
step = []
for i in range(long):
    step.append(i)
plt.plot(step, mse)
plt.show()
print('此时权重为：', w)
np.save('w_{alpha}_1'.format(alpha=alpha[n1]), w)


'''测试'''
'''正确的个数，及正确率'''
accuracy = 0
mse1 = 0

for j in samp2:
    '''遍历一遍，计算误差平方和'''
    data = np.mat(j[:2])
    label = j[2]
    result1 = np.array(w*data.reshape(2, 1))[0][0]
    bias2 = abs(label - result1) * abs(label - result1)
    mse1 = mse1 + bias2
    if result1 > 0:
        result1 = 1
    else:
        result1 = -1
    if result1 == label:
        accuracy += 1
print('检验正确的点的个数{n1}，正确率{n2}，均方误差{n3}'.format(n1=accuracy, n2=accuracy/200, n3=mse1/200))
