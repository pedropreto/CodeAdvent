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
    antenna_positions = {}
    global_antenna_positions = []
    row_size = len(lines)
    col_size = len(lines[0])
    # get all the positions for the antennas
    for i, line in enumerate(lines):
        for j, node in enumerate(line):
            if node != '.':
                antenna_positions[node] = antenna_positions.get(node, []) + [(i , j)]
                global_antenna_positions.append((i, j))
    print(antenna_positions)

    antinodes = []
    keys = antenna_positions.keys()
    for key in keys:
        positions = antenna_positions[key]
        print(f'Calculating for antenna {key}')
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                row_diff = positions[i][0] - positions[j][0]
                column_diff = positions[i][1] - positions[j][1]
                print(f'The row diff between {positions[i]} and {positions[j]} is {row_diff}')
                print(f'The col diff between {positions[i]} and {positions[j]} is {column_diff}\n')

                antinodes.append((positions[i][0] + row_diff, positions[i][1] + column_diff))
                antinodes.append((positions[j][0] - row_diff, positions[j][1] - column_diff))

    # filter antinodes out of bounds
    antinodes = [point for point in antinodes if row_size > point[0] >= 0 and col_size > point[1] >= 0]


    print(antinodes)

    return len(set(antinodes))


result = part1()
print(result)