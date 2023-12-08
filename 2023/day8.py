#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np

start = time.time() * 1000

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    instructions = lines[0]
    nodes, next_steps = [], []

    for line in lines[2:]:
        node, substring = line.split(' = ')
        next_step = re.findall(r'\w+', substring)
        nodes.append(node), next_steps.append(next_step)

    n_instructions = 0
    i = 0
    node = 'AAA'
    idx = nodes.index(node)

    while True:

        node = next_steps[idx][1] if instructions[i] == 'R'else next_steps[idx][0]
        idx = nodes.index(node)
        n_instructions += 1
        if node == 'ZZZ':
            break

        i = 0 if i == len(instructions) - 1 else i + 1

    return n_instructions


result = part1()
print(result)