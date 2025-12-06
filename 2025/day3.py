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


def part2():
    joltages = []
    n_total_digits = len(lines[0])
    n_batteries = 12
    max_excluded = n_total_digits - n_batteries
    for bank in lines:
        excluded = 0
        final_bank = ''
        # Check the largest in the section and exclude the rest
        # continue checking for each section after the last digit chosen
        # when no more can be excluded, end
        while excluded < max_excluded:
            digit, digit_idx = check_largest_digit(bank[:max_excluded-excluded+1])
            final_bank += str(digit)

            excluded += digit_idx
            bank = bank[digit_idx + 1:]
            if len(final_bank) >= n_batteries:
                bank = ''
                break

        final_bank += bank
        joltages.append(int(final_bank))

    return sum(joltages)




result = part2()
print(result)