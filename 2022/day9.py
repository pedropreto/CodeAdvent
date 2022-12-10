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
    head_position = [0, 0]
    tail_position = [0, 0]
    tail_positions = []
    inputs = {"U": [0, 1], "D": [0, -1], "R": [1,0], "L": [-1, 0]}

    for l in lines:
        l = l.split()
        for z in range(0, int(l[1])):
            head_position[0] += inputs[l[0]][0]
            head_position[1] += inputs[l[0]][1]

            coordinate_dif = [head_position[0] - tail_position[0], head_position[1] - tail_position[1]]

            distance = math.sqrt(coordinate_dif[0] ** 2 + coordinate_dif[1] ** 2)
            if coordinate_dif[0] != 0 and distance > math.sqrt(2):  # moves x
                tail_position[0] += 1 if coordinate_dif[0] > 0 else -1
            if coordinate_dif[1] != 0 and distance > math.sqrt(2):  # moves y
                tail_position[1] += 1 if coordinate_dif[1] > 0 else -1

            tail_positions.append(list(tail_position))

    tail_positions_unique = [list(x) for x in set(tuple(x) for x in tail_positions)]

    return len(tail_positions_unique)


def part2():
    head_position = [0, 0]
    rope_size = 9
    positions = [[list(head_position)]] + [[[0,0]] for p in range(0, rope_size)]
    inputs = {"U": [0, 1], "D": [0, -1], "R": [1,0], "L": [-1, 0]}
    for l in lines:
        l = l.split()
        for z in range(0, int(l[1])):
            head_position[0] += inputs[l[0]][0]
            head_position[1] += inputs[l[0]][1]
            positions[0].append(list(head_position))

            for k in range(0, rope_size):
                trail_position = movement(positions[k][-1], positions[k + 1][-1])
                positions[k + 1].append(list(trail_position))

    tail_positions_unique = [list(x) for x in set(tuple(x) for x in positions[-1])]

    return len(tail_positions_unique)


def movement(lead_position, trail_position):

    coordinate_dif = [lead_position[0] - trail_position[0], lead_position[1] - trail_position[1]]

    distance = math.sqrt(coordinate_dif[0] ** 2 + coordinate_dif[1] ** 2)
    if coordinate_dif[0] != 0 and distance > math.sqrt(2):  # moves x
        trail_position[0] += 1 if coordinate_dif[0] > 0 else -1
    if coordinate_dif[1] != 0 and distance > math.sqrt(2):  # moves y
        trail_position[1] += 1 if coordinate_dif[1] > 0 else -1

    return trail_position


result = part2()
print(result)



