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
    score = 0

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == '0':
                trailheads_reached = []
                follow_path = []
                coordinates = (i, j)
                # point where we are at
                follow_path.append(coordinates)

                while True:

                    print(f'The paths to follow are {follow_path}')

                    visit_next = []
                    value = int(lines[coordinates[0]][coordinates[1]])

                    print(f'\nThe current coordinates are {coordinates} and the value is {value}.')


                    if value == 9:
                        if coordinates not in trailheads_reached:
                            # comment the following line for part 2
                            # trailheads_reached.append(coordinates)
                            score += 1
                            print(f'Score is {score}')
                        else:
                            print(f'Trailhead already visited')


                    else:
                        # start searching for 0s
                        # check up
                        visit_next.insert(-1, (coordinates[0] - 1, coordinates[1])) if len(lines) > coordinates[0]-1 >= 0 else None
                        # check down
                        visit_next.insert(-1, (coordinates[0] + 1, coordinates[1])) if len(lines) > coordinates[0] + 1 >= 0 else None
                        # check left
                        visit_next.insert(-1, (coordinates[0], coordinates[1] - 1)) if len(lines[0]) > coordinates[1] - 1 >= 0 else None
                        # check right
                        visit_next.insert(-1, (coordinates[0], coordinates[1] + 1)) if len(lines[0]) > coordinates[1] + 1 >= 0 else None

                    print(f'Places to visit next: {visit_next}')

                    print(f'\nTrailheads visited: {trailheads_reached}.')




                    for point in visit_next:
                        next_value = lines[point[0]][point[1]]
                        print(f'Visiting {point}...')
                        try:
                            print(f'The position has the character {next_value}')
                            if int(next_value) == value + 1:
                                follow_path.append(point)


                        except ValueError:
                            print(f'Char is not a number')

                    follow_path.remove(coordinates)

                    if len(follow_path) > 0:
                        coordinates = follow_path[-1]
                    else:
                        print(f'Reached a dead end')
                        break



    return score

result = part1()
print(result)