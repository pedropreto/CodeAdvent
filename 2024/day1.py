#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# reads it directly into numpy
data = np.loadtxt(file_path)
left_list, right_list = data[:, 0].tolist(), data[:, 1].tolist()

def part1():
    final_number = 0
    left_list.sort()
    right_list.sort()
    for i in range(0, len(left_list)):
        final_number += abs(left_list[i] - right_list[i])
    return final_number

def part2():
    final_score = 0
    for i in left_list:
        final_score += right_list.count(i) * i

    return final_score


result = part1()
print(result)

