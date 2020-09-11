#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 02:24:36 2020

@author: zhengyi

https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""


def rotLeft(a, d):
    d = d % len(a)
    return (a*2)[d:d+len(a)]
