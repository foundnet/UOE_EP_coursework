#!/usr/bin/python

import sys

prev_sid = ""
cntcourse = 0
totalmark = 0
lowlist = []

for line in sys.stdin:
    sid, info = line.strip().split("\t",1)
    scount,smark = info.split(",")
    if sid != prev_sid:
        if prev_sid != "":
            if cntcourse > 3:
                avgmark = float(totalmark) / cntcourse
                if len(lowlist) == 0:
                    lowlist.append((prev_sid , avgmark))
                elif avgmark == (lowlist[0])[1]:
                    lowlist.append((prev_sid , avgmark))
                elif avgmark < (lowlist[0])[1]:
                    lowlist = []
                    lowlist.append((prev_sid , avgmark))
        prev_sid = sid
        cntcourse = int(scount)
        totalmark = int(smark)
    else:
        cntcourse += int(scount)
        totalmark += int(smark)

if prev_sid != "":
    if cntcourse > 3:
        avgmark = float(totalmark) / cntcourse
        if len(lowlist) == 0:
            lowlist.append((prev_sid , avgmark))
        elif avgmark == (lowlist[0])[1]:
            lowlist.append((prev_sid , avgmark))
        elif avgmark < (lowlist[0])[1]:
            lowlist = []
            lowlist.append((prev_sid , avgmark))

for item in lowlist:
    print "names: %s scores: %.1f"%(item[0],item[1])
