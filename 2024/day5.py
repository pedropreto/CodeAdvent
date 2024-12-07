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
    page_order_rules, page_produce = parse_input()
    result = 0
    precedence_dict = {}
    page_list = []
    pattern = r"\d+"
    for rule in page_order_rules:
        matches = re.findall(pattern, rule)
        page_before, page_after = matches

        for page in matches:
            if page not in page_list:
                page_list.append(page)

        if page_after not in precedence_dict:
            precedence_dict[page_after] = []

        precedence_dict[page_after].append(page_before)

    print(f'This is our {precedence_dict}')
    for update in page_produce:
        matches = re.findall(pattern, update)
        print(f'Order of the pages to check: {matches}')
        for i in range (1, len(matches)):
            valid = True
            numbers_before = matches[:i]
            precedences = precedence_dict.get(matches[i], [])
            print(f'The number being evaluated is {matches[i]} and the numbers before him in the pages to check are {numbers_before}')
            print(f'The precedences of the number being evaluated are {precedences}')
            is_subset = set(numbers_before).issubset(set(precedences))

            if not is_subset:
                print(f'Order not valid\n')
                valid = False
                break
            else:
                print(f'{matches[i]} is after {numbers_before}')

            if i == len(matches) - 1 and valid:
                middle_page = int(matches[len(matches) // 2])
                result += middle_page
                print(f'Order correct!\n')

    return result



def parse_input():
    divider_index = lines.index('')
    page_order_rules = lines[:divider_index]
    page_produce = lines[divider_index + 1:]

    return page_order_rules, page_produce

result = part1()
print(result)

