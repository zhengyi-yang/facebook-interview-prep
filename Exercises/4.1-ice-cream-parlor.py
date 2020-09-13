#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 16:56:26 2020

@author: zhengyi

https://www.hackerrank.com/challenges/icecream-parlor/problem
"""


def icecreamParlor(m, arr):
    to_spend = {}

    for i, price in enumerate(arr):
        if price in to_spend:
            return (to_spend[price]+1, i+1)
        else:
            to_spend[m-price] = i
