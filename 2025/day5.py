#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


class Interval:
    def __init__(self, value):
        # Expect format "a-b"
        parts = value.split("-")
        self.min = int(parts[0])
        self.max = int(parts[1])

    def __repr__(self):
        return f"Interval({self.min}, {self.max})"

    def __str__(self):
        return f"{self.min}-{self.max}"

    def contains(self, x):
        return self.min <= x <= self.max

    def __len__(self):
        return self.max - self.min + 1

    def __eq__(self, other):
        if isinstance(other, Interval):
            return self.min == other.min and self.max == other.max
        return False


def split_inputs(input):
    try:
        idx = input.index('')
    except ValueError:
        idx = len(input)
    return input[:idx], input[idx + 1:]


def combine_intervals(interval_list):
    # gets the min min and max max of a list of intervals that are contained inside each other
    min_min = str(min(i.min for i in interval_list))
    max_max = str(max(i.max for i in interval_list))
    return Interval(min_min + '-' + max_max)


def part1():
    fresh = []
    intervals, ingredients = split_inputs(lines)

    for ingredient in ingredients:
        for interval in intervals:
            firstValue = int(interval.split('-')[0])
            lastValue = int(interval.split('-')[1])
            if firstValue <= int(ingredient) <= lastValue:
                fresh.append(int(ingredient))
                break

    return len(fresh)


def part2():
    intervals, _ = split_inputs(lines)
    final_interval_list = []
    # goes through all intervals in the input
    for interval in intervals:

        interval_instance = Interval(interval)
        contained_list = [interval_instance]
        # goes through all final intervals evaluated, with the merged
        for element in final_interval_list:
            # check if new interval element from input is contained totally or partially inside some
            # of the previously stored intervals
            # or the other way around
            if interval_instance.contains(element.min) or interval_instance.contains(element.max)\
                    or element.contains(interval_instance.min) or element.contains(interval_instance.max):
                contained_list.append(element)

        merged_interval = combine_intervals(contained_list)

        if len(contained_list) > 1:
            # remove all intervals that were merged
            for c in contained_list:
                try:
                    final_interval_list.remove(c)
                except ValueError:
                    pass

        final_interval_list.append(merged_interval)


    fresh_ingredients = 0
    for i in final_interval_list:
        fresh_ingredients += len(i)

    return fresh_ingredients



result = part2()
print(result)