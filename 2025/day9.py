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


def get_points():
    coordinates = []
    for line in lines:
        point = line.split(',')
        coordinates.append((int(point[0]), int(point[1])))


    return coordinates


def part1():
    points = get_points()
    n = len(points)
    biggest_target = 0
    for i in range(n):
        for j in range(i + 1, n):
            # find biggest x + y difference
            dx = abs(points[i][0] - points[j][0])
            dy = abs(points[i][1] - points[j][1])
            target = dx + dy
            print(f'Difference from {points[i]} to {points[j]}: {dx} in X and {dy} in Y')
            if target > biggest_target:
                biggest_target = target
                target_points = [points[i], points[j]]
                area = (dx+1)*(dy+1)
                print(f'Biggest differece found between points {points[i]} and {points[j]}')
                print(f'It results in a shape of area {area}\n')

    return area

result = part1()
print(result)