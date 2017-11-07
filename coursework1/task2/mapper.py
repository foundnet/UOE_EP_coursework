#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    if line != "": print line+"\t1"
