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
    monkey_sub_monkeys = {}
    monkey_yells_number = {}
    monkey_yells_formula = {}
    for l in lines:
        monkey, yell = l.split(": ")
        yell_number = re.findall('[0-9]+', l.split(": ")[1])
        if yell_number:
            # it is a number
            monkey_yells_number[monkey] = int(yell_number[0])
        else:
            monkey_yells_formula[monkey] = yell
            monkey_sub_monkeys[monkey] = re.findall('[a-z]+', yell)

    print(f'{monkey_yells_number}\n{monkey_yells_formula}\n\n')

    while len(monkey_yells_formula) > 0:
        monkey_yells_number, monkey_yells_formula = check_formulas(numbers=monkey_yells_number,
                                                                   formulas=monkey_yells_formula,
                                                                   msm=monkey_sub_monkeys)

    return monkey_yells_number['root']


def check_formulas(formulas, numbers, msm):
    for monkey in list(formulas):
        booleans = []
        for m in msm[monkey]:
            booleans.append(m in numbers.keys())
        if all(booleans):  # if all sub monkeys have values already
            n1, sign, n2 = formulas[monkey].split(" ")

            if sign == '+':
                result = numbers[n1] + numbers[n2]
            elif sign == '-':
                result = numbers[n1] - numbers[n2]
            elif sign == '*':
                result = numbers[n1] * numbers[n2]
            elif sign == '/':
                result = numbers[n1] / numbers[n2]

            numbers[monkey] = result
            del formulas[monkey]

    print(f'{numbers}\n{formulas}\n\n')

    return numbers, formulas


def part2():
    return 1


result = part1()
print(result)
