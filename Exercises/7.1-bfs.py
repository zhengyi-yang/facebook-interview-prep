#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 22 17:45:45 2020

@author: zhengyi

https://www.hackerrank.com/challenges/bfsshortreach/problem
"""


from collections import deque


class Node:

    def __init__(self, nid):
        self.nid = nid
        self.neighbors = []

    def get_id(self):
        return self.nid

    def add_neighbor(self, nid):
        self.neighbors.append(nid)

    def get_neighbors(self):
        return self.neighbors


class UnGraph:

    def __init__(self):
        self.nodes = {}

    def add_node(self, nid):
        node = Node(nid)
        self.nodes[nid] = node

    def add_edge(self, src, dst):
        self.nodes[src].add_neighbor(dst)
        self.nodes[dst].add_neighbor(src)

    def get_node(self, nid):
        return self.nodes[nid]


def bfs(n, m, edges, s):
    G = UnGraph()
    for nid in range(1, n+1):
        G.add_node(nid)

    for (src, dst) in edges:
        G.add_edge(src, dst)

    queue = deque()
    queue.append(s)

    distances = [0 if i == s else -1 for i in range(1, n+1)]
    visited = set()
    visited.add(s)

    while queue:
        nid = queue.popleft()
        node = G.get_node(nid)
        neighbors = node.get_neighbors()

        distance = distances[nid-1]

        for neighbor in neighbors:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distances[neighbor-1] = distance+1

    results = [6*d if d != -1 else -1 for d in distances if d != 0]

    return results
