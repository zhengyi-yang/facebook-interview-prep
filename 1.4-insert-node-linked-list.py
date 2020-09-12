#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 16:18:26 2020

@author: zhengyi

https://www.hackerrank.com/challenges/insert-a-node-at-a-specific-position-in-a-linked-list/problem
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

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def insertNodeAtPosition(head, data, position):
    new_node = SinglyLinkedListNode(data)

    if position == 0:    
        new_node.next = head
        return new_node

    curr_node = head
    for _ in range(position-1):
        curr_node = curr_node.next
        
    new_node.next = curr_node.next
    curr_node.next = new_node

    return head
