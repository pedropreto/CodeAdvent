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
    word = 'XMAS'
    occurences = 0
    rotate = 0
    print(lines)
    matrix = lines
    matrices = list()
    matrices.append(matrix)

    while rotate < 3:
        # rotate matrix
        matrix = [''.join(row) for row in zip(*matrix)][::-1]
        print(matrix)
        matrices.append(matrix)
        rotate += 1

    print(matrices)

    # find X, then try to find XMAS to the left up to down left, rotate 90º, repeat
    for idx, matrix in enumerate(matrices):
        print(f'Matrix number {idx + 1}')
        for row in matrix:
            print(row)
            only_left = False
        for j, line in enumerate(matrix):
            for i, letter in enumerate(line):

                # exceeds limits
                # no more space to check diagonal down
                if  j > len(matrix) - len(word):
                    only_left = True

                # no more space left (diagonal and pure left)
                if i > len(line) - len(word):
                    break

                if letter == word[0]: # finds the first letter

                    # check for the left
                    word_left = check_left(i, line, word)
                    word_down_left = False
                    if only_left == False:
                        # check for diagonal down left
                        word_down_left = check_down_left(i, j, word, matrix)



                    occurences += (word_left + word_down_left)
                    print(occurences)


    return occurences


def part2():


    return 0


def check_down_left(i, j, word, matrix):
    increment = 1
    next_letters = list()
    while increment < len(word):
        next_letters.append(matrix[j + increment][i + increment])
        increment += 1

    next_letters = ''.join(next_letters)
    print(f'Next letters on the diagonal are {next_letters}')
    if next_letters == word[1:]:
        return True

    return False


def check_left(i, line, word):
    next_letters = line[i + 1: i + 1 + len(word[1:])]
    print(f'Next letters on the left are {next_letters}')
    if next_letters == word[1:]:
        return True

    return False


result = part1()
print(result)
