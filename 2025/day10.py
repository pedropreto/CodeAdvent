#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np
import itertools
from collections import deque, Counter


file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path, "r") as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def parse_input(text):
    pattern_lights = r"\[[.#]+\]"
    pattern_buttons = r"\(([^()]+)\)"
    lights = re.findall(pattern_lights, text)
    buttons = re.findall(pattern_buttons, text)
    buttons = [[int(n.strip()) for n in group.split(",")] for group in buttons]

    return lights[0].replace('[', '').replace(']',''), buttons


def toggle_lights(button, lights):
    lights_set = set(lights)
    for b in button:
        if b in lights:
            lights_set.remove(b)
        else:
            lights_set.add(b)
    return list(lights_set)


def part1():
    min_button_presses = []
    for line in lines:
        lights, buttons = parse_input(line)
        current_lights = []

        # get the light idx that are turned on
        light_idx = [i for i, l in enumerate(lights) if l == '#']
        print(f'Lights on are {light_idx}')


        # found = False
        button_presses = []
        used_prefixes = []

        # convert buttons to tuples for hashable comparison
        buttons_tuple = [tuple(b) for b in buttons]

        for button_order in itertools.permutations(buttons_tuple):
            # skip permutation that starts with best prefix found
            # it can be improved because the order of the prefix does not matter
            skip = False
            for prefix in used_prefixes:
                if Counter(button_order[:len(prefix)]) == Counter(prefix):
                    skip = True
                    break
            if skip:
                continue

            button_press = 0
            current_lights_copy = current_lights.copy()

            for button in button_order:
                current_lights_copy = toggle_lights(button, current_lights_copy)
                button_press += 1

                if button_press > min(button_presses, default=len(button_order)):
                    break

                if current_lights_copy == light_idx:
                    # print(f'It turned the lights on correctly!')
                    # print(f'Button order is {button_order[:button_press]} pressing {button_press} times!')

                    button_presses.append(button_press)
                    used_prefixes.append(button_order[:button_press])
                    break

        min_button_presses.append(min(button_presses))

    return sum(min_button_presses)


def part1_binary():
    min_lens = []
    for line in lines:
        lights, buttons = parse_input(line)
        target_lights = [i for i, l in enumerate(lights) if l == '#']

        button_masks = [sum(1 << i for i in b) for b in buttons]
        target_mask = sum(1 << i for i in target_lights)
        start_mask = 0

        queue = deque([(start_mask, [])])
        seen = {start_mask}

        while queue:
            # get the first state visited
            state, sequence = queue.popleft()

            # check if target
            if state == target_mask:
                min_lens.append(len(sequence))
                print([buttons[i] for i in sequence], len(sequence))
                break

            # Try pressing each button
            for i, mask in enumerate(button_masks):
                new_state = state ^ mask
                if new_state not in seen:
                    seen.add(new_state)
                    queue.append((new_state, sequence + [i]))

    return sum(min_lens)


result = part1_binary()
print(result)