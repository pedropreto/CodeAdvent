#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import os
import re
import numpy as np

file = 'day' + re.findall(r'\d+', os.path.basename(__file__))[0] + '.txt'
file_path = os.path.join("inputs", file)

# opens the file
with open(file_path) as f:
    lines = [line.rstrip() for line in f]  # takes the \n

farmer_dict = {"my_seeds": re.findall(r'\d+', lines[0].split(':')[1]),
                   "seed-to-soil map": list(), "soil-to-fertilizer map": list(),
                   "fertilizer-to-water map": list(), "water-to-light map": list(), "light-to-temperature map": list(),
                   "temperature-to-humidity map": list(), "humidity-to-location map": list()}




def part1():

    maps = [[]]
    for line in lines:
        maps.append([]) if not line else maps[-1].append(line)

    for j in range(1, len(maps)):
        print(maps[j][0].replace(':', ''))
        put_in_dict(maps[j], maps[j][0].replace(':', ''))

    print(farmer_dict)

    elements_to_convert = farmer_dict["my_seeds"]
    print('seed-to-soil')
    elements_to_convert = convert("seed-to-soil map", elements_to_convert)
    print('soil-to-fert')
    elements_to_convert = convert("soil-to-fertilizer map", elements_to_convert)
    print('fert-to-water')
    elements_to_convert = convert("fertilizer-to-water map", elements_to_convert)
    print('water-to-light')
    elements_to_convert = convert("water-to-light map", elements_to_convert)
    print('light-to-temp')
    elements_to_convert = convert("light-to-temperature map", elements_to_convert)
    print('temp-to-hum')
    elements_to_convert = convert("temperature-to-humidity map", elements_to_convert)
    print('hum-to-location')
    elements_to_convert = convert("humidity-to-location map", elements_to_convert)

    print(elements_to_convert)

    return min(elements_to_convert)


def part2():
    maps = [[]]
    for line in lines:
        maps.append([]) if not line else maps[-1].append(line)

    for j in range(1, len(maps)):
        print(maps[j][0].replace(':', ''))
        put_in_dict(maps[j], maps[j][0].replace(':', ''))

    print(farmer_dict)

    elements_to_convert = list()
    element_start = list()
    element_range = list()

    for idx, i in enumerate(farmer_dict["my_seeds"]):
        if idx % 2 == 0:
            element_start.append(i)
        else:
            element_range.append(i)

    print(element_start, element_range)

    for idx_el, el in enumerate(element_start):
        for idx_map, z in enumerate(farmer_dict["seed-to-soil map"]):
            destination, start_source, rng = z
            start_el, destination, start_source, rng = int(el), int(destination), int(start_source), int(rng)
            final_el = start_el + int(element_range[idx_el])
            final_source = start_source + rng
            if start_source <= start_el < final_source:
                print(f"{start_el} is inside the interval [{start_source}, {final_source}]")
                elements_to_convert.append(start_el) if start_el not in elements_to_convert else None
                max_value_interval = min(final_el, final_source - 1)
                elements_to_convert.append(max_value_interval) if max_value_interval not in elements_to_convert else None

            if start_source >= start_el and final_source - 1 <= final_el:
                print(f"The interval [{start_source}, {final_source - 1}] is contained on the interval [{start_el}, {final_el}]")
                elements_to_convert.append(final_source - 1) if final_source - 1 not in elements_to_convert else None
                elements_to_convert.append(start_source) if start_source not in elements_to_convert else None

            if final_el not in elements_to_convert:
                elements_to_convert.append(final_el - 1)

            if start_el not in elements_to_convert:
                elements_to_convert.append(start_el)

            print(elements_to_convert)

    elements_to_convert = convert("seed-to-soil map", elements_to_convert)
    print('soil-to-fert')
    elements_to_convert = convert("soil-to-fertilizer map", elements_to_convert)
    print('fert-to-water')
    elements_to_convert = convert("fertilizer-to-water map", elements_to_convert)
    print('water-to-light')
    elements_to_convert = convert("water-to-light map", elements_to_convert)
    print('light-to-temp')
    elements_to_convert = convert("light-to-temperature map", elements_to_convert)
    print('temp-to-hum')
    elements_to_convert = convert("temperature-to-humidity map", elements_to_convert)
    print('hum-to-location')
    elements_to_convert = convert("humidity-to-location map", elements_to_convert)

    print(elements_to_convert)

    return min(elements_to_convert)


def convert(key, elements_to_convert):
    new_elements_to_convert = list()

    for el in elements_to_convert:
        for z in farmer_dict[key]:
            destination_number, source_number, rng = z
            # source is on the range
            if int(source_number) <= int(el) < int(source_number) + int(rng):
                dif = int(el) - int(source_number)
                match_number = int(destination_number) + dif
                match = True
                new_elements_to_convert.append(match_number)
                break
            else:
                match = False
        if not match:
            new_elements_to_convert.append(int(el))

    elements_to_convert = new_elements_to_convert

    return elements_to_convert


def put_in_dict(element, dict_key):
    for i in range(1, len(element)):
        map = re.findall(r'\d+', element[i])
        farmer_dict[dict_key].append(map)


result = part2()
print(result)
