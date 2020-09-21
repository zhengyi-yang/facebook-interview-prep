#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 00:54:20 2020

@author: zhengyi

https://www.hackerrank.com/challenges/qheap1/problem
"""


class QHeap:
    def __init__(self):
        self.heap = []
        self.deleted = set()  # allowing lazy deletion

    def insert(self, val):
        if val in self.deleted:
            self.deleted.remove(val)
            return

        self.heap.append(val)

        i = len(self.heap)-1
        while (i-1)//2 >= 0:
            if self.heap[(i-1)//2] > self.heap[i]:
                self.heap[(i-1) //
                          2], self.heap[i] = self.heap[i], self.heap[(i-1)//2]
                i = (i-1)//2
            else:
                break

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        del self.heap[-1]

        i = 0

        while 2*i+1 < len(self.heap):
            left = 2*i+1
            right = left + 1

            if right >= len(self.heap):
                j = left
            elif self.heap[left] < self.heap[right]:
                j = left
            else:
                j = right

            if self.heap[i] < self.heap[j]:
                break

            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

    def delete(self, val):
        self.deleted.add(val)

    def find_min(self):
        heap_min = self.heap[0]

        while heap_min in self.deleted:
            self.pop()
            self.deleted.remove(heap_min)
            heap_min = self.heap[0]

        return heap_min


if __name__ == '__main__':
    t = int(input())
    heap = QHeap()

    for _ in range(t):
        q = input().strip().split()
        if q[0] == '1':
            val = int(q[1])
            heap.insert(val)
        elif q[0] == '2':
            val = int(q[1])
            heap.delete(val)
        else:
            print(heap.find_min())
