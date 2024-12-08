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
    row_size = len(lines)
    col_size = len(lines[0])
    antenna_positions = {}
    global_antenna_positions = []

    # get all the positions for the antennas
    for i, line in enumerate(lines):
        for j, node in enumerate(line):
            if node != '.':
                antenna_positions[node] = antenna_positions.get(node, []) + [(i , j)]
                global_antenna_positions.append((i, j))
    print(antenna_positions)

    infinite_mode = False

    if infinite_mode:
        antinodes = calculate_antinodes(antenna_positions, infinite_mode = infinite_mode)
        antinodes_in_antennas = [item for item in antinodes if item in global_antenna_positions]
        extra_nodes = len(global_antenna_positions) - len(set(antinodes_in_antennas))
    else:
        antinodes = calculate_antinodes(antenna_positions, infinite_mode=infinite_mode)
        extra_nodes = 0

    # filter antinodes out of bounds
    antinodes = [point for point in antinodes if row_size > point[0] >= 0 and col_size > point[1] >= 0]

    antinodes = sorted(antinodes, key=lambda x: (x[0], x[1]))

    print(f'Number of unique antinodes: {len(set(antinodes))}')
    print(f'Number of extra nodes: {extra_nodes}')

    return len(set(antinodes)) + extra_nodes

def part2():
    row_size = len(lines)
    col_size = len(lines[0])
    antenna_positions = {}
    global_antenna_positions = []

    # get all the positions for the antennas
    for i, line in enumerate(lines):
        for j, node in enumerate(line):
            if node != '.':
                antenna_positions[node] = antenna_positions.get(node, []) + [(i , j)]
                global_antenna_positions.append((i, j))
    print(antenna_positions)

    infinite_mode = True

    if infinite_mode:
        antinodes = calculate_antinodes(antenna_positions, infinite_mode = infinite_mode)
        antinodes_in_antennas = [item for item in antinodes if item in global_antenna_positions]
        extra_nodes = len(global_antenna_positions) - len(set(antinodes_in_antennas))
    else:
        antinodes = calculate_antinodes(antenna_positions, infinite_mode=infinite_mode)
        extra_nodes = 0

    # filter antinodes out of bounds
    antinodes = [point for point in antinodes if row_size > point[0] >= 0 and col_size > point[1] >= 0]

    antinodes = sorted(antinodes, key=lambda x: (x[0], x[1]))

    print(f'Number of unique antinodes: {len(set(antinodes))}')
    print(f'Number of extra nodes: {extra_nodes}')

    return len(set(antinodes)) + extra_nodes

def calculate_antinodes(antenna_positions, infinite_mode):
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
                print(f'The col diff between {positions[i]} and {positions[j]} is {column_diff}')

                antinodes = add_antinodes(row_diff, column_diff, i, positions, antinodes, 1, infinite_mode)
                antinodes = add_antinodes(row_diff, column_diff, j, positions, antinodes, -1, infinite_mode)

                print(f'\n')

    return antinodes


def add_antinodes(row_diff, column_diff, idx, positions, antinodes, step, infinite_mode=False):
    row_coordinate = positions[idx][0]
    col_coordinate = positions[idx][1]
    row_size = len(lines)
    col_size = len(lines[0])
    while row_size > row_coordinate >= 0 and col_size > col_coordinate >= 0:
        row_coordinate += row_diff * step
        col_coordinate += column_diff * step
        print(f'Antinode is {(row_coordinate, col_coordinate)}')
        antinodes.append((row_coordinate, col_coordinate))
        if not infinite_mode:
            break



    return antinodes

result = part1()
print(result)