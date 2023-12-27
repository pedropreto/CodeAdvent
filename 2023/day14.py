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
    print(lines)
    transposed_matrix = list(zip(*lines))
    print(transposed_matrix)
    load = 0
    for line in transposed_matrix:
        n_boulders = sum(word.count('O') for word in line)
        print(n_boulders)
        boulders_indices = [index for index, word in enumerate(line) for char_index, char in
                        enumerate(word) if char == 'O']
        cubic_boulders_indices = [index for index, word in enumerate(line) for char_index, char in
                        enumerate(word) if char == '#']
        print(boulders_indices)
        print(cubic_boulders_indices)
        rearranged_boulders_indices = []

        for general_idx, boulders_idx in enumerate(boulders_indices):
            if len(cubic_boulders_indices) == 0:
                load += len(line) - general_idx
                print(load)
            else:
                for cubic_boulders_idx in cubic_boulders_indices:
                    count_cubic_ahead = sum(1 for element in cubic_boulders_indices if element < boulders_idx)
                    if cubic_boulders_indices[count_cubic_ahead - 1] != cubic_boulders_idx:
                        continue
                    elif boulders_idx < cubic_boulders_idx and count_cubic_ahead in [0, 1]:
                        load += len(line) - general_idx
                        rearranged_boulders_indices.append(general_idx)
                        print(load)
                        break
                    else:
                        count_after_cubic = sum(1 for element in rearranged_boulders_indices if element > cubic_boulders_idx)

                        load += len(line) - (cubic_boulders_idx + (count_after_cubic) + 1)

                        rearranged_boulders_indices.append((cubic_boulders_idx + (count_after_cubic) + 1))
                        print(load)

    return load


result = part1()
print(result)

