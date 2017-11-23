#!/usr/bin/python

import sys
import random

sel_line = ""
cur_line = 0

for line in sys.stdin:
    if line.strip()== "": 
        continue
    cur_line += 1

    if random.randint(1,cur_line) == 1:
        sel_line = line.strip()

if sel_line != "":
    print str(cur_line) + "\t" + sel_line
