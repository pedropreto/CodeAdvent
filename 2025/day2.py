#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np
from click import password_option

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n

def part1():
    invalidIDs = list()
    ranges = lines[0].split(',')

    for interval in ranges:
        firstID = int(interval.split('-')[0])
        lastID = int(interval.split('-')[1])

        for i in range(firstID, lastID+1):
            # check if it has an even number of digits
            num_string = str(i)
            if len(num_string) % 2 == 0:
                n_half_digits = int(len(num_string) / 2)

                first_half = num_string[:n_half_digits]
                second_half = num_string[n_half_digits:]

                if first_half == second_half:
                    print(f'The {i} is an invalid ID\n')
                    invalidIDs.append(i)
            else:
                continue

    return sum(invalidIDs)

result = part1()
print(result)
