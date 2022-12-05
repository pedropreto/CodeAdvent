#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import string
import numpy as np
import regex as re
from collections import deque

file = "day5.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def cleandata():
    matrix, columns, first_lines = [], 9, 8
    input_lines = lines[:first_lines]
    input_instructions = lines[first_lines + 2:]

    for l in input_lines:
        index = 1
        line = [0] * columns
        for i in range(0, columns + 1):
            if index > len(l):
                next
            else:
                line[i] = l[index]
                index += 4

        line = [' ' if item == 0 else item for item in line]
        matrix.append(line)

    matrix = np.array(matrix)
    transposed_array = matrix.T
    # get initial config of boxes in a matrix
    matrix = transposed_array.tolist()

    # convert lists to queues

    stack_list = []
    for column in matrix:
        stack = deque()
        for c in column:
            if c == ' ':
                next
            else:
                stack.append(c)
        stack_list.append(stack)

    return stack_list, input_instructions


def part1():

    stack_list, input_instructions = cleandata()

    # read further instructions
    for l in input_instructions:
        l = [int(s) for s in re.findall(r'-?\d+\.?\d*', l)]
        move = l[0]
        from_pile = l[1]
        to_pile = l[2]

        for n in range(0, move):
            stack_list[to_pile - 1].appendleft(stack_list[from_pile - 1][0])
            stack_list[from_pile - 1].popleft()

    final_topstack = ''
    for s in stack_list:
        final_topstack += s[0]
    return final_topstack


def part2():
    stack_list, input_instructions = cleandata()

    # read further instructions
    for l in input_instructions:
        l = [int(s) for s in re.findall(r'-?\d+\.?\d*', l)]
        move = l[0]
        from_pile = l[1]
        to_pile = l[2]

        for n in range(move, 0, -1):
            stack_list[to_pile - 1].appendleft(stack_list[from_pile - 1][n - 1])
            del stack_list[from_pile - 1][n - 1]

    final_topstack = ''
    for s in stack_list:
        final_topstack += s[0]
    return final_topstack


count = part2()
print(count)

