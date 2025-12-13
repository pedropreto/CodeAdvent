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
with open(file_path, "r") as f:
    lines = [line.rstrip() for line in f]  # takes the \n





def find_all_paths(devices, start, end):
    all_paths = []

    def check_path(current, path, visited):
        if current == end:
            print('Reached the end\n')
            print(f'The path is {path}')
            all_paths.append(path.copy())
            return

        for neighbor in devices[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)

                check_path(neighbor, path, visited)

                # backtrack after reaching the end
                path.pop()
                visited.remove(neighbor)

    # check path starting in start, with visited as a set with start only
    check_path(start, [start], {start})
    return all_paths


def part1():
    devices = {}
    start = 'you'
    end = 'out'
    for line in lines:
        device = line.split(':')[0].strip()
        device_output = line.split(':')[1].strip()
        devices[device] = [e for e in device_output.split(' ')]

    print(devices)
    paths = find_all_paths(devices, start, end)
    print(paths)
    return len(paths)


def part2():
    devices = {}
    start = 'svr'
    end = 'out'
    for line in lines:
        device = line.split(':')[0].strip()
        device_output = line.split(':')[1].strip()
        devices[device] = [e for e in device_output.split(' ')]

    print(devices)
    paths = find_all_paths(devices, start, end)
    print(paths)
    return len(paths)

result = part2()
print(result)