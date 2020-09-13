#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 13 15:50:48 2020

@author: zhengyi

https://www.hackerrank.com/challenges/queue-using-two-stacks/problem
"""


# Enter your code here. Read input from STDIN. Print output to STDOUT
class QueueTwoStacks:
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        self._fill_out_stack()
        if not self.out_stack:
            raise IndexError("Can't dequeue from an empty queue")

        return self.out_stack.pop()

    def peek(self):
        self._fill_out_stack()
        if not self.out_stack:
            raise IndexError("Can't peek from an empty queue")

        return self.out_stack[-1]

    def _fill_out_stack(self):
        if not self.out_stack:
            # Move items from in_stack to out_stack, reversing order
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())


if __name__ == '__main__':
    t = int(input())
    queue = QueueTwoStacks()

    for _ in range(t):
        q = input().strip().split()
        if q[0] == '1':
            value = int(q[1])
            queue.enqueue(value)
        elif q[0] == '2':
            queue.dequeue()
        else:
            print(queue.peek())
