#!/usr/bin/python

import sys

prev_sid = ""
cntcourse = 0
totalmark = 0

for line in sys.stdin:
    sid, info = line.strip().split("\t",1)
    scount,smark = info.split(",")
    if sid != prev_sid:
        if prev_sid != "":
            print "%s\t%d,%d"%(prev_sid,cntcourse,totalmark)
        prev_sid = sid
        cntcourse = int(scount)
        totalmark = int(smark)
    else:
        cntcourse += int(scount)
        totalmark += int(smark)

if prev_sid != "":
    print "%s\t%d,%d"%(prev_sid,cntcourse,totalmark)
