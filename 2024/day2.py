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
    dif_list = get_dif_list(lines)

    for lst in dif_list:
        safe_bool, _ = check_safe(lst)
        print(lst)
        print(safe_bool)
        print('\n')
        if safe_bool:
            safe_reports += 1

    return safe_reports


def part2():
    safe_reports = 0
    dif_list, original_lst = get_dif_list(lines)
    for j in range(0, len(dif_list) - 1):
        element = dif_list[j]
        original_element = original_lst[j]

        safe_bool, idx_unsafe = check_safe(element)
        print(f'list {original_element} is {safe_bool}, with the dif of {element}')

        if safe_bool:
            safe_reports += 1
        if not safe_bool: # faltam os casos das pontas com abs > 3
            if check_same_sign(element):
                if abs(element[0]) > 3:
                    idx_unsafe = 0
                elif abs(element[len(element) - 1]) > 3:
                    idx_unsafe = len(element) - 1
                else:
                    continue

            if idx_unsafe != len(element) - 1 and idx_unsafe != 0:
                element[idx_unsafe - 1] = element[idx_unsafe - 1] + element[idx_unsafe]
                element.pop(idx_unsafe)
            else:
                element.pop(idx_unsafe)

            safe_bool, _ = check_safe(element)
            if safe_bool:
                print(f'list {element} turned {safe_bool}')
                safe_reports += 1
                print(f'Number of safe reports is {safe_reports}')
    return safe_reports

def get_dif_list(lines):
    dif_list, original_lst = list(), list()
    for line in lines:
        line = line.split(' ')
        line_dif = list()
        original_lst.append(line)

        for i in range(0, len(line)-1):
            line_dif.append(int(line[i]) - int(line[i+1]))

        dif_list.append(line_dif)

    return dif_list, original_lst


def check_safe(dif_lst):
    sign_list = sign(dif_lst[0])
    for i in range(0, len(dif_lst)):
        if dif_lst[i] == 0 or sign(dif_lst[i]) != sign_list or abs(dif_lst[i])>3:
            return False, i
    return True, -1



def check_same_sign(lst):
    # Check if all elements are positive
    if all(x > 0 for x in lst):
        return True

    # Check if all elements are negative
    if all(x < 0 for x in lst):
        return True

    # If neither, return False
    return False

def sign(number):
    if number == 0:
        return 0
    return number/abs(number)


result = part2()
print(result)

