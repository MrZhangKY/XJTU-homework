#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2018/12/28 21:37'
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

def tss(a, b, c, d):
    '''追赶法解三对角线性方程'''
    n = len(b)

    miu = []
    y = []
    x = []
    for i in range(n):
        x.append(0)

    miu.append(b[0])
    y.append(d[0])

    for i in range(1,n):
        l = a[i]/miu[i-1]
        miu.append(b[i]-l*c[i-1])
        y.append(d[i]-l*y[i-1])

    x[n-1] = y[n-1] / miu[n-1]

    for j in range(n-2,-1,-1):
        x[j] = (y[j] - c[j]*x[j+1]) / miu[j]

    return x

def splinem(x_list, y_list):
    '''自然三次样条'''
    variable = 0
    n = len(x_list)
    m = []
    h = []
    c = []
    a = []
    b = []

    for i in range(n):
        m.append(y_list[i])
        h.append(0)
        c.append(0)
        a.append(0)
        b.append(0)

    for k in range(1,3):
        for i in range(n-1, k-1, -1):
            m[i] = (m[i]-m[i-1]) / (x_list[i]-x_list[i-k])

    h[1] = x_list[1] - x_list[0]

    for i in range(1, n-1):
        h[i+1] = x_list[i+1] - x_list[i]
        c[i] = h[i+1] / (h[i]+h[i+1])
        a[i] = 1 - c[i]
        b[i] = 2
        m[i] = 6*m[i+1]

    m[0] = variable
    m[n-1] = variable
    c[0] = variable
    b[0] = 2
    a[n-1] = variable
    b[n-1] = 2

    return tss(a, b, c, m)

def findk(x_variable, x_list):
    k = 1
    n = len(x_list)

    for i in range(1, n-1):
        if x_variable <= x_list[i]:
            k = i
            break
        else:
            k = i+1

    return k

def evaspline(x_list, y_list, variable_list):
    m = splinem(x_list, y_list)
    result_list = []

    for i in variable_list:
        k = findk(i, x_list)
        h1 = x_list[k] - x_list[k-1]
        h2 = x_list[k] - i
        h3 = i - x_list[k-1]
        result_list.append((m[k-1]*h2*h2*h2/6 + m[k]*h3*h3*h3/6 + (y_list[k-1]-m[k-1]*h1*h1/6)*h2 + (y_list[k]-m[k]*h1*h1/6)*h3) / h1)

    return result_list

def compute(x_list, y_list, variable_list1, variable_list2, name1, name2):
    '''
    x_list, y_list 计算系数用
    variable_list1 预测用，与x_list一致
    variable_list2 绘图用
    name1, name2 横纵坐标名称
    '''
    result_list = evaspline(x_list, y_list, variable_list1)
    draw_list = evaspline(x_list, y_list, variable_list2)

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
#compute(time, temperature, time, time_draw, 'time', 'temperature/C')

def long_compute(x_list, y_list, variable_list):
    '''计算三次样条曲线的第一型线积分'''
    m = splinem(x_list, y_list)
    h = variable_list[1] - variable_list[0]
    long = 0
    for i in variable_list:
        k = findk(i, x_list)
        h1 = x_list[k] - x_list[k-1]
        h2 = x_list[k] - i
        h3 = i - x_list[k-1]
        derivative = -m[k-1]*h2*h2/2/h1 + m[k]*h3*h3/2/h1 + (y_list[k] - y_list[k-1])/h1 - (m[k]-m[k-1])/6*h1
        derivative_2 = math.sqrt(1 + derivative * derivative)
        long = long + derivative_2 * h
    return long

print('所需光缆的长度为：{long} m'.format(long = long_compute(point, depth, point_draw)))

