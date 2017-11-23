#!/usr/bin/python

import sys

cur_aid = ""
cur_qid = ""
cur_uid = ""

for line in sys.stdin:
    str_aid,str_id = line.split("\t",1)
    str_sid = str_aid.strip()
    str_id = str_id.strip()
    if str_aid == "" or str_id == "":
        continue
    if str_aid != cur_aid:
        if cur_aid != "" and cur_qid != "" and cur_uid != "":
            print cur_uid + "\t1\t" + cur_qid
        cur_aid = str_aid
        cur_qid = ""
        cur_uid = ""
    if str_id[0] == 'Q':
        if cur_qid != "":
            print "Warning:Qid already exist:" + cur_qid
        cur_qid = str_id[1:]
    elif str_id[0] == "U":
        if cur_uid != "":
            print "Warning:Uid already exist:" + cur_uid
        cur_uid = str_id[1:]
        
if cur_aid != "" and cur_qid != "" and cur_uid != "":
    print cur_uid + "\t1\t" + cur_qid
 
