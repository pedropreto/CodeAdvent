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

def add_dial(start, x):
    passed = 0
    pointing = False
    final = (start + x) % 100
    rotations = abs(x) // 100

    # passing through zero
    if (abs(x) - rotations * 100) > abs(((100 if x > 0 else 0) - start)) and start != 0:
        passed += 1

    if final == 0:
        pointing = True
        if start == 0:
            rotations = max(0, rotations - 1)

    passed += rotations


    return passed, pointing, final

def part1_2():
    dial = 50
    final_count = 0
    pointing_count = 0
    passed_count = 0

    for instruction in lines:
        direction = instruction[0]
        pattern = r"\d+"
        number = int(re.findall(pattern, instruction)[0])

        print(f'The direction is {direction} and the number is {number}')

        if direction == 'L':
            passed, pointing, dial = add_dial(dial, -number)
        else:
            passed, pointing, dial = add_dial(dial, number)


        final_count += passed + int(pointing)

        pointing_count += int(pointing)
        passed_count += passed



        print(f'\n Dial is now at {dial}!')
        print(f'\nPassed through zero {passed_count} times')
        print(f'Stopped at zero {pointing_count} times\n')

    final_count = passed_count + pointing_count
    print(f'\nThe password is {final_count}!')



result = part1_2()
