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
    disk_map = lines[0]
    final_string = ''
    idx = 0
    decades = 0
    idx_list = []

    # represent string of idx and blank spaces
    for i in range(len(disk_map)):
        if i % 2 == 0:
            for j in range(int(disk_map[i])):
                idx_list.append(idx)
            final_string += str(idx) * int(disk_map[i])
            idx += 1
        else:
            final_string += '.' * int(disk_map[i])

    blank_indices = [idx for idx, char in enumerate(final_string) if char == '.']

    no_spaces_string = final_string.replace('.', '')

    print(f'The string to be evaluated is {final_string}')
    print(f'The idx list is {idx_list}')
    print(f'The blank spots are {blank_indices}')

    # fill the blank spaces with the last element
    while len(blank_indices) > 0:
        # get last element of list
        final_string = final_string[:blank_indices[0]] + no_spaces_string[-1] + final_string[blank_indices[0]+1:]
        # print(f'Last element of the string: {no_spaces_string[-1]} goes to idx {blank_indices[0]}')
        final_string = final_string[:-1]
        while final_string[-1] == '.':
            final_string = final_string[:-1]
            del blank_indices[-1]
        # print(f'The final string is now {final_string}')

        no_spaces_string = no_spaces_string[:-1]
        idx_list.insert(blank_indices[0], idx_list[-1])
        del blank_indices[0]
        del idx_list[-1]
        # print(f'The idx list is now {idx_list}')
        # print(f'The blank indices are now {blank_indices}')


    product_idx = sum(int(z) * i for i, z in enumerate(idx_list))
    print(f'The product of index and digit is {product_idx}')

    return product_idx

result = part1()
print(result)