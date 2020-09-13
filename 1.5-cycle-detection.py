#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:34:40 2020

@author: zhengyi

https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem
"""


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def has_cycle(head):
    slow = head  # travel one node at a time
    fast = head  # travel two nodes at a time

    while not(slow is None or slow.next is None or fast is None or fast.next is None):
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return 1

    return 0
