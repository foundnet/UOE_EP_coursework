#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip("\r\n\t")
    clength = len(line)
    tlength = len(line.split())
    print ("{0}\t{1}".format(clength,tlength))

