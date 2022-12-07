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
    def __init__(self, name, base_folder, folders=[], files=[], size=0, size_calculated=False):
        self.name = name
        self.folders = folders
        self.files = files
        self.base_folder = base_folder
        self.size = size
        self.size_calculated = size_calculated

    def __repr__(self):
        if self.base_folder == '':
            base = ''
        else:
            base = self.base_folder.name
        return "name:" + self.name + "\nsize:" + str(self.size) + "\nnumber of folders:" + str(len(self.folders)) + \
               "\nnumber of files:" + str(len(self.files)) + "\nbase folder:" + base


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __repr__(self):
        return "name:" + self.name + ", size:" + str(self.size)


def part1():
    last_folder = ''
    folder_list = []
    for idx, line in enumerate(lines):
        print(line)
        line_split = line.split(' ')
        if line_split[0] == '$':
            if line_split[1] == 'cd':
                if not "." in line_split[2]:  # does not contain .
                    folder_name = line_split[2]
                    folder = Directory(name=folder_name, base_folder=last_folder)
                    folder_list.append(folder)
                    last_folder = copy.copy(folder)
                else:
                    last_folder = copy.copy(last_folder.base_folder)
        else:
            if line_split[0] == 'dir':
                folder_name = line_split[1]
                folder = Directory(name=folder_name, base_folder=last_folder)
                folder_list.append(folder)
                last_folder.folders.append(folder)
            else:
                file_size = line_split[0]
                file_name = line_split[1]
                file = File(name=file_name, size=file_size)
                last_folder.files.append(file)

    for fol in folder_list:
        check_folder_size(fol)

    return folder_list


def part2():
    marker_number, first_marker, input = 14, 0, lines[0]
    for i in range(marker_number, len(input)):
        x = input[i - marker_number:i]
        if len(set(x)) == len(x):
            first_marker = i
            break

    return first_marker


def check_folder_size(folder):
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
                check_folder_size(dir)


count = part1()
print(count)
