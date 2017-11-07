#!/usr/bin/python

import sys

prev_line = ""
is_repeat = False

for line in sys.stdin:
    sline,temp = line.strip().split("\t")
    if prev_line != sline:
        if prev_line != "" and is_repeat == False:
            print prev_line+"\t1"
        prev_line = sline
        is_repeat = False
    else:
        is_repeat = True

if is_repeat == False:
    print prev_line+"\t1"
