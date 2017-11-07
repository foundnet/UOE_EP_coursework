#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    tokens = line.split()
    if len(tokens) > 3:
        for index in range(len(tokens)-3):
            print ("%s %s %s %s\t1")%(tokens[index],tokens[index+1],\
                   tokens[index+2],tokens[index+3])
        
        
