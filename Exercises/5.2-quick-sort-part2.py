#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 00:10:17 2020

@author: zhengyi

https://www.hackerrank.com/challenges/quicksort2/problem
"""


def partition(arr):
    pivot = arr[0]

    left = []
    equal = []
    right = []

    for i in arr:
        if i == pivot:
            equal.append(i)
        elif i < pivot:
            left.append(i)
        else:
            right.append(i)

    return left, equal, right


def quickSort(arr):
    if len(arr) <= 1:
        return arr

    left, equal, right = partition(arr)
    result = quickSort(left) + equal + quickSort(right)
    print(' '.join(map(str, result)))

    return result


if __name__ == '__main__':
    _t = int(input())
    l = list(map(int, input().strip().split()))
    _result = quickSort(l)
