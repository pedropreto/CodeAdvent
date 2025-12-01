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
    stones = lines[0].split(' ')

    new_stones = list(stones)
    blinks = 1

    print(new_stones)

    while blinks <= 50:
        stones = list(new_stones)
        add_stones = 0
        print(blinks)

        for idx, stone in enumerate(stones):
            if int(stone) == 0:
                new_stones[idx + add_stones] = 1
            elif len(str(stone)) % 2 == 0:
                mid_number = int(len(str(stone))/2)
                new_stone_left = int(str(stone)[:mid_number])
                new_stone_right = int(str(stone)[mid_number:])
                new_stones[idx + add_stones] = new_stone_left
                new_stones.insert(idx+add_stones+1, new_stone_right)
                add_stones += 1
            else:
                new_stones[idx+add_stones] = int(stone) * 2024

        blinks += 1
        # print(f'After {blinks} blinks we have the stones {new_stones}')

    return len(new_stones)


def part2():


result = part1()
print(result)

