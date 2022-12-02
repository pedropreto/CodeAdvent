#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

file = "day1.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    biggest = 0
    d = {}
    elves, elf = list(), list()
    for l in lines:
        if l == '':
            d["food"] = elf
            d["food_sum"] = sum(elf)
            if biggest <= sum(elf):
                biggest = sum(elf)
            elves.append(d)
            elf = list()
        else:
            elf.append(int(l))
    return biggest


def part2():

    elves, elf = list(), list()
    for l in lines:
        if l == '':
            elves.append(sum(elf))
            elf = list()
        else:
            elf.append(int(l))

    elves.sort(reverse=True)
    elves = sum(elves[:3])
    return elves


count = part2()
print(count)

