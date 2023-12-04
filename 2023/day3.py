#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


# def part1v2():
#     part_numbers = []
#
#     for idx, line in enumerate(lines):
#         for match in re.finditer(r'\d+', line):
#             print(match)
#             span = match.span() if match is not None else None
#             print(line)
#             print(match, span)
#
#             # check left and right
#             x_start, x_end = span[0], span[1]
#             if (span[0] != 0 and line[x_start - 1] != '.') or (span[1] > len(line) and line[x_end + 1] != '.'):
#                 part_numbers.append(int(match.group()))
#                 break
#
#             # check line above and below
#             substring_check_above = lines[idx - 1][span[0]: span[1] + 1]
#             substring_check_below = lines[idx + 1][span[0]: span[1] + 1]
#             if (not all(substring_check_above.isdigit() or substring_check_above == '.')) \
#                     or not all(substring_check_below.isdigit() or substring_check_below == '.'):
#                 # it has special characters
#                 part_numbers.append(int(match.group()))
#                 break



    return False


def part1():
    special_coordinates, coordinates, part_numbers = [], [], []

    # register coordinates of special characters
    for index_line, line in enumerate(lines):
        for index_col, char in enumerate(line):
            if not char.isdigit() and char != '.':  # special_characters:
                coordinates.append(index_line)
                coordinates.append(index_col)
                special_coordinates.append(coordinates)
                coordinates = []

    # for each pair of coordinates of a special character, check in every side possible for a number
    for coordinates in special_coordinates:
        # check up
        x, y = coordinates[0] - 1, coordinates[1]
        check_sides_and_diagonals(x, y, lines, part_numbers, side='up')

        # check down
        x, y = coordinates[0] + 1, coordinates[1]
        check_sides_and_diagonals(x, y, lines, part_numbers, side='down')

        # check left
        x, y = coordinates[0], coordinates[1] - 1
        check_sides_and_diagonals(x, y, lines, part_numbers, side='left')

        # check right
        x, y = coordinates[0], coordinates[1] + 1
        check_sides_and_diagonals(x, y, lines, part_numbers, side='right')

    return sum(part_numbers)


def part2():
    gear_numbers, gear_ratios = [], []
    for index_line, line in enumerate(lines):
        for index_col, char in enumerate(line):
            if char == '*':
                part_numbers = get_part_numbers([index_line, index_col])
                if len(part_numbers) == 2:
                    print('It\'s a gear')
                    gear_ratios.append(np.prod(part_numbers))

    return sum(gear_ratios)


def get_part_numbers(coordinates):
    part_numbers = []

    # check up
    x, y = coordinates[0] - 1, coordinates[1]
    check_sides_and_diagonals(x, y, lines, part_numbers, side='up')

    # check down
    x, y = coordinates[0] + 1, coordinates[1]
    check_sides_and_diagonals(x, y, lines, part_numbers, side='down')

    # check left
    x, y = coordinates[0], coordinates[1] - 1
    check_sides_and_diagonals(x, y, lines, part_numbers, side='left')

    # check right
    x, y = coordinates[0], coordinates[1] + 1
    check_sides_and_diagonals(x, y, lines, part_numbers, side='right')

    return part_numbers


def check_sides_and_diagonals(x, y, lines, part_numbers, side):
    if lines[x][y] != '.':
        number = get_number(x, y)
        part_numbers.append(int(number))
        print(number)
    else:
        # check diagonal left
        if lines[x][y - 1] != '.' and side in ['up', 'down']:
            number = get_number(x, y - 1)
            part_numbers.append(int(number))
            print(number)
        # check diagonal right
        if lines[x][y + 1] != '.' and side in ['up', 'down']:
            number = get_number(x, y + 1)
            part_numbers.append(int(number))
            print(number)


def get_number(line, col):
    """
    get the number that is adjacent to a special character
    @param line: line coordinate
    @param col: column coordinate
    @return: return the shole number
    """
    start = search_number(col=col, string_line=lines[line], direction='left')
    end = search_number(col=col, string_line=lines[line], direction='the other way')

    number = lines[line][start:end + 1]

    return number


def search_number(col, string_line, direction):
    """
    search for the start or end positions of a number by searching until it meets a period
    @param col: column coordinate
    @param string_line: whole string of that line
    @param direction: search for left or right
    @return: return position of the first or last digit
    """
    i = -1 if direction == 'left' else 1
    j = i

    while True:
        position = col + j
        if position >= len(string_line) or (position < len(string_line) and not string_line[position].isdigit()):
            final_position = position - i
            break
        j += i

    return final_position


result = part1v2()
print(result)

