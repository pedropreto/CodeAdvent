#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re


file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    start_coordinates = [0, 0]
    start_node = lines[start_coordinates[0]][start_coordinates[1]]
    print(start_node)


    return False


def make_step(coordinates, path):
    return True

result = part1()
print(result)

