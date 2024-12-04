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
    safe_reports = 0
    dif_total_lst = list()
    for line in lines:
        dif_lst = list()
        line = line.split(' ')
        print(line)

        for i in range(0, len(line)-1):
            dif_lst.append(int(line[i]) - int(line[i+1]))
        print(dif_lst)

        if check_safe(dif_lst):
            safe_reports += 1
        dif_total_lst.append(dif_lst)


    return safe_reports


def part2():
    safe_reports = 0
    for line in lines:
        line = line.split(' ')
        print(line)

        dif_lst = calc_dif(line)

        safe, unsafe_idx = check_safe_v2(dif_lst)
        if safe:
            # if safe, count immediately
            safe_reports += 1
            print('Safe')
        else:
            # if unsafe, try to remove one element
            # if unsafe idx is on the second part of the list, add 1
            if unsafe_idx >= len(line) / 2:
                unsafe_idx += 1

            # check what is the unsafe idx and remove it from the original list
            line.pop(unsafe_idx)
            new_dif_lst = calc_dif(line)
            # check again if it's safe
            safe, unsafe_idx = check_safe_v2(new_dif_lst)
            if safe:
                safe_reports += 1
                print('Turned safe')

    return safe_reports


def calc_dif(lst):
    dif_lst = list()
    for i in range(0, len(lst) - 1):
        dif_lst.append(int(lst[i]) - int(lst[i + 1]))
    return dif_lst

def check_safe(lst):
    positive_count = negative_count = zeros = overslope = 0

    for num in lst:
        positive_count += num > 0
        negative_count += num < 0
        zeros += num == 0
        overslope += abs(num) > 3

    if (positive_count > 0 and negative_count > 0) or zeros > 0 or overslope > 0:
        return False

    return True

def check_safe_v2(lst):
    positive_count = negative_count = zeros = overslope = 0

    for num in lst:
        positive_count += num > 0
        negative_count += num < 0
        zeros += num == 0
        overslope += abs(num) > 3

    if not ((positive_count > 0 and negative_count > 0) or zeros > 0 or overslope > 0):
        return True, -1

    if zeros > 0:
        unsafe_idx = [i for i, num in enumerate(lst) if num == 0]
    elif overslope > 0:
        unsafe_idx = [i for i, num in enumerate(lst) if abs(num) > 3]
    elif positive_count > negative_count:
        unsafe_idx = [i for i, num in enumerate(lst) if num < 0]
    else:
        unsafe_idx = [i for i, num in enumerate(lst) if num > 0]

    return False, unsafe_idx[0]






result = part2()
print(result)

