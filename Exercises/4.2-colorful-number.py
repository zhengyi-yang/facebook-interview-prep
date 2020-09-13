#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 16:59:50 2020

@author: zhengyi

https://algorithms.tutorialhorizon.com/colorful-numbers/


Objective: Given a number, find out whether its colorful or not.

Colorful Number: When in a given number, product of every digit of a sub-sequence are different. That number is called Colorful Number. See Example

Example:

Given Number : 3245
Output : Colorful
Number 3245 can be broken into parts like 3 2 4 5 32 24 45 324 245.
this number is a colorful number, since product of every digit of a sub-sequence are different.
That is, 3 2 4 5 (3*2)=6 (2*4)=8 (4*5)=20, (3*2*4)= 24 (2*4*5)= 40

Given Number : 326
Output : Not Colorful.
326 is not a colorful number as it generates 3 2 6 (3*2)=6 (2*6)=12.
Reference : http://www.careercup.com/question?id=4863869499473920
"""


from functools import reduce


def isColorfulNumber(n):
    digits = [int(d) for d in str(n)]
    products = set()

    for l in range(1, len(digits)+1):
        for start in range(len(digits)-l+1):
            sub_seq = digits[start:start+l]
            product = reduce((lambda x, y: x * y), sub_seq)

            if product in products:
                return False
            else:
                products.add(product)

    return True


if __name__ == '__main__':
    print(isColorfulNumber(3245))
    print(isColorfulNumber(326))
