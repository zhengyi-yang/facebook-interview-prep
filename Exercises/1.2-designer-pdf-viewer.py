#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 02:04:36 2020

@author: zhengyi

https://www.hackerrank.com/challenges/designer-pdf-viewer/problem
"""


def designerPdfViewer(h, word):
    h_dict = dict(zip(range(0, 26), h))
    tallest = max(h_dict[ord(l)-ord('a')] for l in word)
    return tallest*len(word)
