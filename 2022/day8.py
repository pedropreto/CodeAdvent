#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import string
import numpy as np
import regex as re

py_name = os.path.basename(__file__)
file = "day" + re.findall(r'\d+', py_name)[0] + ".txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def bothparts():
    best_scenic_score = 0
    visible_trees = 0
    matrix = np.zeros((len(lines), len(lines[0])))
    for idx, l in enumerate(lines):
        row = [int(d) for d in str(l)]
        matrix[idx] = row

    border_trees = len(lines[0]) + 2 * (len(lines) - 1) + (len(lines[0]) - 2)
    visible_trees += border_trees
    for x, element in enumerate(matrix):
        if x == 0 or x == len(matrix) - 1:
            pass
        else:
            inner_element = element[1:-1]
            i = 1

            for el in inner_element:
                visibles, scenic_score, visible_trees_list = check_visibility(m=matrix, coords=[x, i], el=el)

                if scenic_score >= best_scenic_score:
                    best_scenic_score = scenic_score

                i += 1

                if any(visibles):
                    visible_trees += 1

    return visible_trees, best_scenic_score


def check_visibility(m, coords, el):
    visibles = []
    visible_trees_list = []
    top = m[:coords[0], coords[1]].tolist()
    left = m[coords[0], :coords[1]].tolist()
    top.reverse()
    left.reverse()
    right = m[coords[0], coords[1] + 1:].tolist()
    down = m[coords[0] + 1:, coords[1]].tolist()

    visibility_lines = [top, left, right, down]

    for j in visibility_lines:
        visible, lower_trees = check_visibility_line(el, j)
        visibles.append(visible)
        visible_trees_list.append(lower_trees)

    scenic_score = np.prod(visible_trees_list)

    return visibles, scenic_score, visible_trees_list


def check_visibility_line(el, line):
    lower_trees = 0
    for i in line:
        lower_trees += 1
        if i >= el:
            return False, max(lower_trees, 1)

    return True, lower_trees


result, scenic_score = bothparts()
print(result, scenic_score)



