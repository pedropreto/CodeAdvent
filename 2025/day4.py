#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path, "r") as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def is_accessible(row, column):
    rows = len(lines)
    cols = len(lines[0])
    target = '@'
    target_number = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

    for dr, dc in directions:
        nr, nc = row + dr, column + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            if lines[nr][nc] == target:
                target_number += 1

    if target_number < 4:
        print(f'In row {row} and column {column} there is a roll of paper accessible by fork!')
        return True

    return False


def part1():
    rows = len(lines)
    cols = len(lines[0])
    count_rolls = 0
    for i in range(cols):
        for j in range(rows):
            if lines[j][i] == '@':
                count_rolls += is_accessible(j, i)

    return count_rolls




result = part1()
print(result)