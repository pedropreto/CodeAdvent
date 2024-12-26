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
    result = 0
    pattern = r"\d+"

    precedence_dict, page_produce = get_precedence_map(pattern)

    print(f'These is our precedences map {precedence_dict}')
    for update in page_produce:
        pages = re.findall(pattern, update)
        print(f'Order of the pages to check: {pages}')
        new_pages = [0] * len(pages)

        for i in range(0, len(pages)):
            if precedence_dict.get(pages[i]) is None:
                precedence_pages = []
            else:
                precedence_pages = [x for x in pages if x in precedence_dict[pages[i]]]

            new_pages[len(precedence_pages)] = pages[i]

            if new_pages[:i+1] != pages[:i+1]:
                print(f'The order is incorrect, this does not matter')
                break


        if new_pages == pages:
            print(f'The pages are in incorrect order! They were like this {pages}. '
                  f'\nWe fixed them! Now they are {new_pages}')
            middle_page = int(new_pages[len(new_pages) // 2])
            result += middle_page

    return result


def part2():
    result = 0
    pattern = r"\d+"

    precedence_dict, page_produce = get_precedence_map(pattern)

    print(f'These is our precedences map {precedence_dict}')
    for update in page_produce:
        pages = re.findall(pattern, update)
        print(f'Order of the pages to check: {pages}')
        new_pages = [0] * len(pages)

        for i in range(0, len(pages)):
            if precedence_dict.get(pages[i]) is None:
                precedence_pages = []
            else:
                precedence_pages = [x for x in pages if x in precedence_dict[pages[i]]]

            new_pages[len(precedence_pages)] = pages[i]

        if new_pages != pages:
            print(f'The pages are in incorrect order! They were like this {pages}. '
                  f'\nWe fixed them! Now they are {new_pages}')
            middle_page = int(new_pages[len(new_pages) // 2])
            result += middle_page

    return result


def get_precedence_map(pattern):
    page_order_rules, page_produce = parse_input()
    precedence_dict = {}
    for rule in page_order_rules:
        matches = re.findall(pattern, rule)
        page_before, page_after = matches

        if page_after not in precedence_dict:
            precedence_dict[page_after] = []

        precedence_dict[page_after].append(page_before)

    return precedence_dict, page_produce


def parse_input():
    divider_index = lines.index('')
    page_order_rules = lines[:divider_index]
    page_produce = lines[divider_index + 1:]

    return page_order_rules, page_produce

result = part1()
print(result)

