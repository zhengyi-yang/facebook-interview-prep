#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 00:46:11 2020

@author: zhengyi

https://www.hackerrank.com/challenges/the-quickest-way-up/problem
"""


from collections import deque


def quickestWayUp(ladders, snakes):
    ladders = dict(ladders)
    snakes = dict(snakes)

    queue = deque()
    queue.append((1, 0))

    visited = set()
    visited.add(1)

    while queue:
        n, d = queue.popleft()
        for i in range(1, 7):
            m = n+i
            if m in ladders:
                m = ladders[m]
            elif m in snakes:
                m = snakes[m]

            if m == 100:
                return d+1
            elif m < 100 and m not in visited:
                visited.add(m)
                queue.append((m, d+1))

    return -1
