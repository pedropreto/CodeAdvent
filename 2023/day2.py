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


def part2():
    final_number = 0
    for line in lines:
        pattern = r'(\d+ \w+)'
        matches = re.findall(pattern, line)
        color_dict = {"blue": 0, "red": 0, "green": 0}

        for match in matches:
            ball_pattern = r'(\w+)'
            number, color = re.findall(ball_pattern, match)

            if int(number) > int(color_dict[color]):
                color_dict[color] = number

        print(color_dict)
        product = 1
        for value in color_dict.values():
            product *= int(value)
        final_number += product

    return final_number


result = part2()
print(result)

