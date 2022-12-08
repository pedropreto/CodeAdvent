#!/usr/bin/env python
# -*- coding: utf-8 -*-
import copy
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


class Directory:
    def __init__(self, name, level, base_folder, folders=[], files=[], size=0, size_calculated=False):
        self.level = level
        self.name = name
        self.folders = folders
        self.files = files
        self.base_folder = base_folder
        self.size = size
        self.size_calculated = size_calculated

    # def __eq__(self, other):
    #     return self.name == other.name and self.base_folder == other.base_folder

    def __repr__(self):
        if self.base_folder == '':
            base = ''
        else:
            base = self.base_folder.name
        return "\n\nname:" + self.name + "\nsize:" + str(self.size) + "\nnumber of folders:" + str(len(self.folders)) + \
               "\nnumber of files:" + str(len(self.files)) + "\nbase folder:" + base + "\nlevel:" + str(self.level)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return "name:" + self.name + ", size:" + str(self.size)


def part1():
    level, last_level = 1, 0
    last_folder = ''
    folder_list = []
    folder = Directory(name="root", base_folder=last_folder, level=level) # root
    folder_list.append(folder)
    for idx, line in enumerate(lines):
        print(line)
        line_split = line.split(' ')
        if line_split[0] == '$':
            if line_split[1] == 'cd':
                if not "." in line_split[2]:  # does not contain .

                    if level > last_level:
                        last_level = level

                    level += 1
                    last_folder = folder

                else:  # go back
                    last_folder = last_folder.base_folder
                    level -= 1
        else:
            if line_split[0] == 'dir':
                folder_name = line_split[1]
                folder = Directory(name=folder_name, base_folder=last_folder, level=level)

                folder_list.append(folder)

                folder.base_folder.folders.append(folder)
            else:
                file_size = int(line_split[0])
                file_name = line_split[1]
                file = File(name=file_name, size=file_size)
                last_folder.files.append(file)

    for fol in folder_list:
        if fol.level == last_level:
            check_folder_size_files(fol)

    sum_size = 0
    for fol in folder_list:
        if fol.size <= 100000:
            sum_size += fol.size

    return folder_list, sum_size


def part2():
    marker_number, first_marker, input = 14, 0, lines[0]
    for i in range(marker_number, len(input)):
        x = input[i - marker_number:i]
        if len(set(x)) == len(x):
            first_marker = i
            break

    return first_marker


def check_folder_size_v2(folder):
    if folder.size_calculated:
        pass
    else:
        folder.size_calculated = True
        for file in folder.files:
            folder.size += int(file.size)
        for dir in folder.folders:
            if dir.size_calculated:
                folder.size += dir.size
            else:
                check_folder_size_v2(dir)


def check_folder_size_files(folder):
    for file in folder.files:
        folder.size += file.size
    folder.base_folder.size += folder.size



result, sum = part1()
print(result, sum)
