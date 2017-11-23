#!/usr/bin/python

import sys
import math

counters = {}

s_threshold = 0.01
e_errorrate = 0.01 - 0.009

win_size = math.ceil(1 / e_errorrate)

index = 0

del_lines = []

for line in sys.stdin:
    line = line.strip()
    if line in counters:
        counters[line] += 1
    else:
        counters[line] = 1

    index += 1
    if index % win_size == 0 :
        del_lines = []
        for str_key,cnt_value in counters.items():
            if cnt_value <= 1 :
                del_lines.append(str_key)
            else :
                counters[str_key] -= 1
        for str_key in del_lines:
            del counters[str_key]

dic_size = 0
out_seq = 0
for str_key,cnt_value in counters.items():
    dic_size += 1
    if cnt_value > int(s_threshold * index):
        out_seq += 1
        sys.stderr.write( "LINE %d:CNT %d:HASH-%s"%(out_seq,(cnt_value+int(index/win_size)),str_key)+"\n")
        print str_key
  
sys.stderr.write("\n----THE FINAL DICT SIZE IS %d, TOTAL %d LINES, WIN SIZE %d, OUTPUT %d LINES----\n"%(dic_size,index,win_size,out_seq) )

