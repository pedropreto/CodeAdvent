#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def check_largest_digit(number):
    answer = 0
    idx = 0
    for i, digit in enumerate(number):
        if int(digit) > answer:
            answer = int(digit)
            idx = i

    return answer, idx


def part1():
    joltages = []
    for bank in lines:
        # check largest except for last digit
        first_digit, first_digit_idx = check_largest_digit(bank[:-1])
        second_digit, _ = check_largest_digit(bank[first_digit_idx+1:])

        connected_batteries = str(first_digit) + str(second_digit)
        joltages.append(int(connected_batteries))

    return sum(joltages)

result = part1()
print(result)