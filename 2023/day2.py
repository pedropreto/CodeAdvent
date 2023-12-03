#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re

file = "day2.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    limits = {"red": 12, "green": 13, "blue": 14}
    game_number_arr = list()
    impossible_games = list()

    for line in lines:
        print(line)
        pattern = r'(\d+ \w+)'
        matches = re.findall(pattern, line)
        game_pattern = r'(\d+):'
        game_number = re.findall(game_pattern, line)[0]
        game_number_arr.append(int(game_number))
        for match in matches:
            ball_pattern = r'(\w+)'
            number, color = re.findall(ball_pattern, match)

            if int(number) > limits[color]:
                print('Not possible')
                impossible_games.append(int(game_number))
                break

    possible_games = [x for x in game_number_arr if x not in impossible_games]
    final_number = sum(possible_games)

    return final_number



# def part1():
#     limits = {"red": 12, "green": 13, "blue": 14}
#
#     for line in lines:
#         print(line)
#         pattern = r'(\d+ \w+, \d+ \w+;)'
#         matches = re.findall(pattern, line)
#         for match in matches:
#             single_pattern = r'(\w+)'
#             single_match = re.findall(single_pattern, match)
#             print(single_match)
#             if single_match[1] > limits[single_match[1]]:
#                 print('Not possible')
#         print(matches)




result = part1()
print(result)

