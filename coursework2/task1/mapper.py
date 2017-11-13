#!/usr/bin/python

import sys
import os

file_name = os.environ["mapreduce_map_input_file"]
file_name = file_name[file_name.rfind("/")+1:]

for line in sys.stdin:
    line = line.strip()
    token_list = line.split(" ")
    for item in token_list:
        if item.strip() != "":
            print item.strip() + "\t" + file_name + "\t1"
