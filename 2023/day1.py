#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re

file = "day1.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    final_number = 0
    for line in lines:
        line_number = join_numbers(line)
        final_number += int(line_number)

    return final_number


def part2():
    # this also solves part1
    final_number = 0
    matches = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    first_part = ''
    second_part = ''

    for line in lines:
        # finding the first number
        i = 0
        while True:
            first_part += line[i]
            found = find_substring_in_string(first_part, list(matches.keys()))
            if found:
                first_part = first_part.replace(found, str(matches[found]))
                break
            else:
                if bool(re.search(r'\d', first_part)):
                    break
            i += 1

        # finding the last number
        j = -1
        while True:
            second_part = line[j] + second_part
            found = find_substring_in_string(second_part, list(matches.keys()))
            if found:
                second_part = second_part.replace(found, str(matches[found]))
                break
            else:
                if bool(re.search(r'\d', second_part)):
                    break
            j -= 1

        line = first_part + second_part
        line_number = join_numbers(line)
        final_number += int(line_number)
        first_part, second_part = '', ''

    return final_number


def find_substring_in_string(target_string, substring_list):
    found_substring = None

    for substring in substring_list:
        if substring in target_string:
            found_substring = substring
            break

    return found_substring


def join_numbers(line):

    # remove letters from string
    line = re.sub('\D', '', line)
    # join first digit with last
    number = line[0] + line[-1]

    return number


result = part2()
print(result)

