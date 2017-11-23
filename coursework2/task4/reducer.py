#!/usr/bin/python

import sys
import random

total_cnt = 0
sel_line = ""

for line in sys.stdin:
    try:
        str_cnt,str_line = line.strip().split("\t",1)
        str_cnt = str_cnt.strip()
        str_line = str_line.strip()
    except:
        print "ERROR_LINE:" +  line
        break

    if str_cnt != ""  and str_line != "":
        cur_count = int(str_cnt)
        total_cnt += cur_count
        if random.randint(1,total_cnt) <= cur_count:
            sel_line = str_line

if sel_line != "":
    print sel_line
