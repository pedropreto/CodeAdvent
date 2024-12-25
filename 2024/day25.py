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
    nr_lines = 8
    width = 5
    locks = []
    keys = []
    sections = [lines[i:i + nr_lines - 1] for i in range(0, len(lines), nr_lines) if lines[i:i + nr_lines -1]]

    for element in sections:
        heights = []
        t_element =  [''.join(row) for row in zip(*element)]

        for pin in t_element:
            heights.append(pin.count("#") - 1)

        if element[0].count("#") == width:
            print('It is a lock!')
            locks.append(heights)
        else:
            print('It is a key!')
            keys.append(heights)

    pairs = 0

    for key in keys:
        for lock in locks:
            match_list = []
            for i in range(0, len(key)):
                match_list.append(key[i] + lock[i] <= 5)

            if all(match_list):
                pairs += 1

    return pairs

result = part1()
print(result)