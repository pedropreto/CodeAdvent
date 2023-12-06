#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import numpy as np

start = time.time()

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    times = re.findall(r'\d+', lines[0].split(':')[1])
    record_distances = re.findall(r'\d+', lines[1].split(':')[1])

    final_number = 1
    beating_ways = [0] * len(times)
    for idx, time in enumerate(times):
        for i in range(1, int(time)):
            distance = (int(time) - i) * i

            beating_ways[idx] += 1 if distance > int(record_distances[idx]) else 0

    for way in beating_ways:
        final_number *= way

    return final_number


def part2():

    times = re.findall(r'\d+', lines[0].split(':')[1])
    record_distances = re.findall(r'\d+', lines[1].split(':')[1])

    time, record_distance = '', ''
    for x in times:
        time = time + x

    for y in record_distances:
        record_distance = record_distance + y

    beating_ways = 0
    for i in range(1, int(time)):
        distance = (int(time) - i) * i
        if distance > int(record_distance):
            break

        beating_ways = int(time) - 1 - 2 * i

    return beating_ways


result = part2()
print(result)

end = time.time()

print(f'This took {(end-start)} seconds')
