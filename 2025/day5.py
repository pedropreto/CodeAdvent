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
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def split_inputs(input):
    try:
        idx = input.index('')
    except ValueError:
        idx = len(input)
    return input[:idx], input[idx + 1:]


def part1():
    fresh = []
    intervals, ingredients = split_inputs(lines)

    for ingredient in ingredients:
        for interval in intervals:
            firstValue = int(interval.split('-')[0])
            lastValue = int(interval.split('-')[1])
            if firstValue <= int(ingredient) <= lastValue:
                fresh.append(int(ingredient))
                break

    return len(fresh)



result = part1()
print(result)