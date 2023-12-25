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

    print(lines)

    blocks = []
    current_block = []

    # Iterate through the data
    for item in lines:
        if item == '':
            # Found the separator, start a new block
            blocks.append(current_block)
            current_block = []
        else:
            # Add the item to the current block
            current_block.append(item)

    # Add the last block (after the last separator, if any)
    blocks.append(current_block)


    print(blocks)
    lines_above, columns_left = 0, 0

    for idx, block in enumerate(blocks):
        print(f'idx of block {idx}')
        print(f'{block}')
        #print('\n')
        #for line in block:
         #   print(line)
        # check for possible mirrors on first line
        mirrors_column = check_possible_mirrors(block[0])

        end_mirror = check_end_mirror(block, mirrors_column)

        if not end_mirror:
            transposed_block = [''.join(row) for row in zip(*block)]
            for line in transposed_block:
                print(line)
            mirrors_row = check_possible_mirrors(transposed_block[0])
            end_mirror = check_end_mirror(transposed_block, mirrors_row)

            if not end_mirror:
                columns_left += 0
            else:
                print(f'The mirror row lies between row {end_mirror[0] + 1} and row {end_mirror[0] + 2}')
                lines_above += end_mirror[0] + 1
                print(f'Lines above: {end_mirror[0] + 1}')
                print(f'Total lines above: {lines_above}')
        else:

            print(f'The mirror column lies between column {end_mirror[0] + 1} and column {end_mirror[0] + 2}')
            columns_left += end_mirror[0] + 1
            print(f'Columns to the left: {end_mirror[0] + 1}')
            print(f'Total columns to the left: {columns_left}')

    return lines_above * 100 + columns_left


def check_end_mirror(array, mirrors):
    """
    Check if there is any mirror (just checks mirrors as columns
    To check row mirrors, use this function with transposed
    @return:
    """
    mirrors_to_keep = list(mirrors)
    for line in array[1:]:
        if len(mirrors_to_keep) == 0:
            return []
        for mirror in mirrors:
            if not is_mirror(line, mirror) and mirror in mirrors_to_keep:
                mirrors_to_keep.remove(mirror)

    return mirrors_to_keep


def is_mirror(string, idx_mirror):
    """
    @param string: string to evaluate
    @param idx_mirror: idx of string to mirror, if 5, mirror is between 5 and 6
    @return: boolean
    """
    inc = 0
    while True:
        if idx_mirror - inc < 0 or idx_mirror + 1 + inc >= len(string):
            break
        for_char = string[idx_mirror + 1 + inc]
        back_char = string[idx_mirror - inc]
        if for_char != back_char:
            # not a reflection
            return False
        inc += 1

    return True


def check_possible_mirrors(string):
    mirrors = []
    for i in range(0, len(string) - 1):
        # mirror is placed between i and i + 1
        if is_mirror(string, i):
            mirrors.append(i)

    return mirrors


result = part1()
print(result)

