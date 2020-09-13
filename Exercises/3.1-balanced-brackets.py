#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 15:15:08 2020

@author: zhengyi

https://www.hackerrank.com/challenges/balanced-brackets/problem
"""


def isBalanced(s):
    stack = []

    brackets = {')':'(',']':'[','}':'{'}

    for c in s:
        if c in brackets:
            if len(stack)==0 or stack.pop() != brackets[c]:
                return 'NO'
        else:
            stack.append(c)
    
    return 'YES' if len(stack)==0 else 'NO'
