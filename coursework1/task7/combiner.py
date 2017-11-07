#!/usr/bin/python

import sys

prev_sid = ""
strinfo = ""

for line in sys.stdin:
    sid , info = line.strip().split("\t",1)
    if sid != prev_sid:
    	if prev_sid != "":
            if strinfo == "": strinfo = "_NOCOURSE"
            print "%s\t%s"%(prev_sid,strinfo.strip())
        prev_sid = sid
        if info == "_NOCOURSE": strinfo = ""
        else:
            strinfo = info
    else:
        if info != "_NOCOURSE": strinfo = strinfo + "  " + info.strip()
                

if prev_sid != "":
    if strinfo == "": strinfo = "_NOCOURSE"
    print "%s\t%s"%(prev_sid,strinfo.strip())

