#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path, "r") as f:
    matrix = [line.strip().split() for line in f]  # takes the \n

ops = {
    '+': sum,
    '*': math.prod,
}

def apply_operation(operator, numbers):
    return ops[operator](numbers)


def part1():
    results = []
    # Transpose the matrix
    transpose = list(map(list, zip(*matrix)))

    for row in transpose:
        operator = row[-1]
        result = apply_operation(operator, [int(d) for d in row if d not in ops.keys()])
        results.append(result)

    return sum(results)



result = part1()
print(result)