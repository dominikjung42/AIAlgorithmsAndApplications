# -*- coding: utf-8 -*-
"""
Lecture 4 - Data Engineering
@author: Dominik Jung (dominik.jung42@gmail.com)
"""
import csv

read_file = open("delimited_file.txt", mode="r")
reader = csv.reader(read_file, delimiter="|")

my_dictionnary = {}

next(reader)

for row in reader:
    model = row[0]
    comment = row[1]
    user = row[2]
    my_dictionnary[user] = [model, comment]

read_file.close()


# Model | Comment | UserID
# 911 | "i like the sound of the motor" | 1
# 718 | "best car ever " | 4

