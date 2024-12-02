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
    unsafe_reports = 0
    total_reports = len(lines)

    for line in lines:
        line = line.split(' ')
        print(line)
        dif_signal = int(line[0]) - int(line[1])
        for i in range(0, len(line)-1):
            # positive is decreasing, negative is increasing
            dif = int(line[i]) - int(line[i+1])
            if sign(dif_signal) != sign(dif) or abs(dif) > 3:
                unsafe_reports += 1
                break
        print(unsafe_reports)

    return total_reports - unsafe_reports

def sign(number):
    if number == 0:
        return 0
    return number/abs(number)

result = part1()
print(result)

