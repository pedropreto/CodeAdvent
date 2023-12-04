#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():

    final_number = 0
    for line in lines:
        matching_numbers = []
        _, cards = line.split(':')
        winning_card, my_card = cards.split('|')
        winning_numbers = re.findall(r'\d+', winning_card)
        my_numbers = re.findall(r'\d+', my_card)
        for number in my_numbers:
            if number in winning_numbers:
                matching_numbers.append(number)

        card_points = 2**(len(matching_numbers) -1) if len(matching_numbers) > 0 else 0
        final_number += card_points

    return final_number


def part2():
    card_points = []  # useless list because they didn't ask for points
    cards_reps = [1] * len(lines)  # list of repetitions of the cards
    for line in lines:
        matching_numbers = []
        game_number_part, cards = line.split(':')
        game_number = int(re.findall(r'\d+', game_number_part)[0])
        winning_card, my_card = cards.split('|')
        winning_numbers = re.findall(r'\d+', winning_card)
        my_numbers = re.findall(r'\d+', my_card)
        for number in my_numbers:
            if number in winning_numbers:
                matching_numbers.append(number)

        for i in range(game_number, game_number - 1 + len(matching_numbers) + 1):
            cards_reps[i] += 1 * cards_reps[game_number - 1]

        single_card_points = 2 ** (len(matching_numbers) - 1) if len(matching_numbers) > 0 else 0
        card_points.append(single_card_points)

    return sum(cards_reps)


result = part2()
print(result)

