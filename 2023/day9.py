#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np

start = time.time() * 1000

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    final_number = 0
    for line in lines:
        sequence = [int(x) for x in re.findall(r'[-+]?\d+', line)]
        new_sequence, last_elements = find_next_sequence(sequence, [sequence[-1]])

        for idx, el in enumerate(reversed(last_elements)):
            if idx >= len(last_elements) - 1:
                break
            last_elements[-idx - 2] = last_elements[-idx - 2] + el
            print(last_elements)

        final_number += last_elements[0]
        print(last_elements[0])

        print('Next line')

    return final_number


def part2():
    final_number = 0
    for line in lines:
        sequence = [int(x) for x in re.findall(r'[-+]?\d+', line)]
        new_sequence, first_elements = find_next_sequence_part2(sequence, [sequence[0]])

        for idx, el in enumerate(reversed(first_elements)):
            if idx >= len(first_elements) - 1:
                break
            first_elements[-idx - 2] = first_elements[-idx - 2] - el
            print(first_elements)

        final_number += first_elements[0]
        print(first_elements[0])

        print('Next line')

    return final_number


def find_next_sequence_part2(sequence, first_elements):
    new_sequence = [1] * (len(sequence) - 1)
    for i in range(0, len(new_sequence)):
        new_sequence[i] = sequence[i+1] - sequence[i]

    if len(new_sequence) == 0:
        first_elements = [0]
    elif new_sequence != [0] * len(new_sequence):
        first_elements.append(new_sequence[0])
        new_sequence, first_elements = find_next_sequence_part2(new_sequence, first_elements)

    return new_sequence, first_elements


def find_next_sequence(sequence, last_elements):
    new_sequence = [1] * (len(sequence) - 1)
    for i in range(0, len(new_sequence)):
        new_sequence[i] = sequence[i+1] - sequence[i]

    if len(new_sequence) == 0:
        last_elements = [0]
    elif new_sequence != [0] * len(new_sequence):
        last_elements.append(new_sequence[-1])
        new_sequence, last_elements = find_next_sequence(new_sequence, last_elements)

    return new_sequence, last_elements


result = part2()
print(result)
