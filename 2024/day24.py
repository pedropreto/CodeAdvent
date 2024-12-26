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

    dict_values = {}

    split_index = lines.index('')
    values = lines[:split_index]
    instructions = lines[split_index+1:]

    # store values of wires
    for i, el in enumerate(values):
        wire, value = el.split(': ')
        dict_values[wire] = int(value)


    print(dict_values)
    # parse instructions
    pattern = r'(\w+) (\w+) (\w+) -> (\w+)'

    dict_values = calculate_instructions(pattern, instructions, dict_values)

    # build the final bit number
    match = True
    i = 0
    final_number = ''
    while match:
        if i < 10:
            number_str = '0' + str(i)
        else:
            number_str = str(i)
        to_find = 'z' + number_str

        if dict_values.get(to_find) is None:
            match = False
        else:
            final_number += str(dict_values.get(to_find))

        i += 1

    # reverse the order
    final_number = final_number[::-1]
    # convert from binary to decimal
    final_number = int(final_number,2)


    return final_number


def calculate_instructions(pattern, instructions, dict_values):
    new_instructions = []
    for ins in instructions:
        print(ins)
        matches = re.findall(pattern, ins)
        print(matches)
        wire_op1, op, wire_op2, result = matches[0]

        if dict_values.get(wire_op1) is None or dict_values.get(wire_op2) is None:
            print(f'Wires don''t have values assigned')
            new_instructions.append(ins)
            continue

        if op == 'XOR':
            dict_values[result] = dict_values[wire_op1] ^ dict_values[wire_op2]
        elif op == 'AND':
            dict_values[result] = dict_values[wire_op1] & dict_values[wire_op2]
        elif op == 'OR':
            dict_values[result] = dict_values[wire_op1] | dict_values[wire_op2]
        else:
            print(f'Operation not recognized')

    if len(new_instructions) > 0:
        dict_values = calculate_instructions(pattern, new_instructions, dict_values)

    return dict_values

result = part1()
print(result)