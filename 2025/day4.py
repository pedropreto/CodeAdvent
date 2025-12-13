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
    lines = [list(line.rstrip()) for line in f]



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


def count_roll_removing():
    rows = len(lines)
    cols = len(lines[0])
    count_rolls = 0
    removal_coordinates = []
    for i in range(cols):
        for j in range(rows):
            if lines[j][i] == '@':
                if is_accessible(j, i):
                    count_rolls += 1
                    # remove roll
                    removal_coordinates.append((j,i))

    return count_rolls, removal_coordinates


def replace_rolls(removal_coordinates):
    for coordinates in removal_coordinates:
        r, c = coordinates[0], coordinates[1]
        lines[r][c] = '.'


def part2():
    # If you need the lines back as strings:
    total_removals = 0
    count_rolls = 1
    while count_rolls > 0:
        count_rolls, removal_coordinates = count_roll_removing()
        replace_rolls(removal_coordinates)
        total_removals += count_rolls
        print(f'In this round we removed {count_rolls} and in total {total_removals}!')


    return total_removals




result = part2()
print(result)