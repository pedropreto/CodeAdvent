#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    right_list, left_list = format_input()

    left_list.sort()
    right_list.sort()

    final_distance = 0
    for i in range(0, len(left_list)):
        print(f"left number: {left_list[i]}")
        print(f"right number {right_list[i]}")
        final_distance += abs(left_list[i]-right_list[i])
        print(f"final distance is: {final_distance}")

    return final_distance

def part2():
    right_list, left_list = format_input()
    final_score = 0
    for i in left_list:
        final_score += right_list.count(i) * i

    return final_score



def format_input():
    right_list, left_list = list(), list()

    for line in lines:
        output = line.split(" ")

        left_list.append(int(output[0]))
        right_list.append(int(output[-1]))
    return left_list, right_list


result = part2()
print(result)

