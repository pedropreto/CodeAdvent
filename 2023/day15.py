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
    final_number = 0

    for line in lines:
        elements = line.split(',')

    for el in elements:
        result = 0
        for char in el:
            ascii_value = ord(char)
            result = ((result + ascii_value) * 17) % 256
        final_number += result

    return final_number


result = part1()
print(result)

