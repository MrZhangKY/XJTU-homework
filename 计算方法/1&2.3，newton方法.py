#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/14 20:47'
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


def newton(x_list, y_list, variable_list):
    result_list = []
    long = len(x_list)
    n = long - 1
    k_array = np.arange(1, n, 1)

    '''为了不改变原参数'''
    y_list_copy = []
    for i in y_list:
        y_list_copy.append(i)

    '''求系数'''
    for k in k_array:
        i_array = np.arange(k, n, 1)[::-1]
        for i in i_array:
            y_list_copy[i] = (y_list_copy[i] - y_list_copy[i-1]) / (x_list[i] - x_list[i-k])

    i_array = np.arange(0, n-1, 1)[::-1]
    for variable in variable_list:
        result = y_list_copy[n]
        for i in i_array:
            result = result * (variable - x_list[i]) + y_list_copy[i]
        result_list.append(result)

    return result_list


def compute(x_list, y_list, variable_list1, variable_list2, name1, name2):
    '''
    x_list, y_list 计算系数用
    variable_list1 预测用，与x_list一致
    variable_list2 绘图用
    name1, name2 横纵坐标名称
    '''
    result_list = newton(x_list, y_list, variable_list1)
    draw_list = newton(x_list, y_list, variable_list2)

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


#compute(point, depth, point, point_draw, 'point', 'depth/m')
compute(time, temperature, time, time_draw, 'time', 'temperature/C')
