#!/usr/bin/python

import sys

prev_key = ""
total_value = 0

for line in sys.stdin:
    key,svalue = line.split("\t",1)
    value = int(svalue)
    if key != prev_key:
        if prev_key != "":
            print ("%s\t%d")%(prev_key,total_value)
        prev_key = key
        total_value = value
    else:
        total_value += value
       
print ("%s\t%d")%(prev_key,total_value)     
