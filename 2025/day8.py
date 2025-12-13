#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
from collections import Counter

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path, "r") as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def distance_3d(p1, p2):
    # p1 and p2 are tuples or lists like (x, y, z)
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2 + (p2[2] - p1[2])**2)


def parse_points():
    point_list = []
    for line in lines:
        coordinates = line.split(',')
        point = (int(coordinates[0]), int(coordinates[1]), int(coordinates[2]))
        point_list.append(point)

    return point_list

def min_distances(point_list):
    pairs = []
    n = len(point_list)

    for i in range(n):
        for j in range (i + 1, n):
            p1 = point_list[i]
            p2 = point_list[j]
            distance = distance_3d(p1, p2)
            pairs.append((distance, p1, p2))


    pairs.sort(key=lambda x: x[0])

    return pairs


def part1():
    junction_boxes = parse_points()

    n_connections = 1000

    pairs = min_distances(junction_boxes)

    circuits = [{box} for box in junction_boxes]

    for _, p1, p2 in pairs[:n_connections]:
        c1 = c2 = None
        for c in circuits:
            # puts cX as the circuit that has pX
            if p1 in c:
                c1 = c
                print(f'{c} contains {p1}!')
            if p2 in c:
                print(f'{c} contains {p2}!')
                c2 = c

        if c1 is not c2:
            # if they are not the same, merge and remove
            c1.update(c2)
            print(f'Updated {c1} to include {c2}')
            circuits.remove(c2)
            print(f'Removed {c2}')

    len_circuits = []
    for c in circuits:
        len_circuits.append(len(c))

    len_circuits.sort()

    product = math.prod(len_circuits[-3:])


    return product


def part2():
    junction_boxes = parse_points()

    pairs = min_distances(junction_boxes)

    circuits = [{box} for box in junction_boxes]

    for _, p1, p2 in pairs:
        c1 = c2 = None
        for c in circuits:
            # puts cX as the circuit that has pX
            if p1 in c:
                c1 = c
                print(f'{c} contains {p1}!')
            if p2 in c:
                print(f'{c} contains {p2}!')
                c2 = c

        if c1 is not c2:
            # if they are not the same, merge and remove
            c1.update(c2)
            print(f'Updated {c1} to include {c2}')
            circuits.remove(c2)
            print(f'Removed {c2}')

        if len(circuits) == 1:
            print(f'The juntion boxes that connected the last 2 circuits were {p1} and {p2}')
            return p1[0]*p2[0]








result = part2()
print(result)