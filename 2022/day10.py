#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import string
import numpy as np
import regex as re
from statistics import mean

py_name = os.path.basename(__file__)
file = "day" + re.findall(r'\d+', py_name)[0] + ".txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    cycles = [20, 60, 100, 140, 180, 220]
    signals = []
    final_signals = []
    cycle = 0
    X = 1
    inputs = ["noop", "addx"]
    for l in lines:
        print(l)
        l = l.split()
        if l[0] == inputs[0]:
            cycle += 1
            print(f'X:{X}, cycle:{cycle}, signal:{X*cycle}')
            signals.append(cycle * X)
        else:
            cycle += 1

            signals.append(cycle * X)
            print(f'X:{X}, cycle:{cycle}, signal:{X * cycle}')
            cycle += 1
            signals.append(cycle * X)
            print(f'X:{X}, cycle:{cycle}, signal:{X * cycle}')
            X += int(l[1])

    for i in cycles:
        final_signals.append(signals[i-1])

    return sum(final_signals)


def part2():
    first, last = 0, 39

    signals = []
    cycle = 0
    X = 1
    inputs = ["noop", "addx"]
    for l in lines:
        l = l.split()
        if l[0] == inputs[0]:
            cycle += 1

            signals.append([cycle, X])
        else:
            cycle += 1

            signals.append([cycle, X])

            cycle += 1
            signals.append([cycle, X])

            X += int(l[1])

    pixel = first
    line = ''
    for s in signals:
        sprite_mid = s[1]
        sprite_position = [sprite_mid - 1, sprite_mid, sprite_mid + 1]
        if pixel in sprite_position:
            line += "#"
        else:
            line += "."

        pixel += 1

        if pixel == last + 1:
            print(line)
            line = ''
            pixel = 0

    return ''


result = part2()
print(result)



