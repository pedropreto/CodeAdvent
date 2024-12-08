#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    pattern = r"\d+"
    safe_reports = 0
    for line in lines:
        levels = re.findall(pattern, line)

        if check_safe(levels):
            safe_reports += 1

    return safe_reports


def part2():
    pattern = r"\d+"
    safe_reports = 0
    for line in lines:
        levels = re.findall(pattern, line)

        if check_safe(levels):
            safe_reports += 1
        else:
            # brute force remove 1 by 1
            for i in range(0, len(levels)):
                levels_copy = list(levels)
                del levels_copy[i]
                if check_safe(levels_copy):
                    safe_reports += 1
                    break

    return safe_reports



def check_safe(levels):
    dif_lst = []
    for i in range(0, len(levels) - 1):
        dif_lst.append(int(levels[i]) - int(levels[i + 1]))

    positive_count = negative_count = zeros = overslope = 0

    for num in dif_lst:
        positive_count += num > 0
        negative_count += num < 0
        zeros += num == 0
        overslope += abs(num) > 3

    if (positive_count > 0 and negative_count > 0) or zeros > 0 or overslope > 0:
        return False

    return True

result = part2()
print(result)

