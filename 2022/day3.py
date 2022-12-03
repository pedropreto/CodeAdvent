#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import string

file = "day3.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    priority = 0
    for rucksack in lines:
        compartment_1 = rucksack[:int(len(rucksack)/2)]
        compartment_2 = rucksack[int(len(rucksack)/2):]

        common = ''.join(set(compartment_1).intersection(compartment_2))
        priority += string.ascii_letters.index(common) + 1

    return priority


def part2():
    i, priority = 2, 0
    while i < len(lines):
        common = ''.join(set(lines[i - 2]).intersection(lines[i - 1]))
        common = ''.join(set(common).intersection(lines[i]))
        priority += string.ascii_letters.index(common) + 1
        i += 3

    return priority


count = part2()
print(count)

