#!/usr/bin/python

import sys

tklist = []

for line in sys.stdin:
    tklist = line.strip().split()
    if tklist[0] == "mark":
        print "%s\t1,%s"%(tklist[1],tklist[3])

