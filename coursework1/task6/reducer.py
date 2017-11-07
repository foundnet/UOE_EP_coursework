#!/usr/bin/python

import sys
import math

prev_key = ""
hresult = 0.0
totalcnt = 0
cntlist = []

for line in sys.stdin:
    key,info = line.strip().split("\t",1)
    if key != prev_key:
        if prev_key != "":
           hresult = 0.0
           cntlist = strinfo.split(",")
           cntlist = map(int,cntlist)
           totalcnt = sum(cntlist)
           for v in cntlist:
               hresult = hresult - float(v) / totalcnt *\
                                   math.log(float(v)/totalcnt,2)
           print "%s\t%f"%(prev_key,hresult)
        prev_key = key
        strinfo = info.strip()
    else:
        strinfo = strinfo + "," + info.strip()

if prev_key != "":
    hresult = 0.0
    cntlist = strinfo.split(",")
    cntlist = map(int,cntlist)
    totalcnt = sum(cntlist)
    for v in cntlist:
        hresult = hresult - float(v) / totalcnt *\
                            math.log(float(v)/totalcnt,2)
    print "%s\t%f"%(prev_key,hresult)
       
