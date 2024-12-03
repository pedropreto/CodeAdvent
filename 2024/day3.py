#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    content = f.read()

def part1():
    final_result = 0
    pattern = r"mul\(\d+(?:,\d+)*\)"
    matches = re.findall(pattern, content)
    print(matches)

    for match in matches:
        numbers = re.findall(r'\d+', match)
        print(numbers)
        multiplication = int(numbers[0]) * int(numbers[-1])
        final_result += multiplication
        print(f'match is {match}')
        print(f'multiplication is {multiplication}')
        print(f'final result = {final_result}')
    return final_result


result = part1()
print(result)
