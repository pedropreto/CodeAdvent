#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re


file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    min_value, max_value = 200000000000000, 400000000000000
    count = 0

    x_positions = []
    y_positions = []
    x_velocities = []
    y_velocities = []
    for line in lines:
        print(line)
        i_x_position, i_y_position, _, x_v, y_v, _ = re.findall(r'-?\d+', line)
        x_positions.append(int(i_x_position))
        y_positions.append(int(i_y_position))
        x_velocities.append(int(x_v))
        y_velocities.append(int(y_v))

    for j in range(0, len(x_positions) - 1):
        for z in range(j + 1, len(x_positions)):

            x, y = find_intersection([x_positions[j], x_positions[z]],
                             [y_positions[j], y_positions[z]],
                             [x_velocities[j], x_velocities[z]], [y_velocities[j], y_velocities[z]])

            print(f'Hailstone 1: {x_positions[j]}, {y_positions[j]}, {x_velocities[j]}, {y_velocities[j]}\n')
            print(f'Hailstone 2: {x_positions[z]}, {y_positions[z]}, {x_velocities[z]}, {y_velocities[z]}\n')
            print(f'Intersection coordinates: x:{x}, y:{y}')

            v1_sign = math.copysign(1, x_velocities[j])
            v2_sign = math.copysign(1, x_velocities[z])

            k1 = (x - x_positions[j]) * v1_sign
            k2 = (x - x_positions[z]) * v2_sign

            if not x and not y:
                pass
            elif k1 < 0 or k2 < 0:
                print(f'It is in the past!')
            elif min_value <= x <= max_value and min_value <= y <= max_value:
                print(f'Intersection is inside test area\n')
                print(count)
                count += 1

            print('\n')
    return count


def find_intersection(x_position, y_position, x_velocity, y_velocity):
    """
    1st step: convert to position equation, independent of time y = bx + c
    2nd step: find the intersection x coordinate
    3rd step: find the intersection y coordinate
    @return:
    """
    x01, x02 = x_position
    y01, y02 = y_position
    vx1, vx2 = x_velocity
    vy1, vy2 = y_velocity

    b1 = -1 / vx1 * (1/(-1/vy1))
    c1 = ((y01 / -vy1) - (x01 / - vx1)) * -vy1

    b2 = -1 / vx2 * (1 / (-1 / vy2))
    c2 = ((y02 / -vy2) - (x02 / - vx2)) * -vy2

    if b1 - b2 == 0:
        return False, False
    else:
        x = (c2 - c1) / (b1 - b2)
    y = b1 * x + c1

    return x, y


result = part1()
print(result)

