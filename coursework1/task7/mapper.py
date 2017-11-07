#!/usr/bin/python

import sys

tklist = []

for line in sys.stdin:
    tklist = line.strip().split()
    if tklist[0] == "student":
        print "%s\t_NOCOURSE"%(tklist[1])
    elif tklist[0] == "mark":
        print "%s\t(%s,%s)"%(tklist[1],tklist[3],tklist[2])
    else:
        continue
 
