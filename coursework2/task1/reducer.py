#!/usr/bin/python

import sys

prev_token = ""
prev_file = ""
cur_count = 0
token_count = 0
token_list = []

for line in sys.stdin:
    line = line.strip()
    if line.find("\t") >= 0:
        token_name,file_name,scount = line.strip().split("\t",2)
        if token_name != prev_token:
            if prev_token != "":
               token_list.append([prev_file,str(cur_count)])
               str_list = "{"
               for item in token_list:
                   str_list = str_list + "(" + ','.join(item) + "), "
               str_list = str_list[:-2]
               str_list = str_list + "}"
               print prev_token + ":" + str(token_count) + ":" + str_list.strip()
            prev_token = token_name
            prev_file = file_name
            cur_count = int(scount)
            token_count = 1
            token_list = []
        else:
            if file_name != prev_file:
                token_list.append([prev_file,str(cur_count)])
                prev_file = file_name
                cur_count = int(scount)
                token_count = token_count + 1
            else:
                cur_count = cur_count + int(scount)

if prev_token != "":
    token_list.append([prev_file,str(cur_count)])
    str_list = "{"
    for item in token_list:
        str_list = str_list + "(" + ','.join(item) + "), "
    str_list = str_list[:-2]
    str_list = str_list + "}"
    print prev_token + ":" + str(token_count) + ":" + str_list.strip()
