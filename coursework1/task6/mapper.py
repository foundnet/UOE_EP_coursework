#!/usr/bin/python

import sys

for line in sys.stdin:
    line = line.strip()
    if line.find('\t') >= 0:
        key,scount = line.split("\t",1)
        listkey = key.split(" ",3)
        newkey = listkey[0]+" "+listkey[1]+" "+listkey[2]
        print newkey.strip()+"\t"+scount.strip()
