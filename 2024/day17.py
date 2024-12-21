#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
from math import floor

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def division(n1, n2):
    # division
    result = floor(n1 / n2)
    return result

def bitxor(n1, n2):
    # bitwise xor
    result = n1 ^ n2
    return result

def modulo8(n1):
    # modulo 8
    result = n1 % 8
    return result


def part1():
    pattern = r"\d+"
    instruction_pointer = 0
    a_value = re.findall(pattern,lines[0])[0]
    b_value = re.findall(pattern,lines[1])[0]
    c_value = re.findall(pattern,lines[2])[0]

    registers = [int(a_value), int(b_value), int(c_value)]

    program = re.findall(pattern, lines[4])

    output = []

    dict_map = {0:0, 6:1, 7:2}

    while instruction_pointer <  len(program) - 1:
        instruction = int(program[instruction_pointer])
        operand = int(program[instruction_pointer + 1])
        combo_operand = operand
        if operand > 3:
            combo_operand = registers[operand - 4]

        if instruction == 0 or instruction == 6 or instruction == 7:
            result = division(registers[0], 2**combo_operand)
            registers[dict_map[instruction]] = result
        elif instruction == 1:
            result = bitxor(registers[1], operand)
            registers[1] = result
        elif instruction == 2:
            result = modulo8(combo_operand)
            registers[1] = result
        elif instruction == 3:
            if registers[0] == 0:
                pass
            else:
                instruction_pointer = operand
                continue
        elif instruction == 4:
            result = bitxor(registers[1], registers[2])
            registers[1] = result
        elif instruction == 5:
            result = modulo8(combo_operand)
            output.append(result)

        instruction_pointer += 2
        # print(output)

    string = ''
    for out in output:
        string += str(out) + ','

    string = string[:-1]

    print(f'Length of output is {len(output)} and length of program is {len(program)}')
    print(f'A is {a_value} and in binary {bin(int(a_value))}')

    return string


def part2():
    pattern = r"\d+"
    a_value = re.findall(pattern, lines[0])[0]
    b_value = re.findall(pattern, lines[1])[0]
    c_value = re.findall(pattern, lines[2])[0]

    registers = [int(a_value), int(b_value), int(c_value)]

    program = re.findall(pattern, lines[4])

    dict_map = {0: 0, 6: 1, 7: 2}

    i = 10000000000000 # to get 15 instructions

    copy_found = False

    suffix = 0b0111110100

    step = 1 << 10 # 2^10
    i = suffix

    while True:
        binary_representation = bin(i)
        assert binary_representation.endswith('0111110100'),\
            "Generated number does not end with the desired binary suffix!"

        instruction_pointer = 0
        output = []

        while instruction_pointer < len(program) - 1:
            instruction = int(program[instruction_pointer])
            operand = int(program[instruction_pointer + 1])
            combo_operand = operand
            if operand > 3:
                combo_operand = registers[operand - 4]

            if instruction == 0 or instruction == 6 or instruction == 7:
                result = division(registers[0], 2 ** combo_operand)
                registers[dict_map[instruction]] = result
            elif instruction == 1:
                result = bitxor(registers[1], operand)
                registers[1] = result
            elif instruction == 2:
                result = modulo8(combo_operand)
                registers[1] = result
            elif instruction == 3:
                if registers[0] == 0:
                    pass
                else:
                    instruction_pointer = operand
                    continue
            elif instruction == 4:
                result = bitxor(registers[1], registers[2])
                registers[1] = result
            elif instruction == 5:
                result = modulo8(combo_operand)
                output.append(str(result))

                if (len(output) > 0 and output == program[:len(output)]) or len(output) == 0:
                    if len(output) > 8:
                        print(f'The A is {i}, its binary is {bin(i)} and the output was {output}')

                    if len(output) == len(program):
                        copy_found = True
                        print(f'Found the copy at A = {i}')
                        break
                else:
                    # print(f'Breaking with output = {output}')
                    break

            instruction_pointer += 2
            # print(output)



        if copy_found:
            break
        i += suffix
        registers[0] = i
        print(f'next number is {i}, in binary {bin(i)}')

    return 0

result = part2()
print(result)
