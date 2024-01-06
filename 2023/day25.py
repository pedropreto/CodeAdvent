#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import networkx as nx

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    # minimum cut theory
    g = nx.Graph()

    for line in lines:
        left, right = line.split(":")
        for node in right.strip().split():
            g.add_edge(left, node)
            g.add_edge(node, left)

    g.remove_edges_from(nx.minimum_edge_cut(g))
    a, b = nx.connected_components(g)

    return len(a) * len(b)


result = part1()
print(result)

