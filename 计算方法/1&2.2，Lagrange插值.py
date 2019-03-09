#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/9 22:01'
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
import datetime
from matplotlib import pyplot as plt
import numpy as np

point_draw = np.arange(0, 20.01, 0.01)
time_draw = np.arange(0, 24.01, 0.01)

author = '张开宇'
time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
print('作者：{author}，日期：{date}'.format(author=author, date=time))

point = []
for i in range(21):
    point.append(i)

time = []
for i in range(25):
    time.append(i)

depth = [9.01, 8.96, 7.96, 7.97, 8.02, 9.05, 10.13, 11.18, 12.26, 13.28, 13.32, 12.61, 11.29, 10.22,
         9.15, 7.90, 7.95, 8.86, 9.81, 10.80, 10.93]

temperature = [15, 14, 14, 14, 14, 15, 16, 18,
               20, 20, 23, 25, 28, 31, 34, 31,
               29, 27, 25, 24, 22, 20, 18, 17, 16]

def Lagrange(x_list, y_list, variable_list):
    long = len(x_list)
    result_list = []

    for m in variable_list:
        '''计算所有自变量，返回一个向量'''
        count = 0
        result = 0
        for i in range(long):
            '''所有的y'''
            numerator = 1
            denominator = 1
            for j in range(long):
                '''计算分子，不减索引为count的x'''
                if j == count:
                    numerator = numerator
                else:
                    numerator = numerator * (m - x_list[j])
            for k in range(long):
                '''计算分母，用索引为count的x去减'''
                if k == count:
                    denominator = denominator
                else:
                    denominator = denominator * (x_list[count] - x_list[k])
            result = result + y_list[i] * numerator / denominator
            count += 1
        result_list.append(result)
    return result_list

result_list = Lagrange(point, depth, point)
long = len(point)
for i in range(long):
    a = abs(result_list[i] - depth[i])
    b = a/depth[i] * 100
    print('节点{i}的预测深度为:{depth}，绝对误差为{a}，相对误差为{b}%'.format(i=i, depth=result_list[i], a=a, b=b))

depth_draw = Lagrange(point, depth, point_draw)

plt.plot(point_draw, depth_draw)

'''画散点图'''
plt.scatter(point, result_list, c='r', marker='o')

plt.xlabel('point')
plt.ylabel('depth/m')
plt.show()

# result_list = Lagrange(time, temperature, time)
# long = len(time)
# for i in range(long):
#     a = abs(result_list[i] - temperature[i])
#     b = a/temperature[i] * 100
#     print('时间{i}的预测温度为:{depth}，绝对误差为{a}，相对误差为{b}%'.format(i=i, depth=result_list[i], a=a, b=b))
#
# temperature_draw = Lagrange(time, temperature, time_draw)
#
# plt.plot(time_draw, temperature_draw)
#
# '''画散点图'''
# plt.scatter(time, result_list, c='r', marker='o')
#
# plt.xlabel('time')
# plt.ylabel('temperature/C')
plt.show()


