#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__author__ = '张开宇'
__time__ = '2019/1/12 14:28'
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
import math


def f(x):
    '''计算f(x)的值'''
    n = 100
    h = math.pi/n
    F = 0
    for i in range(1, n+1):
        F = h/2/math.pi*(math.cos(x*math.sin((i-1)*h))+math.cos(x*math.sin(i*h))) + F
    return F


def dichotomy(list, error):
    n = 0
    while abs(list[0]-list[1])>=error:
    #for i in range(70):
        middle = (list[0] + list[1])/2
        f1 = f(list[0])
        f_middle = f(middle)
        if f1*f_middle<0:
            list[1] = middle
        else:
            list[0] = middle
        n+=1
    print(abs(list[0]-list[1]))
    print(n)
    return list[0]

print('[2,3]之间非线性方程的根为：{x}'.format(x=dichotomy([2,3], pow(10,-15))))
