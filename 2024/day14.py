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
    t = 100
    wide = 101
    tall = 103
    quadrant_wide = int((wide - 1) / 2)
    quadrant_tall = int((tall - 1) / 2)

    quadrants = [[] for _ in range(4)]

    dict_quadrant = {1: [[0, quadrant_wide], [0, quadrant_tall]],
                     2: [[quadrant_wide + 1, wide], [0, quadrant_tall]],
                     3: [[0, quadrant_wide], [quadrant_wide - 1, wide]],
                     4: [[quadrant_wide + 1, wide], [quadrant_wide + 1, wide]]}

    for line in lines:
        pattern = r"[-\d]+"
        results = re.findall(pattern, line)
        position = (int(results[0]), int(results[1]))
        velocity = (int(results[2]), int(results[3]))
        final_x = (position[0] + velocity[0] * t) % wide
        final_y = (position[1] + velocity[1] * t) % tall

        final_coordinates = (final_x, final_y)

        for key, value in dict_quadrant.items():
            low_x = dict_quadrant[key][0][0]
            high_x = dict_quadrant[key][0][1]
            low_y = dict_quadrant[key][1][0]
            high_y = dict_quadrant[key][1][1]
            if final_x in range(low_x, high_x) and final_y in range(low_y, high_y):

                quadrants[key - 1].append(final_coordinates)
                print(f'Robot in coordinates {final_coordinates} is in quadrant number {key}')
                break

    print(quadrants)

    safety_factor = 1
    for quadrant in quadrants:
        safety_factor *= len(quadrant)

    return safety_factor


result = part1()
print(result)