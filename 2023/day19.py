#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re


file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    temp_idx = lines.index('')
    flows, parts = [lines[: temp_idx], lines[temp_idx + 1:]]

    flows_dict = {}
    rules_flow = {}
    parts_lists = []
    part_dict = {}
    for flow in flows:
        key = re.findall(r'(.*)\{', flow)[0]
        mid = re.findall(r'([a-zA-Z]+[<>]\d+:[a-zA-Z]+)', flow)
        other = re.findall(r',([^,{}]+)}', flow)[0]

        rules_flow["other"] = other
        rules_flow["rules"] = mid
        flows_dict[key] = dict(rules_flow)

    accepted_parts = []
    final_number = 0
    for part in parts:
        numbers = re.findall(r'\d+', part)
        numbers = [int(num) for num in numbers]
        part_dict["x"], part_dict["m"], part_dict["a"], part_dict["s"] = numbers
        parts_lists.append(part_dict)
        # print(part_dict)

        next_flow = "in"
        while True:
            # print(next_flow)
            next_flow = get_next_flow(flows_dict[next_flow], part_dict)
            if next_flow == 'A':
                accepted_parts.append(part_dict)
                final_number += sum(numbers)
                break
            elif next_flow == 'R':
                break
            else:
                continue

    return final_number


def compare(number1, number2, symbol):
    if symbol == '<':
        return number1 < number2
    elif symbol == '>':
        return number1 > number2
    else:
        return None


def get_next_flow(flow_dict, part_dict):
    for rule in flow_dict["rules"]:
        symbol = re.findall(r'[<>]', rule)[0]
        letter, number = rule.split(':')[0].split(symbol)
        next_step = rule.split(':')[1]

        # check rule
        if compare(int(part_dict[letter]), int(number), symbol):
            return next_step
        else:
            continue

    return flow_dict["other"]

result = part1()
print(result)

