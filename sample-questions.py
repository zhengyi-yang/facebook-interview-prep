#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 01:05:21 2020

@author: zhengyi

https://www.facebook.com/careers/life/sample_interview_questions
"""


from itertools import cycle


def spiral(n):
    if not type(n) is int:
        raise TypeError('n must be int')

    if n <= 0:
        raise ValueError('n must be >0')

    matrix = [[0] * n for _ in range(n)]
    i = 0
    j = 0
    value = 1

    # init first element
    matrix[i][j] = value
    value += 1

    directions = {'r': lambda i, j: (i, j+1),  # right
                  'd': lambda i, j: (i+1, j),  # down
                  'l': lambda i, j: (i, j-1),  # left
                  'u': lambda i, j: (i-1, j)}  # up

    direction_iter = cycle('rdlu')
    curr_direction = next(direction_iter)

    while value <= n*n:
        direction_f = directions[curr_direction]
        new_i, new_j = direction_f(i, j)

        if 0 <= new_i < n and 0 <= new_j < n and matrix[new_i][new_j] == 0:
            i, j = new_i, new_j
            matrix[i][j] = value
            value += 1
        else:
            curr_direction = next(direction_iter)

    return matrix


def look_and_say_seq(n):
    if not type(n) is int:
        raise TypeError('n must be int')

    if n <= 0:
        raise ValueError('n must be >0')

    value = '1'
    print(value)

    for _ in range(n-1):
        prev_digit = value[0]
        count = 1
        new_value = []

        for digit in value[1:]:
            if digit == prev_digit:
                count += 1
            else:
                new_value.append('{}{}'.format(count, prev_digit))
                prev_digit = digit
                count = 1

        new_value.append('{}{}'.format(count, prev_digit))
        value = ''.join(new_value)
        print(value)


def one_edit_apart(s1, s2):
    if not (isinstance(s1, str) and isinstance(s2, str)):
        raise TypeError('s1 and s2 must be str')

    if len(s1) > len(s2):
        s1, s2 = s2, s1  # force len(s1)<len(s2)

    if len(s2)-len(s1) > 1:
        return False

    for i, (a, b) in enumerate(zip(s1, s2)):
        if a != b:
            if len(s1) == len(s2):
                return s1[i+1:] == s2[i+1]
            else:
                return s1[i:] == s2[i+1:]

    return True
