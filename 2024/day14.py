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
                     3: [[0, quadrant_wide], [quadrant_tall + 1, tall]],
                     4: [[quadrant_wide + 1, wide], [quadrant_tall + 1, tall]]}

    for line in lines:
        pattern = r"[-\d]+"
        results = re.findall(pattern, line)
        position = (int(results[0]), int(results[1]))
        velocity = (int(results[2]), int(results[3]))
        final_x = (position[0] + velocity[0] * t) % wide
        final_y = (position[1] + velocity[1] * t) % tall
        final_coordinates = (final_x, final_y)

        print(f'Evaluating robot starting in {position} and ending in {final_coordinates}')

        for key, value in dict_quadrant.items():
            low_x = dict_quadrant[key][0][0]
            high_x = dict_quadrant[key][0][1]
            low_y = dict_quadrant[key][1][0]
            high_y = dict_quadrant[key][1][1]
            if final_x in range(low_x, high_x) and final_y in range(low_y, high_y):

                quadrants[key - 1].append(final_coordinates)
                print(f'Robot is in quadrant number {key}')
                break

    print(quadrants)

    safety_factor = 1
    for quadrant in quadrants:
        safety_factor *= len(quadrant)

    return safety_factor


def part2():
    filename = "grid_output.txt"
    with open(filename, 'w') as file:
        pass

    for t in range(0, 10000):
        print(t)
        wide = 101
        tall = 103

        points = []

        for line in lines:
            pattern = r"[-\d]+"
            results = re.findall(pattern, line)
            position = (int(results[0]), int(results[1]))
            velocity = (int(results[2]), int(results[3]))
            final_x = (position[0] + velocity[0] * t) % wide
            final_y = (position[1] + velocity[1] * t) % tall
            final_coordinates = (final_x, final_y)
            points.append(final_coordinates)

        grid = [['.' for _ in range(wide)] for _ in range(tall)]

        for point in points:
            x, y = point
            if 0 <= x < wide and 0 <= y < tall:
                grid[y][x] = '#'

        # Write the grid to a file
        with open(filename, 'a') as file:
            for row in grid:
                file.write(''.join(row) + '\n')
            file.write('\n' + str(t) + '\n')

    return 0

result = part2()
print(result)