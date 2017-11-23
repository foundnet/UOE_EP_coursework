#!/usr/bin/python

import sys
import random

sel_list = []
cur_line = 0

if len(sys.argv) != 2 :
    print "Error:Should have one parameter to specify the sample count."
    sys.exit(0)

sample_line = int(sys.argv[1])

for line in sys.stdin:
    if line.strip()== "":
        continue
    cur_line += 1

    if random.randint(1,cur_line) <= sample_line :
        if len(sel_list) == sample_line:
            del sel_list[random.randint(0,sample_line-1)]
        sel_list.append(line.strip())

cur_line = 0
for item in sel_list :
    cur_line += 1
    print item

