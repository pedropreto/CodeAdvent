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
    pair = []
    for l in lines:
        print(l)
        element = [x for x in l if x not in ('[', ']')]
        pair.append(element)

        if l == '':
            pair = []
    return 1


def part2():

    return 1


result = part1()
print(result)



