#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import numpy as np

file = "day4.txt"
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


result = part1()
print(result)

