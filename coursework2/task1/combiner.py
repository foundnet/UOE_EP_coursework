#!/usr/bin/python

import sys

prev_token = ""
prev_file = ""
cur_count = 0

for line in sys.stdin:
    line = line.strip()
    if line.find("\t") >= 0:
        token_name,file_name,scount = line.strip().split("\t",2)
        if token_name != prev_token:
            if prev_token != "":
               print prev_token + "\t" + prev_file + "\t" + str(cur_count)
            prev_token = token_name
            prev_file = file_name
            cur_count = int(scount)

        else:
            if file_name != prev_file:
                print prev_token + "\t" + prev_file + "\t" + str(cur_count)
                prev_file = file_name
                cur_count = int(scount)
            else:
                cur_count = cur_count + int(scount)

if prev_token != "":
    print prev_token + "\t" + prev_file + "\t" + str(cur_count)
      
