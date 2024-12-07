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
    grid = lines
    initial_position = next((r, row.index('^')) for r, row in enumerate(grid) if '^' in row)
    # print(initial_position)
    coordinates = initial_position
    visited = [initial_position]
    rotations = 0
    while coordinates[0] != -1:
        coordinates, visited = move(coordinates, grid, visited, rotations)
        rotations += 1

    return len(set(visited))


def move(position, grid, visited, rotations):
# reference grid -> i represents the rows, j the columns, first row is i = 0 and first column j = 0
# going up means the i decreases with the original grid

    if rotations == 0 or rotations % 4 == 0:
        # goes up, i decreases
        position, visited = move_registering_original_coordinates(position, -1, 0, visited, grid)
    elif (rotations - 1) % 4 == 0:
        # goes right, j increases
        position, visited = move_registering_original_coordinates(position, 0, 1, visited, grid)
    elif (rotations - 2) % 4 == 0:
        # goes down, i increases
        position, visited = move_registering_original_coordinates(position, 1, 0, visited, grid)
    elif (rotations - 3) % 4 == 0:
        # goes left, j decreases
        position, visited = move_registering_original_coordinates(position, 0, -1, visited, grid)

    return position, visited


def move_registering_original_coordinates(position, step_i, step_j, visited, grid):
    # starting row
    i = position[0]
    # column
    j = position[1]
    while 0 <= i < len(grid) - 1 and 0 <= j < len(grid) - 1:
        if grid[i + step_i][j + step_j] == '#':
            return (i, j), visited
        else:
            i += step_i
            j += step_j
            visited.append((i, j))

    return (-1, -1), visited

result = part1()
print(result)

