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

    expanded_one_way = add_row(lines, transposed=False)
    expanded_data = add_row(expanded_one_way, transposed=True)

    for line in expanded_data:
        print(line)

    galaxy_positions = check_galaxies(expanded_data)

    final_distance = 0
    for i in range(len(galaxy_positions)):
        for j in range(i + 1, len(galaxy_positions)):
            point1 = galaxy_positions[i]
            point2 = galaxy_positions[j]
            distance = manhattan_distance(point1, point2)
            final_distance += distance
            print(f"Distance between {point1} and {point2}: {distance}")

    return final_distance


def part2():

    expanded_rows = check_empty_row(lines, transposed=False)
    expanded_columns = check_empty_row(lines, transposed=True)

    galaxy_positions = check_galaxies(lines)

    final_distance = 0
    for i in range(len(galaxy_positions)):
        for j in range(i + 1, len(galaxy_positions)):
            point1 = galaxy_positions[i]
            point2 = galaxy_positions[j]

            sum_distance = check_expansion_distance(point1, point2, expanded_rows, expanded_columns, expansion_size=1000000)

            distance = manhattan_distance(point1, point2) + sum_distance
            final_distance += distance
            print(f"Distance between {point1} and {point2}: {distance}")

    return final_distance


def check_expansion_distance(point1, point2, expanded_rows, expanded_columns, expansion_size):
    sum_distance = 0

    sorted_tuple = sorted([point1, point2], key=lambda x: x[0])
    for empty_row in expanded_rows:
        if sorted_tuple[0][0] < empty_row < sorted_tuple[1][0]:
            sum_distance += expansion_size - 1

    sorted_tuple = sorted([point1, point2], key=lambda x: x[1])
    for empty_column in expanded_columns:
        if sorted_tuple[0][1] < empty_column < sorted_tuple[1][1]:
            sum_distance += expansion_size - 1

    return sum_distance


def check_galaxies(array):
    galaxy_positions = []
    for i, row in enumerate(array):
        for j, char in enumerate(row):
            if char == '#':
                galaxy_positions.append((i, j))

    return galaxy_positions


def check_empty_row(array, transposed):
    if transposed:
        array = [list(row) for row in zip(*array)]
        array = [''.join(row) for row in array]

    idx_array = []
    for idx, line in enumerate(array):
        if '#' not in line:
            idx_array.append(idx)

    return idx_array


def add_row(array, transposed):
    if transposed:
        array = [list(row) for row in zip(*array)]
        array = [''.join(row) for row in array]

    end_array = []
    for line in array:
        end_array.append(line)
        if '#' not in line:
            end_array.append(line)

    if transposed:
        end_array = [list(row) for row in zip(*end_array)]
        end_array = [''.join(row) for row in end_array]

    return end_array


def manhattan_distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    distance = abs(x2 - x1) + abs(y2 - y1)
    return distance


result = part2()
print(result)

