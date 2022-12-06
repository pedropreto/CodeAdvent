#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import string
import numpy as np
import regex as re

py_name = os.path.basename(__file__)
file = "day" + re.findall(r'\d+', py_name)[0] + ".txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    marker_number, first_marker, input = 4, 0, lines[0]
    for i in range(marker_number, len(input)):
        x = input[i - marker_number:i]
        if len(set(x)) == len(x):
            first_marker = i
            break

    return first_marker


def part2():
    marker_number, first_marker, input = 14, 0, lines[0]
    for i in range(marker_number, len(input)):
        x = input[i - marker_number:i]
        if len(set(x)) == len(x):
            first_marker = i
            break

    return first_marker


def bothparts(char_in_a_row):
    marker_number, first_marker, input = char_in_a_row, 0, lines[0]
    for i in range(marker_number, len(input)):
        x = input[i - marker_number:i]
        if len(set(x)) == len(x):
            first_marker = i
            break

    return first_marker


count = part2()
print(count)

result_part1 = bothparts(char_in_a_row=4)
result_part2 = bothparts(char_in_a_row=14)

print(result_part1, result_part2)

