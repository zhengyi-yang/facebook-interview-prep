#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 13:28:09 2020

@author: zhengyi

https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new = Node(val)

        if self.root is None:
            self.root = new
        else:
            node = self.root
            while True:
                if val < node.info:
                    if node.left is None:
                        node.left = new
                        break
                    else:
                        node = node.left
                elif val > node.info:
                    if node.right is None:
                        node.right = new
                        break
                    else:
                        node = node.right
                else:
                    break

        return self.root


def height(root):
    if root is None:
        return -1

    return max(height(root.left), height(root.right))+1
