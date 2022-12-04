#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import string

file = "day4.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    count = 0

    for l in lines:
        print(f'line {l}')
        pairs = l.split(',')
        limits_1, limits_2 = pairs[0].split('-'), pairs[1].split('-')
        if (int(limits_2[0]) >= int(limits_1[0]) and int(limits_2[1]) <= int(limits_1[1])) \
                or (int(limits_1[0]) >= int(limits_2[0]) and int(limits_1[1]) <= int(limits_2[1])):
            count += 1
            print(f'{count} pairs are contained')
        else:
            next

    return count


def part2():
    count = 0

    for l in lines:
        print(f'line {l}')
        pairs = l.split(',')
        limits_1, limits_2 = pairs[0].split('-'), pairs[1].split('-')
        if int(limits_2[0]) <= int(limits_1[0]) <= int(limits_2[1]) or int(limits_1[0]) <= int(limits_2[0]) <= int(limits_1[1]):
            count += 1
            print(f'{count} pairs overlap')
        else:
            next
    return count


count = part2()
print(count)

