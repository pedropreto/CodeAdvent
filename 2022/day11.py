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
    i = 0
    info = {}
    start_items_l = []
    operation_sign_l = []
    operator_l = []
    test_l = []
    iftrue_l = []
    iffalse_l = []

    while i < len(lines):
        monkey_nr = re.findall(r'\d+', lines[i])[0]
        start_items = re.findall('\d+', lines[i+1])

        operation = lines[i+2].split("= ")[1]
        _, sign, operator = operation.split(" ")

        test = re.findall('\d+', lines[i+3])[0]
        iftrue = re.findall('\d+', lines[i+4])[0]
        iffalse = re.findall('\d+', lines[i+5])[0]

        start_items_l.append([int(x) for x in start_items])
        operation_sign_l.append(sign)
        operator_l.append(operator)
        test_l.append(int(test))
        iftrue_l.append(int(iftrue))
        iffalse_l.append(int(iffalse))

        i += 7

    info = {"start_items":start_items_l, "signs": operation_sign_l, "operators": operator_l,
            "test": test_l, "iftrue": iftrue_l, "iffalse": iffalse_l}

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    round = 20
    r = 1
    monkey_nr = int(monkey_nr)
    info["items_inpected"] = [0 for x in range(0, monkey_nr + 1)]
    while r <= round:

        for j in range(0, monkey_nr + 1):

            info["items_inpected"][j] += len(info["start_items"][j])

            for item in info["start_items"][j]:
                if info["operators"][j] == 'old':
                    worry_level = operations[info["signs"][j]](item, item)
                else:
                    worry_level = operations[info["signs"][j]](item, int(info["operators"][j]))

                worry_level = math.floor(worry_level / 3)

                if check_divisible(worry_level, info["test"][j]):
                    target_monkey = int(info["iftrue"][j])
                else:
                    target_monkey = int(info["iffalse"][j])

                info["start_items"][target_monkey].append(worry_level)

            info["start_items"][j] = []

        print(f'Round {r}\nStart Items: {info["start_items"]}\nItems Inspected: {info["items_inpected"]}')
        r += 1

    info["items_inpected"].sort(reverse=True)
    result = info["items_inpected"][0] * info["items_inpected"][1]

    return result


def part2():
    i = 0
    info = {}
    start_items_l = []
    operation_sign_l = []
    operator_l = []
    test_l = []
    iftrue_l = []
    iffalse_l = []

    while i < len(lines):
        monkey_nr = re.findall(r'\d+', lines[i])[0]
        start_items = re.findall('\d+', lines[i + 1])

        operation = lines[i + 2].split("= ")[1]
        _, sign, operator = operation.split(" ")

        test = re.findall('\d+', lines[i + 3])[0]
        iftrue = re.findall('\d+', lines[i + 4])[0]
        iffalse = re.findall('\d+', lines[i + 5])[0]

        start_items_l.append([int(x) for x in start_items])
        operation_sign_l.append(sign)
        operator_l.append(operator)
        test_l.append(int(test))
        iftrue_l.append(int(iftrue))
        iffalse_l.append(int(iffalse))

        i += 7

    info = {"start_items": start_items_l, "signs": operation_sign_l, "operators": operator_l,
            "test": test_l, "iftrue": iftrue_l, "iffalse": iffalse_l}



    round = 20
    r = 1
    monkey_nr = int(monkey_nr)
    info["items_inpected"] = [0 for x in range(0, monkey_nr + 1)]
    while r <= round:

        for j in range(0, monkey_nr + 1):

            info["items_inpected"][j] += len(info["start_items"][j])

            for item in info["start_items"][j]:
                worry_level = operate(item, info["signs"][j], info["operators"][j])

                #worry_level = math.floor(worry_level * (1/(int(info["test"][j]))))

                if check_divisible(worry_level, info["test"][j]):
                    target_monkey = int(info["iftrue"][j])
                else:
                    target_monkey = int(info["iffalse"][j])
                    result = operate(worry_level, info["signs"][target_monkey], info["operators"][target_monkey])
                    remainder = result % info["test"][j]
                    worry_level = info["test"][j] + remainder

                info["start_items"][target_monkey].append(worry_level)

            info["start_items"][j] = []

        print(f'Round {r}\nStart Items: {info["start_items"]}\nItems Inspected: {info["items_inpected"]}')
        # print(f'Round {r}')
        r += 1

    info["items_inpected"].sort(reverse=True)
    result = info["items_inpected"][0] * info["items_inpected"][1]

    return result


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


def operate(original_value, sign, value_operation):

    operations = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
    }

    if value_operation == 'old':
        worry_level = operations[sign](original_value, original_value)
    else:
        worry_level = operations[sign](original_value, int(value_operation))

    return worry_level


def check_divisible(n1, n2):
    if n1 % n2 == 0:
        return True
    else:
        return False

result = part2()
print(result)



