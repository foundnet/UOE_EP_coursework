#!/usr/bin/python

import sys

prev_key = ""
strinfo = ""

tokendic = {}
valuelist = []

for line in sys.stdin:
    line = line.strip()
    if line.find("\t") >= 0:
        key,info = line.strip().split("\t")
        if key != prev_key:
            if prev_key != "":
                print prev_key+"\t"+strinfo.strip()
            prev_key = key
            strinfo = info.strip()
        else:
            strinfo = strinfo.strip()+ "," + info.strip()

if prev_key != "":
    print prev_key+"\t"+strinfo.strip()
      
