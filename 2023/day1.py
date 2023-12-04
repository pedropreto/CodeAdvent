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
    final_number = 0
    for line in lines:
        line_number = join_numbers(line)
        final_number += int(line_number)

    return final_number


def part2():

    final_number = 0

    for line in lines:

        first_part = search_numbers_in_string(line=line, search_type='first')
        last_part = search_numbers_in_string(line=line, search_type='last')

        line = first_part + last_part
        line_number = join_numbers(line)
        final_number += int(line_number)

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


def search_numbers_in_string(line, search_type):
    """
    This functions searchs for a number in the form of a digit or a string (eg. four = 4)
    Depending on the search type it could be the first or the last number

    @param line: string to check
    @param search_type: check if you want to search for the FIRST or LAST number of the string
    @return: returns the first (or last) number of the string
    """
    matches = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    partial_string = ''

    if search_type.lower() == 'first':
        i = 0
        add_number = 1
    elif search_type.lower() == 'last':
        i = -1
        add_number = -1

    while True:

        if search_type.lower() == 'first':
            partial_string += line[i]
        elif search_type.lower() == 'last':
            partial_string = line[i] + partial_string

        found = find_substring_in_string(partial_string, list(matches.keys()))
        if found:
            partial_string = partial_string.replace(found, str(matches[found]))
            break
        else:
            if bool(re.search(r'\d', partial_string)):
                break
        i += add_number

    return partial_string


result = part2()
print(result)

