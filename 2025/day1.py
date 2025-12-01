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

def part1():
    dial = 50
    password = 0

    for instruction in lines:
        direction = instruction[0]
        pattern = r"\d+"
        number = int(re.findall(pattern, instruction)[0])

        if number > 100:
            # last 2 digits
            number = int(str(number)[-2:])

        print(f'The direction is {direction} and the number is {number}')

        if direction == 'L':
            dial -= number
        else:
            dial += number


        if dial >= 100:
            dial = dial - 100
        elif dial < 0:
            dial = 100 + dial

        if dial == 0:
            password += 1

        print(f'\n Dial is now at {dial}!')
    print(f'\nThe password is {password}!')

result = part1()
