#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path, "r") as f:
    lines = [list(line.rstrip()) for line in f]


def get_coordinates():
    rows = len(lines)
    cols = len(lines[0])
    coord_splitters = []
    coord_beam = (0,0)
    for i in range(rows):
        for j in range(cols):
            if lines[i][j] == 'S':
                coord_beam = [i+1,j]
            if lines[i][j] == '^':
                coord_splitters.append((i,j))
    return coord_beam, coord_splitters


def get_row_splitters(row, all_splitters):
    row_splitters = []
    for splitter in all_splitters:
        if splitter[0] == row:
            row_splitters.append(splitter)
        elif splitter[0] > row:
            break
    return row_splitters


def part1():
    beam, splitters = get_coordinates()
    # register only the columns
    last_beams = {beam[1]}
    beams_row = beam[0]
    n_splits = 0
    while beams_row < len(lines):
        # check the row where we are and check for splitters in the next row
        next_splitters = get_row_splitters(beams_row+1, splitters)
        new_beams = set()
        if len(next_splitters) > 0:
            for b in last_beams:
                split = False

                for s in next_splitters:
                    if b == s[1]:
                        print(f'Beam in row {beams_row} and column {b} split in two!')
                        print(f'They are now in columns {s[1] + 1} and {s[1] - 1}')
                        # split and fall one row to simplify
                        new_beams.add(s[1] + 1)
                        new_beams.add(s[1] - 1)
                        split = True
                        n_splits += 1
                        break

                if not split:
                    new_beams.add(b)

            last_beams = new_beams
        beams_row += 1
        print(f'Beams going to row {beams_row}\n')
    return n_splits


result = part1()
print(result)