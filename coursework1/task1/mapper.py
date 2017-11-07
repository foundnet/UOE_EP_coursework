#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    if line != "": 
        print line

