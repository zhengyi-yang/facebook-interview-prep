#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:58:43 2020

@author: zhengyi

https://www.hackerrank.com/challenges/insertionsort2/problem
"""


def insertionSort2(n, arr):
    for i in range(1, n):
        for j in range(i-1, -1, -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            else:
                break
        print(' '.join(map(str, arr)))
