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
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, content)
    print(matches)

    for match in matches:
        multiplication = product(match)
        final_result += multiplication
        print(f'match is {match}')
        print(f'multiplication is {multiplication}')
        print(f'final result = {final_result}')
    return final_result


def part2():
    final_result = 0
    new_lst = list()
    switch = True
    pattern = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"
    matches = re.findall(pattern, content)
    print(matches)
    for match in matches:
        if match == 'don\'t()':
            switch = False
            continue
        elif match == 'do()':
            switch = True
            continue

        if switch:
            new_lst.append(match)
            result = product(match)
            final_result += result


    print(new_lst)

    return final_result


def product(string):
    numbers = re.findall(r'\d+', string)
    multiplication = int(numbers[0]) * int(numbers[-1])
    return multiplication

result = part2()
print(result)
