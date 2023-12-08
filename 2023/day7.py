#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import time
import os
import re
import numpy as np

start = time.time() * 1000

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n


def part1():
    card_value = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}
    hands, bids = [], []
    for line in lines:
        hand, bid = line.split(' ')
        hands.append(hand), bids.append(bid)

    ranks = [0] * len(hands)
    for i, hand1 in enumerate(hands):
        won = 0
        for j, hand2 in enumerate(hands):
            if i != j:
                result = compare_hands([hand1, hand2], card_value)
                if result:
                    won += 1

        ranks[i] = won + 1

        product = [int(x) * int(y) for x, y in zip(ranks, bids)]

    return sum(product)


def part2():
    card_value = {"J": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9,
                  "T": 10, "Q": 12, "K": 13, "A": 14}

    # result = compare_hands_part2(['T55J5', 'K55J5'], card_value)
    hands, bids = [], []
    for line in lines:
        hand, bid = line.split(' ')
        hands.append(hand), bids.append(bid)

    ranks = [0] * len(hands)
    for i, hand1 in enumerate(hands):
        won = 0
        for j, hand2 in enumerate(hands):
            if i != j:
                result = compare_hands_part2([hand1, hand2], card_value)
                if result:
                    won += 1

        ranks[i] = won + 1
    print(ranks)

    product = [int(x) * int(y) for x, y in zip(ranks, bids)]

    return sum(product)


def compare_hands_part2(hand_list, card_value):
    point_attr = {2: 1, 3: 4, 4: 9, 5: 16}
    first_hand, second_hand = hand_list
    # count cards in each hand
    count_dict_fh, count_dict_sh = {}, {}
    fh_unique, sh_unique = "".join(set(first_hand)), "".join(set(second_hand))
    for idx, card in enumerate(fh_unique):
        fh_counter = first_hand.count(card)
        count_dict_fh[card] = fh_counter

    for idx, card in enumerate(sh_unique):
        sh_counter = second_hand.count(card)
        count_dict_sh[card] = sh_counter

    hands_counter = [count_dict_fh, count_dict_sh]

    points = [0, 0]
    joker = 'J'

    for idx, dict in enumerate(hands_counter):
        if joker in dict:
            n_joker = dict[joker]
            del dict[joker]
            print(first_hand, second_hand)
            dict[max(dict, key=dict.get)] += n_joker

        for key, value in dict.items():
            points[idx] += (value - 1) ** 2

    if points[0] > points[1]:
        return True
    elif points[1] > points[0]:
        return False
    else:
        for card1, card2 in zip(first_hand, second_hand):
            if card_value[card1] > card_value[card2]:
                return True
            if card_value[card2] > card_value[card1]:
                return False


def compare_hands(hand_list, card_value):
    first_hand, second_hand = hand_list
    # count cards in each hand
    count_dict_fh, count_dict_sh = {}, {}
    fh_unique, sh_unique = "".join(set(first_hand)), "".join(set(second_hand))
    for idx, card in enumerate(fh_unique):
        fh_counter = first_hand.count(card)
        count_dict_fh[card] = fh_counter

    for idx, card in enumerate(sh_unique):
        sh_counter = second_hand.count(card)
        count_dict_sh[card] = sh_counter

    hands_counter = [count_dict_fh, count_dict_sh]
    points = [0, 0]

    for idx, dict in enumerate(hands_counter):
        for key, value in dict.items():
            points[idx] += (value - 1) ** 2

    if points[0] > points[1]:
        return True
    elif points[1] > points[0]:
        return False
    else:
        for card1, card2 in zip(first_hand, second_hand):
            if card_value[card1] > card_value[card2]:
                return True
            if card_value[card2] > card_value[card1]:
                return False


result = part2()
print(result)

end = time.time() * 1000

print(f'This took {(end-start)} miliseconds')
