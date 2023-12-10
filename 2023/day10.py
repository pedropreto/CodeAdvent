#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re

start = time.time() * 1000

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    # referencial is y (row) positive down and x (column) positive to the right

    col, row = findCharacter(lines, 'S')
    distance_traveled = 0
    first_direction, next_direction = get_first_direction([row, col])
    add_row, add_col = first_direction
    new_coordinates = [row + add_row, col + add_col]

    while lines[new_coordinates[0]][new_coordinates[1]] != 'S':

        new_coordinates, distance_traveled, next_direction = \
            get_next_coordinate([new_coordinates[0], new_coordinates[1]], next_direction, distance_traveled)

        print(new_coordinates)

    return math.ceil(float(distance_traveled) / 2)


def get_first_direction(coordinate):
    pipe_dict = {"|": [[1, 0], [-1, 0]], "-": [[0, 1], [0, -1]], "L": [[-1, 0], [0, 1]], "J": [[-1, 0], [0, -1]],
                 "7": [[1, 0], [0, -1]], "F": [[1, 0], [0, 1]]}

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    row, col = coordinate
    found_direction = False
    for i, j in directions:
        if found_direction:
            break
        char = lines[row + i][col + j]
        if char in pipe_dict.keys():
            next_end = get_next_end([i, j], char, pipe_dict)
            if not next_end:
                continue
            return [i, j], next_end


def get_next_coordinate(coordinate, direction, distance_traveled):
    row, col = coordinate
    pipe_dict = {"|": [[1, 0], [-1, 0]], "-": [[0, 1], [0, -1]], "L": [[-1, 0], [0, 1]], "J": [[-1, 0], [0, -1]],
                 "7": [[1, 0], [0, -1]], "F": [[1, 0], [0, 1]]}

    if direction is None:  # direction is not know, we need to find it out, starting point is S
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        found_direction = False
        for i, j in directions:
            if found_direction:
                break
            char = lines[row + i][col + j]
            if char in pipe_dict.keys():
                next_end = get_next_end([i, j], char, pipe_dict)
                if not next_end:
                    continue
                add_row, add_col = i, j

    else:
        add_row, add_col = direction
        next_char = lines[row+add_row][col+add_col]
        next_end = get_next_end(direction, next_char, pipe_dict)

    new_coordinate = [row + add_row, col + add_col]
    distance_traveled += 1
    # print(new_coordinate)

    # new_coordinate = get_next_coordinate(new_coordinate, next_end, distance_traveled)

    return new_coordinate, distance_traveled, next_end


def get_next_end(from_direction, char, pipe_dict):

    i, j = from_direction
    if char not in pipe_dict.keys():
        return False
    for idx, end in enumerate(pipe_dict[char]):
        if [-i, -j] == end:
            ends = list(pipe_dict[char])
            ends.pop(idx)
            next_end = ends[0]
            return next_end
    return False


def findCharacter(strings, char):
    # Loop through all rows and columns
    for i, s in enumerate(strings):
        if char in s:
            j = s.index(char)
            return j, i


result = part1()
print(result)
