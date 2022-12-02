#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os

file = "day2.txt"
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    final_score = 0
    score = {"X": 1, "Y": 2, "Z": 3}
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}

    for l in lines:
        play = l.split()
        if play[1] == wins[play[0]]:
            final_score += score[play[1]] + 6
        elif play[1] == draws[play[0]]:
            final_score += score[play[1]] + 3
        else:
            final_score += score[play[1]]

    return final_score


def part2():

    final_score = 0
    loses = {"A": "Z", "B": "X", "C": "Y"}
    wins = {"A": "Y", "B": "Z", "C": "X"}
    draws = {"A": "X", "B": "Y", "C": "Z"}
    score_play = {"X": 1, "Y": 2, "Z": 3}
    score_round = {"X": 0, "Y": 3, "Z": 6}

    strategy = {"X": loses, "Y": draws, "Z": wins}

    for l in lines:
        play = l.split()
        myplay = strategy[play[1]][play[0]]

        final_score += score_play[myplay] + score_round[play[1]]

    return final_score



count = part2()
print(count)

