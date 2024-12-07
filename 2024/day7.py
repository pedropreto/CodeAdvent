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
    sum_equation_results = 0
    for line in lines:
        equation_result, elements = line.split(':')
        print(f'The equation result should be {equation_result}')
        pattern = r"\d+"
        elements_list = re.findall(pattern,elements)
        print(elements_list)
        len_possibilities = len(elements_list) - 1

        configurations = get_all_configurations_new(len_possibilities, 2)


        for config in configurations:
            # 0 is multiplication, 1 is sum
            print(config)
            result_list = list(elements_list)
            final_list = do_operations_no_math_precedences(result_list, config)

            final_result = sum(map(int, final_list))
            print(f'Final result is {final_result}\n')


            if final_result == int(equation_result):
                sum_equation_results += final_result
                print(f'Matched result {final_result}')
                print(f'The score is now {sum_equation_results}\n')
                break

    return sum_equation_results


def part2():
    sum_equation_results = 0
    for z, line in enumerate(lines):
        print(z + 1)
        equation_result, elements = line.split(':')
        # print(f'The equation result should be {equation_result}')
        pattern = r"\d+"
        elements_list = re.findall(pattern, elements)
        # print(elements_list)
        len_possibilities = len(elements_list) - 1

        configurations = get_all_configurations_new(len_possibilities, 3)

        for config in configurations:
            # 0 is multiplication, 1 is sum, 2 is concat
            # print(config)
            result_list = list(elements_list)
            final_list = do_operations_no_math_precedences_part2(result_list, config)

            final_result = sum(map(int, final_list))
            # print(f'Final result is {final_result}\n')

            if final_result == int(equation_result):
                sum_equation_results += final_result
                # print(f'Matched result {final_result}')
                # print(f'The score is now {sum_equation_results}\n')
                break

    return sum_equation_results

    return sum_equation_results


def do_operations_no_math_precedences_part2(result_list, config):
    for c in config:
        if c == 0:
            result = multiply(result_list[0], result_list[1])
        elif c == 1:
            result = add(result_list[0], result_list[1])
        elif c == 2:
            result = concat(result_list[0], result_list[1])
        exclude_indexes = [0, 1]
        result_list = [value for index, value in enumerate(result_list) if index not in exclude_indexes]
        result_list.insert(0, result)
    return result_list

def do_operations_no_math_precedences(result_list, config):
    for c in config:
        if c == 0:
            result = multiply(result_list[0], result_list[1])
        else:
            result = add(result_list[0], result_list[1])
        exclude_indexes = [0, 1]
        result_list = [value for index, value in enumerate(result_list) if index not in exclude_indexes]
        result_list.insert(0, result)
    return result_list


def do_operations_math_precedences(result_list, indexes_multiply):
    try:
        idx = indexes_multiply[0]
    except IndexError:
        idx = None

    while True and len(indexes_multiply) > 0:
        # multiply two values with the lower idx of multiply based on list with all the numbers
        result = multiply(result_list[idx], result_list[idx + 1])
        # create a new list without the elements that are being multiplied
        exclude_indexes = [idx, idx + 1]
        result_list = [value for index, value in enumerate(result_list) if index not in exclude_indexes]
        # insert the multiplication result in the right place
        result_list.insert(idx, result)
        # lower all indexes because the list got 1 element shorter
        indexes_multiply = [x - 1 for x in indexes_multiply]
        del indexes_multiply[0]



        if len(indexes_multiply) == 0:
            break
        else:
            idx = indexes_multiply[0]

    return result_list

def add(a, b):
    return int(a) + int(b)

def multiply(a, b):
    return int(a) * int(b)

def concat(a, b):
    return int(str(a) + str(b))


def get_all_configurations_new(n, num_values):
    # Generate all configurations for numbers in range [0, num_values - 1]
    configurations = []
    for i in range(num_values ** n):  # Use num_values as the base
        # Convert the number to the desired base and pad with leading zeros
        base_string = ""
        num = i
        for _ in range(n):
            base_string = str(num % num_values) + base_string
            num //= num_values
        base_string = base_string.zfill(n)  # Padding (optional)

        # Convert the base string to a list of integers
        configuration = [int(digit) for digit in base_string]
        configurations.append(configuration)

    return configurations

def get_all_configurations(n):
    # Generate all configurations by iterating through binary numbers
    configurations = []
    for i in range(2 ** n):
        # Convert the number to a binary string and pad it with leading zeros to ensure length n
        binary_string = bin(i)[2:].zfill(n)
        # Convert the binary string to a list of integers (0s and 1s)
        configuration = [int(bit) for bit in binary_string]
        configurations.append(configuration)

    return configurations


result = part2()
print(result)