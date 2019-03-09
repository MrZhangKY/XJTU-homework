#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/29 21:52'
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
import math

author = '张开宇'
time = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
print('作者：{author}，日期：{date}'.format(author=author, date=time))

point_draw = np.arange(0, 20.01, 0.01)
time_draw = np.arange(0, 24.01, 0.01)

point = []
for i in range(21):
    point.append(i)
depth = [9.01, 8.96, 7.96, 7.97, 8.02, 9.05, 10.13, 11.18, 12.26, 13.28, 13.32, 12.61, 11.29, 10.22,
         9.15, 7.90, 7.95, 8.86, 9.81, 10.80, 10.93]

time = []
for i in range(25):
    time.append(i)
temperature = [15, 14, 14, 14, 14, 15, 16, 18,
               20, 20, 23, 25, 28, 31, 34, 31,
               29, 27, 25, 24, 22, 20, 18, 17, 16]

def compute_G(x_list, n):
    '''计算法方程系数矩阵'''
    coefficient_matrix = []
    for i in range(n+1):
        coefficient_list = []
        for j in x_list:
            coefficient_list.append(pow(j, i))
        coefficient_matrix.append(coefficient_list)
    coefficient_matrix = np.mat(coefficient_matrix)
    return coefficient_matrix

def least_square_method(x_list, y_list, n, variable_list):
    '''计算插值函数系数'''
    G = compute_G(x_list, n)
    GT = np.transpose(G)
    y_matrix = np.mat(y_list)

    coefficient_matrix = G * GT
    y_matrix = G * np.transpose(y_matrix)
    alpha = np.linalg.solve(np.array(coefficient_matrix), np.array(y_matrix))   #用array计算

    '''由插值函数系数及阶数计算插值结果'''
    result_list = []
    for i in variable_list:
        result = 0
        for j in range(n+1):
            result = result + alpha[j] * pow(i, j)
        result_list.append(result[0])
    return result_list

def compute(x_list, y_list, n, variable_list1, variable_list2, name1, name2):
    '''
    x_list, y_list 计算系数用
    variable_list1 预测用，与x_list一致
    variable_list2 绘图用
    name1, name2 横纵坐标名称
    '''
    result_list = least_square_method(x_list, y_list, n, variable_list1)
    draw_list = least_square_method(x_list, y_list, n, variable_list2)

    long = len(x_list)
    for i in range(long):
        a = abs(result_list[i] - y_list[i])
        b = a/y_list[i] * 100
        print('{x}{i}的预测值是：{result}，真实值是：{real}，绝对误差为{a}，相对误差为{b}%'.format(x=name1, i=i, real=y_list[i],
                                                                      result=result_list[i], a=a, b=b))
    '''画折线图'''
    plt.plot(variable_list2, draw_list)

    '''画散点图'''
    plt.scatter(x_list, result_list, c='r', marker='o')
    plt.scatter(x_list, y_list, c='b', marker='*')

    plt.xlabel(name1)
    plt.ylabel(name2)
    plt.show()

#compute(point, depth, 10, point, point_draw, 'point', 'depth/m')
#compute(time, temperature, 3, time, time_draw, 'time', 'temperature/C')

'''计算温度平均值'''
sum = temperature[2]+temperature[8]+temperature[14]+temperature[20]
print('平均气温为：{T}℃'.format(T=sum/4))
'''计算插值误差'''
result_list = least_square_method(time, temperature, 3, time)
E = 0
long = len(result_list)
for i in range(long):
    E = E+pow((result_list[i]-temperature[i]), 2)
E = math.sqrt(E)
print('最小二乘解的误差为：{E}'.format(E=E))
