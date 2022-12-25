#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import string
import numpy as np
import regex as re
from statistics import mean

py_name = os.path.basename(__file__)
file = "day" + re.findall(r'\d+', py_name)[0] + ".txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    cube_list = []
    sides_free = []
    for l in lines:
        cube = re.findall('[0-9]+', l)
        cube = [int(x) for x in cube]
        cube_list.append(cube)
        sides_free.append(6)

    print(cube_list)

    for idx, cube in enumerate(cube_list):
        for i in range(idx, len(cube_list)):
        #for loop_idx, cube_list[i in enumerate(cube_list):
            if cube_list[i][0] == cube[0] and cube_list[i][1] == cube[1] and abs(cube_list[i][2] - cube[2]) == 1\
                    or cube_list[i][0] == cube[0] and cube_list[i][2] == cube[2] and abs(cube_list[i][1] - cube[1]) == 1\
                    or cube_list[i][1] == cube[1] and cube_list[i][2] == cube[2] and abs(cube_list[i][0] - cube[0]) == 1:
                sides_free[i] -= 1
                sides_free[idx] -= 1

        sum_sides_free = sum(sides_free)


    return sum_sides_free


def part2():

    return 1


result = part1()
print(result)
